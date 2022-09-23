# import matplotlib
# matplotlib.use("Qt5Agg")
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import copy

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
        return


    def get_flow(self):
        return self.firing[-1]

    def get_flow_hist(self):
        return self.firing

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

            dVdt = (self.gl * (self.El - self.V[self.ref_dvdt_idx: ]) + self.Iext + self.Isyn) / self.C

            tau_m = self.C / (self.gl + self.gsyn)

            #dVdt[:self.ref_dvdt_idx ] = 0
            tf.concat([tf.zeros(self.ref_dvdt_idx, dtype=tf.float32), dVdt], axis=0)
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
                self.V = tf.concat([self.Vreset, V_without_last[1:], V_last], axis=0)
            t = t + dt
###################################################################################
class Channel:
    def __init__(self, gmax, E, V, x=None, y=None, x_reset=None, y_reset=None, x_deg=0, y_deg=0):
        self.gmax = tf.constant(gmax, dtype=tf.float32)
        self.E =  tf.constant(E, dtype=tf.float32)
        self.g = tf.Variable(0, dtype=tf.float32)
        self.x_deg = tf.constant(x_deg, dtype=tf.float32)
        self.y_deg = tf.constant(y_deg, dtype=tf.float32)

        if not x is None:
            self.x = self.get_x_inf(V)
            self.x_reset =  tf.constant([x_reset, ], shape=(1, ), dtype=tf.float32)
        else:
            self.x = None

        if not y is None:
            self.y = self.get_y_inf(V)
            self.y_reset =  tf.constant([y_reset, ], shape=(1, ), dtype=tf.float32)
        else:
            self.y = None

    def update(self, dt, V):
        self.g = self.gmax

        if not (self.x is None):
            x_inf = self.get_x_inf(V)
            tau_x = self.get_tau_x(V)
            self.x = x_inf - (x_inf - self.x) * exp(-dt / tau_x)
            self.g = self.g * (self.x**self.x_deg)

        if not (self.y is None):
            y_inf = self.get_y_inf(V)
            tau_y = self.get_tau_y(V)
            self.y = y_inf - (y_inf - self.y) * exp(-dt / tau_y)
            self.g = self.g * (self.y**self.y_deg)


    def get_I(self, V):
        I = self.g * (V - self.E)
        return I

    def get_g(self):
        return self.g

    def reset(self):
        if not (self.x is None):
            self.x = tf.tensor_scatter_nd_update(self.x, [[0], ], self.x_reset)

        if not (self.y is None):
            self.y = tf.tensor_scatter_nd_update(self.y, [[0], ], self.y_reset)


    def get_x_inf(self, V):
        return 0

    def get_y_inf(self, V):
        return 0

    def get_tau_x(self, V):
        return 0

    def get_tau_y(self, V):
        return 0

    def roll(self, max_roH_idx):
        if not (self.x is None):
            tmpx = self.x[max_roH_idx]
            last_x = self.x[-1]
            rolled_x = tf.roll(self.x[:-1], 1)

            tmpx = tf.reshape(tmpx, [1, ])
            last_x = tf.reshape(last_x, [1, ])
            self.x = tf.concat([tmpx, rolled_x, last_x], axis=0)

        if not (self.y is None):
            # tmpy = self.y[max_roH_idx]
            # self.y[:-1] = np.roll(self.y[:-1], 1)
            # self.y[0] = tmpy
            tmpy = self.x[max_roH_idx]
            last_y = self.y[-1]
            rolled_y = tf.roll(self.y[:-1], 1)

            tmpy = tf.reshape(tmpy, [1, ])
            last_y = tf.reshape(last_y, [1, ])
            self.y = tf.concat([tmpy, rolled_y, last_y], axis=0)

###################################################################################
class SimlestSinapse:
    def __init__(self, params):
        self.w = tf.Variable(params["w"], dtype=tf.float32)
        # self.delay = params["delay"] # !!!!!!!!!
        self.pre = params["pre"]
        self.post = params["post"]
        # self.pre_hist = []

    def update(self, dt):
        pre_flow = self.pre.get_flow()
        Isyn = self.w * pre_flow

        self.post.add_Isyn(Isyn, 0)

        return


class Synapse(SimlestSinapse):
    def __init__(self, params):
        super(Synapse, self).__init__(params)

        self.tau_s = tf.Variable(params["tau_s"], dtype=tf.float32)  # 5.4
        self.tau = tf.Variable(params["tau_a"], dtype=tf.float32)  # 1
        self.gbarS = tf.Variable(params["gbarS"], dtype=tf.float32)  # 1.0
        self.Erev = tf.Variable(params["Erev"], dtype=tf.float32)  # 50

        self.S = tf.Variable(0, dtype=tf.float32)
        self.dsdt = tf.Variable(0, dtype=tf.float32)
        self.tau_s_2 = self.tau_s ** 2

    def update(self, dt):
        pre_flow = self.pre.get_flow()

        self.dsdt = self.dsdt + dt * (
                    self.tau * self.gbarS * pre_flow / self.tau_s_2 - self.S / self.tau_s_2 - 2 * self.dsdt / self.tau_s)
        self.S = self.S + dt * self.dsdt

        gsyn = self.S * self.gbarS * self.w
        Isyn = gsyn * (self.post.getV() - self.Erev)

        self.post.add_Isyn(-Isyn, gsyn)

        return

class PlasticSynapse(SimlestSinapse):
    def __init__(self, params):
        super(PlasticSynapse, self).__init__(params)

        self.tau_d = tf.Variable(params["tau_d"], dtype=tf.float32)
        self.tau_r = tf.Variable(params["tau_r"], dtype=tf.float32)
        self.tau_f = tf.Variable(params["tau_f"], dtype=tf.float32)
        self.Uinc = tf.Variable(params["Uinc"], dtype=tf.float32)

        self.gbarS = tf.Variable(params["gbarS"], dtype=tf.float32)
        self.Erev = tf.Variable(params["Erev"], dtype=tf.float32)

        #tau_d, tau_r, tau_f, u, u0, x0, y0

        self.S = tf.Variable(0, dtype=tf.float32)
        self.x = tf.Variable(1.0, dtype=tf.float32)
        self.y = tf.Variable(0.0, dtype=tf.float32)
        self.u = tf.Variable(0.0, dtype=tf.float32)

        if self.tau_d != self.tau_r:
            self.tau1r = self.tau_d / (self.tau_d - self.tau_r)
        else:
            self.tau1r = 1e-13

    def update(self, dt):
        SRpre = self.pre.get_flow()

        y_ = self.y * exp(-dt / self.tau_d)
        x_ = 1 + (self.x - 1 + self.tau1r * self.y) * exp(-dt / self.tau_r) - self.tau1r * y_
        u_ = self.u * exp(-dt / self.tau_f)
        self.u = u_ + self.Uinc * (1 - u_) * SRpre
        self.y = y_ + self.u * x_ * SRpre
        self.x = x_ - self.u * x_ * SRpre
        gsyn = self.gbarS * self.w * self.y
        Isyn = gsyn * (self.post.getV() - self.Erev)
        self.post.add_Isyn(-Isyn, gsyn)

        return


################################################################################3
class Network:
    def __init__(self, neurons, synapses):
        self.neurons = neurons
        self.synapses = synapses

    def update(self, dt, duration):
        t = 0

        while(t < duration):
            for idx, neuron in enumerate(self.neurons):
                neuron.update(dt, dt)

            for synapse in self.synapses:
                synapse.update(dt)

            #print(self.synapses[0].y.numpy())
            t += dt
        return

###################################################################################
params_neurons = {
    "Vreset" : -80.0,
    "Vt" : -50.0,
    "gl" : 0.1,
    "El" : -70.0,
    "C"  : 1.0,
    "sigma" : 0.3,
    "ref_dvdt" : 0,
    "refactory" :  3.0, # refactory for threshold
    "w_in_distr" : 1.0,  # weight of neuron in model
    "Iext" : 1.8,

    "use_CBRD" : True,
    "N" : 400,
    "dts" : 0.5
}

# synapse_params = {
#     "w" : 1.0,
#     "pre" : None,
#     "post": None,
#     "tau_s" : 5.4,
#     "tau_a" : 1.0,
#     "gbarS" : 1.0,
#     "Erev": -75.0,
# }

synapse_params = {
    "w" : 1.0,
    "pre" : None,
    "post": None,
    "tau_f" : 12.0,  # ms
    "tau_r" : 750.0, # 1912.0, #  ms   # Synaptic depression rate
    "tau_d" : 2.8, #
    "Uinc"  : 0.6, # 0.153,
    "gbarS" : 1.0,
    "Erev": -75.0,
}

neuron_pops_1 = LIF_Neuron(params_neurons)
params_neurons["Iext"] = 1.7
neuron_pops_2 = LIF_Neuron(params_neurons)

synapse_params_1 = copy.deepcopy(synapse_params)
synapse_params_1["pre"] = neuron_pops_1
synapse_params_1["post"] = neuron_pops_2
synapse_params_1["w"] = 2.5
synapse1 = PlasticSynapse(synapse_params_1)

synapse_params_2 = copy.deepcopy(synapse_params)
synapse_params_2["pre"] = neuron_pops_2
synapse_params_2["post"] = neuron_pops_1
synapse_params_2["w"] = 2.5
synapse2 = PlasticSynapse(synapse_params_2)

net = Network([neuron_pops_1, neuron_pops_2], [synapse1, synapse2])


#net.update(0.1, 1000)
with tf.GradientTape() as tape:
    tape.watch(synapse1.Uinc)
    net.update(0.1, 500)
    grad = tape.gradient(neuron_pops_1.firing[-1], synapse1.Uinc)
    print(grad)

firing1 = neuron_pops_1.get_flow_hist().numpy()
firing2 = neuron_pops_2.get_flow_hist().numpy()

print(firing1[-1])
print(firing2[-1])
# print(firing2)

times = np.linspace(0, firing1.size*0.1, firing1.size)
print(times[-1])
import matplotlib.pyplot as plt
plt.scatter(times, firing1, color="red", label="Pop1")
plt.scatter(times, firing2, color="green", label="Pop2")
plt.legend()
plt.show()




