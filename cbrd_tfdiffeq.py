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


        self.El =  tf.constant(params["El"], dtype=tf.float64)
        self.C =  tf.constant(params["C"], dtype=tf.float64)
        self.sigma = tf.constant(params["sigma"], dtype=tf.float64)

        self.ref_dvdt = params["ref_dvdt"]   # refactory in updates of V and variables of states
        self.refactory = params["refactory"] # refactory for threshold

        self.Iext = tf.Variable(params["Iext"], dtype=tf.float64)
        self.input_index = None

        self.N = params["N"]
        self.start_idx = 0
        self.end_idx = 2 * self.N

        self.V = tf.zeros(self.N, dtype=tf.float64)
        self.gl = tf.zeros_like(self.V) + params["gl"]
        self.dts = tf.constant(params["dts"], dtype=tf.float64)


        self.ro_H_integral = tf.Variable(0, dtype=tf.float64)
        self.firing = tf.Variable(0, dtype=tf.float64)

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
        F_T = SQRT_FROM_2_PI * exp(- (T**2) ) / (1.00000001 + erf(T))
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

class LIF_Neuron(BaseNeuron):
    def __init__(self, params):

        super(LIF_Neuron, self).__init__(params)

        #self.V = self.V + self.Vreset
        self.sigma = self.sigma / self.gl * sqrt(0.5 * self.gl / self.C)



    @tf.function
    def __call__(self, t, y, gsyn=0.0, Erev=0.0):
        ro = y[:self.N]
        V = y[self.N:]

        #print(gsyn)
        #print(V)

        if tf.equal(tf.size(gsyn), 0):
            dVdt = (self.gl * (self.El - V) + self.Iext ) / self.C
            tau_m = self.C / self.gl
        else:
            Isyn = tf.reduce_sum( gsyn * (Erev - tf.reshape(V, shape=(1, -1))), axis=0 )
            dVdt = (self.gl * (self.El - V) + self.Iext + Isyn) / self.C #!!!!!![self.ref_dvdt_idx: ]
            tau_m = self.C / (self.gl + tf.reduce_sum(gsyn))

        tau_m = tf.reshape(tau_m, shape=(-1, ))
        dVdt = tf.reshape(dVdt, shape=(-1, ))

        H = self.H_function(V, dVdt, tau_m, self.Vt, self.sigma)
        #print(H[-1], V[-1], dVdt[-1], tau_m[-1], self.Vt, self.sigma[-1])


        sourse4Pts = ro * H
        firing = tf.math.reduce_sum(sourse4Pts)

        sourse4Pts = tf.tensor_scatter_nd_update(sourse4Pts, [[0], ], -tf.reshape(firing, [1, ]))


        dro_dt = self.update_z(ro, self.dts, sourse4Pts)
        dV_dt = self.update_z(V, self.dts, -dVdt)
        dV_dt = tf.tensor_scatter_nd_update(dV_dt, [[0], [tf.size(dV_dt) - 1]], [0, dVdt[-1]])
        dy_dt = tf.concat([dro_dt, dV_dt], axis=0)
        return dy_dt


class SimlestSinapse(tf.Module):
    def __init__(self, params):
        super(SimlestSinapse, self).__init__(name="Synapse")
        # self.w = tf.Variable(params["w"], dtype=tf.float64)
        # self.delay = params["delay"] # !!!!!!!!!
        # self.pre = params["pre"]
        # self.post = params["post"]
        self.start_idx = 0
        self.end_idx = 3
        # self.pre_hist = []
class PlasticSynapse(SimlestSinapse):
    def __init__(self, params):
        super(PlasticSynapse, self).__init__(params)

        tau_ds = []
        tau_rs = []
        tau_fs = []
        Uincs = []
        gbarSs = []
        Erevs = []
        Ws = []

        pre_indxes = []
        post_indxes = []
        for p in params:
            tau_ds.append(p["tau_d"])
            tau_rs.append(p["tau_r"])
            tau_fs.append(p["tau_f"])
            Uincs.append(p["Uinc"])
            gbarSs.append(p["gbarS"])
            Erevs.append(p["Erev"])
            Ws.append(p["w"])

            pre_indxes.append(p["pre"])
            post_indxes.append(p["post"])

        self.tau_d = tf.Variable(tau_ds, dtype=tf.float64)
        self.tau_r = tf.Variable(tau_rs, dtype=tf.float64)
        self.tau_f = tf.Variable(tau_fs, dtype=tf.float64)
        self.Uinc = tf.Variable(Uincs, dtype=tf.float64)

        self.gbarS = tf.Variable(gbarSs, dtype=tf.float64)
        self.Erev = tf.Variable(Erevs, dtype=tf.float64)
        self.W = tf.Variable(Ws, dtype=tf.float64)

        self.end_idx = 3 * len(params)


        self.pre_indxes = tf.convert_to_tensor(pre_indxes, dtype=tf.int32)
        self.post_indxes = tf.convert_to_tensor(post_indxes, dtype=tf.int32)

        self.tau1r = tf.where(self.tau_d != self.tau_r,  self.tau_d / (self.tau_d - self.tau_r), 1e-13)

        self.dt = 0.1 # !!!!!

    @tf.function
    def __call__(self, t, y, SRpre=0):

        X = y[0:2]
        Y = y[2:4]
        U = y[4:6]

        y_ = Y * exp(-self.dt / self.tau_d)

        x_ = 1 + (X - 1 + self.tau1r * Y) * exp(-self.dt / self.tau_r) - self.tau1r * Y

        u_ = U * exp(-self.dt / self.tau_f)
        u0 = u_ + self.Uinc * (1 - u_) * SRpre
        y0 = y_ + u0 * x_ * SRpre
        x0 = x_ - u0 * x_ * SRpre

        dXdt = (x0 - X) / self.dt
        dYdt = (y0 - Y) / self.dt
        dUdt = (u0 - U) / self.dt

        # print(SRpre.numpy())
        # print(Y.numpy(), dYdt.numpy())
        # print(X.numpy(), dXdt.numpy())
        # print(U.numpy(), dUdt.numpy())
        # print("#################################################")
        # rs = U * X * SRpre
        # dYdt = -Y / self.tau_d + rs
        # dXdt = 0.1 - (X - 1 + self.tau1r * Y) / self.tau_r - 0.1 * self.tau1r * Y - rs
        # dUdt = -U / self.tau_f + self.Uinc * (1 - U) * SRpre

        dy_dt = tf.concat([dXdt, dYdt, dUdt], axis=0)

        return dy_dt
##########################################
class Network(tf.keras.Model):

    def __init__(self, params):
        super(Network, self).__init__(name="Network")

        self.synapses = []
        params_synapses = params["params_synapses"]
        Syn = PlasticSynapse(params_synapses)
        self.synapses.append(Syn)
        # for idx, param_synapse in enumerate(params_synapses):
        #     Syn = PlasticSynapse(param_synapse)
        #     Syn.start_idx = idx * 3 # 3 - число динамических переменных для синапса
        #     Syn.end_idx = Syn.start_idx + 3
        #     self.synapses.append(Syn)

        start_idx4_neurons = 3 * len(params_synapses) # !!!!!!
        params_neurons = params["params_neurons"]
        self.neurons = []

        ro_0_indexes = []
        for idx, param_neuron in enumerate(params_neurons):
            Pop = LIF_Neuron(param_neuron)
            start_idx = start_idx4_neurons + idx * 2 * Pop.N
            Pop.start_idx = start_idx
            Pop.end_idx = start_idx + 2*Pop.N
            ro_0_indexes.append(start_idx)
            self.neurons.append(Pop)

        self.ro_0_indexes = tf.convert_to_tensor(ro_0_indexes, dtype=tf.int32)



    @tf.function
    def __call__(self, t, y):
        dy_dt = []

        firings = tf.reshape( tf.gather(y, self.ro_0_indexes), shape=(-1, ))
        for synapse in self.synapses:
            y4syn = y[synapse.start_idx:synapse.end_idx]
            #print(y4syn.numpy())
            SRpre = tf.reshape(tf.gather(firings, synapse.pre_indxes) , shape=(-1, ))

            dsyn_dt = synapse(t, y4syn, SRpre=SRpre)
            #dsyn_dt = tf.reshape(dsyn_dt, shape=(-1, ))
            dy_dt.append(dsyn_dt)

            #print("################################################")

        for neuron_idx, neuron in enumerate(self.neurons):
            y4neuron = y[ neuron.start_idx:neuron.end_idx ]

            #for synapse in self.synapses:  ### !!!!!!!!!!!
            synapse = self.synapses[0]

            Yofsyn = y[synapse.start_idx+2:synapse.start_idx+4] #  [1::3]
            gsyn_tmp = tf.where(synapse.post_indxes == neuron_idx, Yofsyn, 0.0)



            gsyn = synapse.W * synapse.gbarS * gsyn_tmp
            Erev = tf.reshape(synapse.Erev, shape=(-1, 1))
            gsyn = tf.reshape(gsyn, shape=(-1, 1))


            # print(SRpre[-1].numpy(), dVdt[-1].numpy(), tau_m[-1].numpy(), Vt.numpy(), sigma[-1].numpy())
            #print(y4neuron[0].numpy(), y4neuron[-1].numpy())

            dneur_dt = neuron(t, y4neuron, gsyn=gsyn, Erev=Erev)

            #print(dneur_dt[0].numpy(), dneur_dt[-1].numpy())
            #print("######################################")
            dy_dt.append( dneur_dt )

        dy_dt = tf.concat(dy_dt, axis=0)
        return dy_dt



##########################################
def main():


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
    synapse_params1 = {
        "w" : 1.6,
        "pre" : 0, # None,
        "post": 1, # None,
        "tau_f" : 12.0,  # ms
        "tau_r" : 1912.0, #  ms   # Synaptic depression rate
        "tau_d" : 2.8, #
        "Uinc"  : 0.153,
        "gbarS" : 1.0,
        "Erev": -75.0,
    }

    synapse_params2 = {
        "w" : 1.2,
        "pre" : 1, # None,
        "post": 0, # None,
        "tau_f" : 12.0,  # ms
        "tau_r" : 912.0, #  ms   # Synaptic depression rate
        "tau_d" : 2.8, #
        "Uinc"  : 0.153,
        "gbarS" : 1.0,
        "Erev": -75.0,
    }
    params_net = {
        "params_neurons" : [params_neurons, params_neurons],
        "params_synapses" : [synapse_params1, synapse_params2]
    }



    t = tf.range(0.0, 500.0, 0.1, dtype=tf.float64) #tf.Variable(0, dtype=tf.float64)
    V = tf.zeros(400, dtype=tf.float64) - 90
    ro = tf.zeros(400, dtype=tf.float64)
    ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[399, ]], [1 / 0.5, ]))
    # y0 = tf.concat([ro, V, ro, V], axis=0)
    #dydt = net(t, y0)
    y0syn = tf.Variable([1.0, 1.0, 0.0, 0.0, 0.0, 0.0], dtype=tf.float64)
    y0 = tf.concat([y0syn, ro, V, ro, V], axis=0)

    net = Network(params_net)

    #print( (t[:-1] - t[1:]  ))
    solution = odeint_adjoint(net, y0, t, method="euler" )
    # with tf.GradientTape() as tape:
    #     tape.watch(net.neurons[0].Iext)
    #     solution = odeint_adjoint(net, y0, t, method="euler")
    #     grad = tape.gradient(solution[-1, 0], net.neurons[0].Iext)
    #
    # print(grad)
    #np.savetxt("test.txt", solution.numpy(), fmt='%.2f', delimiter='\t')
    #print(solution.numpy())
    # Pop = LIF_Neuron(params_neurons)

    # V = tf.zeros(400, dtype=tf.float64) - 90
    # ro = tf.zeros(400, dtype=tf.float64)
    # ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[399, ]], [1 / 0.5, ]))
    # y0 = tf.concat([ro, V], axis=0)
    # # dydt = Pop.update(t, y)
    # # t = tf.Variable(0, dtype=tf.float64)
    # t = tf.range(0.0, 500.0, 0.1, dtype=tf.float64)
    #
    # #solution = odeint(Pop.update, y0, t, method="euler")
    # # odeint_adjoint(func, y0, t, rtol=1e-6, atol=1e-12, method=None, options=None, adjoint_method=None, adjoint_rtol=None,
    # #                    adjoint_atol=None, adjoint_options=None)
    #
    # with tf.GradientTape() as tape:
    #     tape.watch(Pop.Iext)
    #     #sol = odeint_adjoint(Pop, y0, t, method="euler")
    #     sol = odeint(Pop, y0, t, method="euler")
    #
    #     grad = tape.gradient(sol[-1, 0], Pop.Iext)
    #
    # print(grad)
    # solution = sol
    fig, axes = plt.subplots(nrows=4)
    # t = t.numpy()
    # solution = solution.numpy()
    # #print(solution[:, -1])

    firing1 = solution[:, 6]
    firing2 = solution[:, 806]
    gsyn1 =  solution[:, 2]
    gsyn2 =  solution[:, 3]
    # Vm = solution[:, -1]

    axes[0].plot(t, firing1)
    axes[1].plot(t, firing2)
    axes[2].plot(t, gsyn1)
    axes[3].plot(t, gsyn2)
    plt.show()


if __name__ == '__main__':
    main()