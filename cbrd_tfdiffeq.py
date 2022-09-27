import numpy as np
import tensorflow as tf
from tfdiffeq import odeint, odeint_adjoint

import matplotlib.pyplot as plt

erf = tf.math.erf
sqrt = tf.math.sqrt
exp = tf.math.exp
maximum = tf.math.maximum
minimum = tf.math.minimum
abs = tf.math.abs
logical_and = tf.math.logical_and
logical_not = tf.math.logical_not

SQRT_FROM_2 = np.sqrt(2)
SQRT_FROM_2_PI = 0.7978845608028654

class BaseNeuron(tf.keras.Model):

    def __init__(self, params):
        super(BaseNeuron, self).__init__(name="NeuronPopulation")

        self.Vreset = tf.constant(params["Vreset"], shape=[1, ], dtype=tf.float64)
        self.Vt = tf.constant(params["Vt"], dtype=tf.float64)

        self.gl =  tf.constant(params["gl"], dtype=tf.float64)
        self.El =  tf.constant(params["El"], dtype=tf.float64)
        self.C =  tf.constant(params["C"], dtype=tf.float64)
        self.sigma = tf.constant(params["sigma"], dtype=tf.float64)

        self.ref_dvdt = params["ref_dvdt"]   # refactory in updates of V and variables of states
        self.refactory = params["refactory"] # refactory for threshold


        self.Iext = tf.Variable(params["Iext"], dtype=tf.float64)

        self.N = params["N"]

        self.V = tf.zeros(self.N, dtype=tf.float64)
        self.dts = tf.constant(params["dts"], dtype=tf.float64)

        self.Isyn = tf.zeros_like(self.V)
        self.gsyn = tf.zeros_like(self.V)

        # self.ro = tf.zeros_like(self.V)
        # self.ro = tf.Variable(tf.tensor_scatter_nd_update(self.ro, [[0, ]], [1 / self.dts, ]))

        # self.ro[-1] = 1 / self.dts
        self.ro_H_integral = tf.Variable(0, dtype=tf.float64)

        self.ref_idx = tf.Variable(int(self.refactory / self.dts), dtype=tf.int32)
        self.ref_dvdt_idx = tf.Variable(int(self.ref_dvdt / self.dts), dtype=tf.int32)

        self.max_roH_idx = tf.Variable(0, dtype=tf.int32)

    def H_function(self, V, dVdt, tau_m, Vt, sigma):
        #T = (Vt - V) / sigma / SQRT_FROM_2
        delta_V = maximum((Vt - V), -1.0)
        #print(V[-1].numpy(), Vt, delta_V[-1].numpy())
        T = delta_V / sigma / SQRT_FROM_2
        A = exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
        dT_dt = -1.0 / sigma / SQRT_FROM_2 * dVdt
        dT_dt = minimum(dT_dt, 0.0)
        F_T = SQRT_FROM_2_PI * exp(-T**2) / (1.000000001 + erf(T))
        B = -SQRT_FROM_2 * dT_dt * F_T * tau_m
        H = (A + B) / tau_m
        H = maximum(H, 0.0)
        return H


    def limiter(self, a, b):
        w = tf.zeros_like(a)
        selected_indx1 = ((a * b) <= 0)
        selected_indx2 = (a < 0) & (a * b > 0)

        x1 = abs(a + b) * 0.5
        x2 = 2.0 * minimum(abs(a), abs(b))

        w = tf.where(selected_indx2, -minimum(x1, x2), w)


        selected_indx3 = logical_not(logical_and(selected_indx1, selected_indx2))
        w = tf.where(selected_indx3, minimum(x1, x2), w)

        return w

    def update_z(self, z, dts, Sourse):
        diff_z = z[1:] - z[:-1]
        a = diff_z[1:]
        b = diff_z[:-1]
        wi = self.limiter(a, b)
        a_ = b[1:]
        b_ = b[:-1]
        wi_1 = self.limiter(a_, b_)
        wi_1 = tf.concat([[0, ], wi_1], axis=0)

        dz_1 = -1 / dts * (diff_z[:-1] + 0.5*(1 - 0.1 / dts) * (wi - wi_1) ) - Sourse[1:-1] # Нужен dt !!!!!!!
        # dz_1 = -dt / dts * (diff_z[:-1] + dt / dts * (wi - wi_1)) - dt * S[1:-1]

        dz_0 = -1 / dts * z[0] - Sourse[0]

        dz_2 = 1 / dts * (z[-2] + 0.5 * (1 - 0.1 / dts) * wi[-1]) - Sourse[-1]
        # dz_2 = dt/dts * (z[-2] + dt/dts * wi[-1]) - dt * S[-1]

        dz_0 = tf.reshape(dz_0, [1, ])
        dz_2 = tf.reshape(dz_2, [1, ])

        dz_dt = tf.concat([dz_0, dz_1, dz_2], axis=0)
        return dz_dt


    def add_Isyn(self, Isyn, gsyn):
        self.Isyn += Isyn
        self.gsyn += gsyn

    def update(self, dt):
        return

    def getV(self):
        return self.V

class LIF_Neuron(BaseNeuron):
    def __init__(self, params):

        super(LIF_Neuron, self).__init__(params)

        #self.V = self.V + self.Vreset
        self.sigma = self.sigma / self.gl * sqrt(0.5 * self.gl / self.C)



    @tf.function
    def __call__(self, t, y):
        ro = y[:self.N]
        V = y[self.N:]

        dVdt = (self.gl * (self.El - V) + self.Iext + self.Isyn) / self.C #!!!!!![self.ref_dvdt_idx: ]
        tau_m = self.C / (self.gl + self.gsyn)

        #self.Isyn = tf.zeros_like(self.V)
        #self.gsyn = tf.zeros_like(self.V)
        #dVdt = tf.concat([tf.zeros(self.ref_dvdt_idx, dtype=tf.float64), dVdt], axis=0)

        H = self.H_function(V, dVdt, tau_m, self.Vt, self.sigma)
        sourse4Pts = ro * H
        firing = tf.math.reduce_sum(sourse4Pts)
        #print( firing )

        sourse4Pts = tf.tensor_scatter_nd_update(sourse4Pts, [[0], ], -tf.reshape(firing, [1, ]))

        dro_dt = self.update_z(ro, self.dts, sourse4Pts)
        dV_dt = self.update_z(V, self.dts, -dVdt)
        dV_dt = tf.tensor_scatter_nd_update(dV_dt, [[0], [tf.size(dV_dt) - 1]], [0, dVdt[-1]])

        dy_dt = tf.concat([dro_dt, dV_dt], axis=0)
        return dy_dt

##########################################
params_neurons = {
    "Vreset" : -90.0,
    "Vt" : -50.0,
    "gl" : 0.1,
    "El" : -60.0,
    "C"  : 1.0,
    "sigma" : 0.3,
    "ref_dvdt" : 3.0,
    "refactory" :  3.0, # refactory for threshold
    "w_in_distr" : 1.0,  # weight of neuron in model
    "Iext" : 1.1,

    "use_CBRD" : True,
    "N" : 400,
    "dts" : 0.5
}
Pop = LIF_Neuron(params_neurons)


V = tf.zeros(400, dtype=tf.float64) - 90
ro = tf.zeros(400, dtype=tf.float64)
ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[399, ]], [1 / 0.5, ]))
y0 = tf.concat([ro, V], axis=0)
# dydt = Pop.update(t, y)
# t = tf.Variable(0, dtype=tf.float64)
t = tf.range(0.0, 500.0, 0.1, dtype=tf.float64)

#solution = odeint(Pop.update, y0, t, method="euler")
# odeint_adjoint(func, y0, t, rtol=1e-6, atol=1e-12, method=None, options=None, adjoint_method=None, adjoint_rtol=None,
#                    adjoint_atol=None, adjoint_options=None)

with tf.GradientTape() as tape:
    tape.watch(Pop.Iext)
    sol = odeint_adjoint(Pop, y0, t, method="euler")

    grad = tape.gradient(sol[-1, 0], Pop.Iext)

print(grad)
solution = sol
fig, axes = plt.subplots(nrows=2)
t = t.numpy()
solution = solution.numpy()
#print(solution[:, -1])

firing = solution[:, 0]
Vm = solution[:, -1]
axes[0].plot(t, firing)
axes[1].plot(t, Vm)
plt.show()