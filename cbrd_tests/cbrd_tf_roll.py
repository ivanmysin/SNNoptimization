# import matplotlib
# matplotlib.use("Qt5Agg")
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# from scipy.special import erf
# from tensorflow.math import erf, sqrt, exp, maximum, minimum, abs

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


class BaseNeuron:

    def __init__(self, params):

        self.Vreset = tf.constant(params["Vreset"], shape=[1, ], dtype=tf.float32)
        self.Vt = tf.constant(params["Vt"], dtype=tf.float32)

        self.gl =  tf.constant(params["gl"], dtype=tf.float32)
        self.El =  tf.constant(params["El"], dtype=tf.float32)
        self.C =  tf.constant(params["C"], dtype=tf.float32)
        self.sigma = tf.constant(params["C"], dtype=tf.float32)

        self.ref_dvdt = params["ref_dvdt"]   # refactory in updates of V and variables of states
        self.refactory = params["refactory"] # refactory for threshold


        self.Iext = tf.Variable(params["Iext"], dtype=tf.float32)

        self.N = params["N"]

        self.V = tf.zeros(self.N, dtype=tf.float32)
        self.dts = tf.constant(params["dts"], dtype=tf.float32)

        self.Isyn = tf.zeros_like(self.V)
        self.gsyn = tf.zeros_like(self.V)
        # self.t_states = np.linspace(0, self.N * self.dts, self.N)
        self.ro = tf.zeros_like(self.V)
        self.ro = tf.Variable(tf.tensor_scatter_nd_update(self.ro, [[0, ]], [1 / self.dts, ]))

        # self.ro[-1] = 1 / self.dts
        self.ro_H_integral = tf.Variable(0, dtype=tf.float32)
        self.ts =  tf.Variable(0, dtype=tf.float32)

        self.ref_idx = tf.Variable(int(self.refactory / self.dts), dtype=tf.int32)
        self.ref_dvdt_idx = tf.Variable(int(self.ref_dvdt / self.dts), dtype=tf.int32)

        self.max_roH_idx = tf.Variable(0, dtype=tf.int32)


        self.firing = tf.Variable([0, ], shape=[1, ], dtype=tf.float32)


        #self.CVhist = [0]
        #self.saveCV = True



    def H_function(self, V, dVdt, tau_m, Vt, sigma):
        T = (Vt - V) / sigma / SQRT_FROM_2
        A = np.exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
        dT_dt = -1.0 / sigma / SQRT_FROM_2 * dVdt
        dT_dt = minimum(0.0, dT_dt)
        F_T = SQRT_FROM_2_PI * np.exp(-T**2) / (1.000000001 + erf(T))
        B = -SQRT_FROM_2 * dT_dt * F_T * tau_m
        H = (A + B) / tau_m
        return H


    def update_ro(self, dt, dVdt, tau_m):
        shift = False
        if self.ts >= self.dts:
            last_ro = self.ro[-1] + self.ro[-2]
            ro_without_last = self.ro[:-1]
            ro_without_last = tf.roll(ro_without_last, 1, axis=0)

            self.ro_H_integral = tf.reshape(self.ro_H_integral, [1, ])
            last_ro = tf.reshape(last_ro, [1, ])
            self.ro = tf.concat([self.ro_H_integral, ro_without_last[1:], last_ro], axis=0)
            self.ro_H_integral = 0 * self.ro_H_integral
            self.ts = 0 * self.ts
            shift = True


        H = self.H_function(self.V[self.ref_idx:], dVdt[self.ref_idx:], tau_m[self.ref_idx:], self.Vt, self.sigma)


        # print(self.V[-1].numpy(), H[-1].numpy())

        # H[:self.ref_idx] = 0
        dro = self.ro[self.ref_idx:] * (1 - exp(-H * dt))  # dt * self.ro[self.ref_idx:] * H  #

        #self.Val = dro[-1]

        dro = tf.concat([tf.zeros(self.ref_idx, dtype=tf.float32), dro], axis=0)


        self.max_roH_idx = tf.math.argmax(dro)


        # self.ro[self.ro < 0] = 0
        fired = tf.math.reduce_sum(dro) #tf.math.reduce_sum(H * self.ro[self.ref_idx:])

        self.firing = tf.concat( [self.firing, tf.reshape(fired, [1, ])], axis=0)
        #print(self.firing)
        self.ro_H_integral = self.ro_H_integral + fired

        self.ro = self.ro - dro
        self.ts = self.ts + dt

        return shift


    def add_Isyn(self, Isyn, gsyn):
        self.Isyn += Isyn
        self.gsyn += gsyn

    def update(self, dt):
        return 0, 0, 0, 0


    def get_flow(self):
        return self.firing[-1]

    def get_flow_hist(self):
        return np.asarray(self.firing)

    def get_CV(self):
        return np.asarray(self.CVhist)

    def getV(self):
        return self.V

##################################################################

class LIF_Neuron(BaseNeuron):
    artifitial_generator = False

    def __init__(self, params):

        super(LIF_Neuron, self).__init__(params)

        self.V = self.V + self.Vreset

        #self.Vhist = [self.V[-1]]

        #self.times = [0]

        #if self.is_use_CBRD:
        self.sigma = self.sigma / self.gl * np.sqrt(0.5 * self.gl / self.C)




    def update(self, dt, duration):
        t = 0
        while (t < duration):
            # dVdt = -self.V / self.tau_m + self.Iext / self.tau_m + self.Isyn
            dVdt = (self.gl * (self.El - self.V) + self.Iext + self.Isyn) / self.C

            tau_m = self.C / (self.gl + self.gsyn)

            #dVdt[:self.ref_dvdt_idx ] = 0
            self.V = self.V + dt * dVdt


            #self.Vhist.append(self.V[-1])

            self.Isyn = tf.zeros_like(self.V)
            self.gsyn = tf.zeros_like(self.V)


            shift = self.update_ro(dt, dVdt, tau_m)



            #self.firing.append(1000 * self.ro[0])

            if shift:
                V_last = tf.reshape(self.V[-1], [1, ])
                V_without_last = self.V[:-1]
                V_without_last = tf.roll(V_without_last, 1, axis=0)

                # self.V[:-1] = np.roll(self.V[:-1], 1)
                # self.V[0] = self.Vreset

                self.V = tf.concat([self.Vreset, V_without_last[1:], V_last], axis=0)



            t = t + dt

        # if self.is_use_CBRD:
        #     return self.t_states, self.w_in_distr * self.ro, self.times, self.w_in_distr * np.asarray(
        #         self.firing),[]  # , self.t_states, self.V
        # else:
        #     return np.zeros(400), np.zeros(400), self.times, self.w_in_distr * np.asarray(self.firing), []


###################################################################################
params = {
    "Vreset" : -80.0,
    "Vt" : -50.0,
    "gl" : 0.01,
    "El" : -70.0,
    "C"  : 0.2,
    "sigma" : 0.3,
    "ref_dvdt" : 0,
    "refactory" :  3.0, # refactory for threshold
    "w_in_distr" : 1.0,  # weight of neuron in model
    "Iext" : 0.3,

    "use_CBRD" : True,
    "N" : 400,
    "dts" : 0.5
}

neuron_pops = LIF_Neuron(params)

with tf.GradientTape() as tape:
    tape.watch(neuron_pops.Iext)
    neuron_pops.update(0.1, 500)
    grad = tape.gradient(neuron_pops.firing[-1], neuron_pops.Iext)

    print(grad)
# firing = neuron_pops.get_flow_hist()
# print(firing.shape)
#
# times = np.linspace(0, 0.1, firing.size)
# import matplotlib.pyplot as plt
# plt.scatter(times, firing)
# plt.show()




