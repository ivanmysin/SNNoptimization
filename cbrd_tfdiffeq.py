import numpy as np
import tensorflow as tf
from tfdiffeq import odeint, odeint_adjoint

import matplotlib.pyplot as plt

erf = tf.math.erf
bessel_i0 = tf.math.bessel_i0
sqrt = tf.math.sqrt
exp = tf.math.exp
cos = tf.math.cos
maximum = tf.math.maximum
minimum = tf.math.minimum
abs = tf.math.abs
logical_and = tf.math.logical_and
logical_not = tf.math.logical_not

SQRT_FROM_2 = np.sqrt(2)
SQRT_FROM_2_PI = 0.7978845608028654
PI = np.pi

class BaseNeuron(tf.keras.Model):

    def __init__(self, params, dt):
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


        self.gl = tf.constant(params["gl"], dtype=tf.float64)
        self.dts = tf.constant(params["dts"], dtype=tf.float64)


        self.ref_idx = tf.Variable(int(self.refactory / self.dts), dtype=tf.int32, trainable=False)
        self.ref_dvdt_idx = tf.Variable(int(self.ref_dvdt / self.dts), dtype=tf.int32, trainable=False)

        self.max_roH_idx = tf.Variable(0, dtype=tf.int32, trainable=False)
        self.dt = dt

    @tf.function
    def H_function(self, V, dVdt, tau_m, Vt, sigma):
        delta_V = maximum((Vt - V), -1.0)
        T = delta_V / sigma / SQRT_FROM_2
        A = exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
        dT_dt = -1.0 / sigma / SQRT_FROM_2 * dVdt
        dT_dt = minimum(dT_dt, 0.0)
        F_T = SQRT_FROM_2_PI * exp(- (T**2) ) / (1.00000001 + erf(T))
        B = -SQRT_FROM_2 * dT_dt * F_T * tau_m
        H = (A + B) / tau_m
        H = maximum(H, 0.0)
        return H

    @tf.function
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

    @tf.function
    def update_z(self, z, dts, Sourse):
        diff_z = z[1:] - z[:-1]
        a = diff_z[1:]
        b = diff_z[:-1]
        wi = self.limiter(a, b)
        a_ = b[1:]
        b_ = b[:-1]
        wi_1 = self.limiter(a_, b_)
        wi_1 = tf.concat([[0, ], wi_1], axis=0)

        dz_1 = -1 / dts * (diff_z[:-1] + 0.5*(1 - self.dt / dts) * (wi - wi_1) ) - Sourse[1:-1]
        # dz_1 = -dt / dts * (diff_z[:-1] + dt / dts * (wi - wi_1)) - dt * S[1:-1]

        dz_0 = -1 / dts * z[0] - Sourse[0]

        dz_2 = 1 / dts * (z[-2] + 0.5 * (1 - self.dt / dts) * wi[-1]) - Sourse[-1]
        # dz_2 = dt/dts * (z[-2] + dt/dts * wi[-1]) - dt * S[-1]

        dz_0 = tf.reshape(dz_0, [1, ])
        dz_2 = tf.reshape(dz_2, [1, ])

        dz_dt = tf.concat([dz_0, dz_1, dz_2], axis=0)
        return dz_dt

class LIF_Neuron(BaseNeuron):
    def __init__(self, params, dt=0.1):

        super(LIF_Neuron, self).__init__(params, dt)

        #self.V = self.V + self.Vreset
        self.sigma = self.sigma / self.gl * sqrt(0.5 * self.gl / self.C)

        self.ro_start_idx = 0
        self.ro_end_idx = self.N
        self.V_start_idx = self.ro_end_idx
        self.V_end_idx = self.V_start_idx + self.N


    @tf.function
    def __call__(self, t, y, gsyn=0.0, Isyn=0.0):
        ro = y[self.ro_start_idx : self.ro_end_idx]
        V = y[self.V_start_idx : self.V_end_idx]

        dVdt = (self.gl * (self.El - V) + self.Iext + Isyn) / self.C #!!!!!![self.ref_dvdt_idx: ]
        tau_m = self.C / (self.gl + tf.reduce_sum(gsyn))

        tau_m = tf.reshape(tau_m, shape=(-1, ))
        dVdt = tf.reshape(dVdt, shape=(-1, ))

        H = self.H_function(V, dVdt, tau_m, self.Vt, self.sigma)
        sourse4Pts = ro * H
        firing = tf.math.reduce_sum(sourse4Pts)
        sourse4Pts = tf.tensor_scatter_nd_update(sourse4Pts, [[0], ], -tf.reshape(firing, [1, ]))

        dro_dt = self.update_z(ro, self.dts, sourse4Pts)
        dV_dt = self.update_z(V, self.dts, -dVdt)
        dV_dt = tf.tensor_scatter_nd_update(dV_dt, [[0], [tf.size(dV_dt) - 1]], [0, dVdt[-1]])
        dy_dt = tf.concat([dro_dt, dV_dt], axis=0)
        return dy_dt


class SimlestSinapse(tf.Module):
    def __init__(self, params, dt):
        super(SimlestSinapse, self).__init__(name="Synapse")
        self.dt = dt
class PlasticSynapse(SimlestSinapse):
    def __init__(self, params, dt=0.1, start_idx=0):
        super(PlasticSynapse, self).__init__(params, dt)

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

        self.tau_d = tf.Variable(tau_ds, dtype=tf.float64, name='tau_d')
        self.tau_r = tf.Variable(tau_rs, dtype=tf.float64, name='tau_r')
        self.tau_f = tf.Variable(tau_fs, dtype=tf.float64, name='tau_f')
        self.Uinc = tf.Variable(Uincs, dtype=tf.float64, name='Uinc')
        self.tau1r = tf.where(self.tau_d != self.tau_r,  self.tau_d / (self.tau_d - self.tau_r), 1e-13)

        self.gbarS = tf.Variable(gbarSs, dtype=tf.float64, trainable=False)
        self.Erev = tf.Variable(Erevs, dtype=tf.float64, trainable=False)
        self.W = tf.Variable(Ws, dtype=tf.float64, name='Wplasticsyns')

        self.pre_indxes = tf.convert_to_tensor(pre_indxes, dtype=tf.int32)
        self.post_indxes = tf.convert_to_tensor(post_indxes, dtype=tf.int32)

        self.num_synapses = len(params)
        self.num_dynamic_vars = 3 # X, Y and U
        self.start_idx = start_idx
        self.end_idx = self.start_idx + self.num_dynamic_vars * self.num_synapses

        self.start_X_idx = 0
        self.end_X_idx = self.num_synapses

        self.start_R_idx = self.end_X_idx
        self.end_R_idx = self.start_R_idx + self.num_synapses

        self.start_U_idx = self.end_R_idx
        self.end_U_idx = self.start_U_idx + self.num_synapses

    def get_G_Isyn(self, y, Vpost, neuron_post_idx):
        Rofsyn = y[self.start_idx + self.start_R_idx:self.start_idx + self.end_R_idx]
        gsyn_tmp = tf.where(self.post_indxes == neuron_post_idx, Rofsyn, 0.0)

        gsyn = self.W * self.gbarS * gsyn_tmp
        Erev = tf.reshape(self.Erev, shape=(-1, 1))
        gsyn = tf.reshape(gsyn, shape=(-1, 1))
        Isyn = tf.reduce_sum(gsyn * (Erev - tf.reshape(Vpost, shape=(1, -1))), axis=0)
        return gsyn, Isyn



    @tf.function
    def __call__(self, t, y, SRpre=0):

        X = y[self.start_X_idx : self.end_X_idx]
        Y = y[self.start_R_idx : self.end_R_idx]
        U = y[self.start_U_idx : self.end_U_idx ]

        y_ = Y * exp(-self.dt / self.tau_d)

        x_ = 1 + (X - 1 + self.tau1r * Y) * exp(-self.dt / self.tau_r) - self.tau1r * Y

        u_ = U * exp(-self.dt / self.tau_f)
        u0 = u_ + self.Uinc * (1 - u_) * SRpre
        y0 = y_ + u0 * x_ * SRpre
        x0 = x_ - u0 * x_ * SRpre

        dXdt = (x0 - X) / self.dt
        dYdt = (y0 - Y) / self.dt
        dUdt = (u0 - U) / self.dt
        dy_dt = tf.concat([dXdt, dYdt, dUdt], axis=0)

        return dy_dt
##########################################
class VonMissesGenerators(tf.Module):

    def __init__(self, params, dt=0.1, start_idx=0):
        super(VonMissesGenerators, self).__init__()

        Rs = []
        omegas = []
        phases = []
        mean_spike_rates = []
        for p in params:
            Rs.append(p["R"])
            omegas.append( p["freq"] )
            phases.append( p["phase"] )
            mean_spike_rates.append(p["mean_spike_rate"] )

        self.omega = tf.constant(omegas, dtype=tf.float64)
        self.phase = tf.constant(phases, dtype=tf.float64)
        self.mean_spike_rate = tf.constant(mean_spike_rates, dtype=tf.float64)

        R = tf.constant(Rs, dtype=tf.float64)
        self.kappa = self.r2kappa(R)

        self.mult4time = tf.constant( 2 * PI * self.omega * 0.001, dtype=tf.float64)

        I0 = bessel_i0(self.kappa)
        self.normalizator = self.mean_spike_rate / I0 * dt * 0.001



    def r2kappa(self, R):
        """
        recalulate kappa from R for von Misses function
        """

        # if R < 0.53:
        #     kappa = 2 * R + R ** 3 + 5 / 6 * R ** 5
        #
        # elif R >= 0.53 and R < 0.85:
        #     kappa = -0.4 + 1.39 * R + 0.43 / (1 - R)
        #
        # elif R >= 0.85:
        #     kappa = 1 / (3 * R - 4 * R ** 2 + R ** 3)
        kappa = tf.where(R < 0.53,  2 * R + R ** 3 + 5 / 6 * R ** 5, 0.0)
        kappa = tf.where(logical_and(R >= 0.53, R < 0.85),  -0.4 + 1.39 * R + 0.43 / (1 - R), kappa)
        kappa = tf.where(R >= 0.85,  1 / (3 * R - 4 * R ** 2 + R ** 3), kappa)
        return kappa

    def __call__(self, t):
        firings = self.normalizator * exp(self.kappa * cos(self.mult4time * t + self.phase) )
        return firings


class Network(tf.keras.Model):

    def __init__(self, params, dt=0.1):
        super(Network, self).__init__(name="Network", dtype=tf.float64)


        self.synapses = []
        params_synapses = params["params_synapses"]
        Syn = PlasticSynapse(params_synapses, dt=dt)
        self.synapses.append(Syn)
        # for idx, param_synapse in enumerate(params_synapses):
        #     Syn = PlasticSynapse(param_synapse)
        #     Syn.start_idx = idx * 3 # 3 - число динамических переменных для синапса
        #     Syn.end_idx = Syn.start_idx + 3
        #     self.synapses.append(Syn)

        start_idx4_neurons = self.synapses[-1].end_idx
        params_neurons = params["params_neurons"]
        self.neurons = []

        ro_0_indexes = []
        for idx, param_neuron in enumerate(params_neurons):
            Pop = LIF_Neuron(param_neuron, dt=dt)
            start_idx = start_idx4_neurons + idx * 2 * Pop.N
            Pop.start_idx = start_idx
            Pop.end_idx = start_idx + 2*Pop.N
            ro_0_indexes.append(start_idx)
            self.neurons.append(Pop)

        self.ro_0_indexes = tf.convert_to_tensor(ro_0_indexes, dtype=tf.int32)

        self.generators = []
        generator = VonMissesGenerators(params["params_generators"])

        self.generators.append(generator)



    @tf.function(
    input_signature=[tf.TensorSpec(shape=(), dtype=tf.float64), tf.TensorSpec(shape=(None, ), dtype=tf.float64)])
    def __call__(self, t, y):
        t = tf.cast(t, dtype=tf.float64)
        dy_dt = []
        neurons_firings = tf.reshape( tf.gather(y, self.ro_0_indexes), shape=(-1, ))

        all_firings = [neurons_firings, ]
        for generator in self.generators:
            artifitial_firing = generator(t)
            #firings = tf.concat(firings, artifitial_firing, axis=0)
            all_firings.append(artifitial_firing)

        firings = tf.concat(all_firings, axis=0)

        for synapse in self.synapses:
            y4syn = y[synapse.start_idx:synapse.end_idx]
            SRpre = tf.reshape(tf.gather(firings, synapse.pre_indxes) , shape=(-1, ))
            dsyn_dt = synapse(t, y4syn, SRpre=SRpre)
            dy_dt.append(dsyn_dt)

        for neuron_idx, neuron in enumerate(self.neurons):
            y4neuron = y[ neuron.start_idx:neuron.end_idx ]
            Vpost = y4neuron[neuron.V_start_idx:neuron.V_end_idx]

            gsyn_full = 0.0
            Isyn_full = 0.0
            for synapse in self.synapses:
                gsyn, Isyn = synapse.get_G_Isyn(y, Vpost, neuron_idx)
                gsyn_full = gsyn_full + gsyn
                Isyn_full = Isyn_full + Isyn


            dneur_dt = neuron(t, y4neuron, gsyn=gsyn_full, Isyn=Isyn_full)

            dy_dt.append( dneur_dt )

        dy_dt = tf.concat(dy_dt, axis=0)
        return dy_dt



##########################################
def main():


    params_neurons1 = {
        "Vreset" : -90.0,
        "Vt" : -50.0,
        "gl" : 0.1,
        "El" : -60.0,
        "C"  : 1.0,
        "sigma" : 0.3,
        "ref_dvdt" : 3.0,
        "refactory" :  3.0, # refactory for threshold
        "w_in_distr" : 1.0,  # weight of neuron in model
        "Iext" : 0.1,

        "use_CBRD" : True,
        "N" : 400,
        "dts" : 0.5
    }

    params_neurons2 = {
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

    synapse_params3 = {
        "w" : 10.0,
        "pre" : 2, # None,
        "post": 0, # None,
        "tau_f" : 12.0,  # ms
        "tau_r" : 912.0, #  ms   # Synaptic depression rate
        "tau_d" : 2.8, #
        "Uinc"  : 0.153,
        "gbarS" : 1.0,
        "Erev": 0.0,
    }

    generator1 = {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 18,
        "phase": 0,
    }


    params_net = {
        "params_neurons" : [params_neurons1, params_neurons2],
        "params_synapses" : [synapse_params1, synapse_params2, synapse_params3],
        "params_generators" : [generator1, ],
    }



    t = tf.range(0.0, 500.0, 0.1, dtype=tf.float64) #tf.Variable(0, dtype=tf.float64)
    V = tf.zeros(400, dtype=tf.float64) - 90
    ro = tf.zeros(400, dtype=tf.float64)
    ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[399, ]], [1 / 0.5, ]))
    # y0 = tf.concat([ro, V, ro, V], axis=0)
    #dydt = net(t, y0)
    y0syn = tf.Variable([1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=tf.float64)
    y0 = tf.cast( tf.concat([y0syn, ro, V, ro, V], axis=0), dtype=tf.float64)

    net = Network(params_net)

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

    # with tf.GradientTape() as tape:
    #     tape.watch(Pop.Iext)
    #     #sol = odeint_adjoint(Pop, y0, t, method="euler")
    #     sol = odeint(Pop, y0, t, method="euler")
    #
    #     grad = tape.gradient(sol[-1, 0], Pop.Iext)
    #
    # print(grad)
    # solution = sol
    fig, axes = plt.subplots(nrows=4, sharex=True)
    # t = t.numpy()
    # solution = solution.numpy()
    # #print(solution[:, -1])

    firing1 = solution[:, 9]
    firing2 = solution[:, 809]
    gsyn1 = solution[:, 3]
    gsyn2 = solution[:, 4]
    gsyn3 = solution[:, 5]
    # Vm = solution[:, -1]

    axes[0].plot(t, firing1)
    axes[1].plot(t, firing2)
    axes[2].plot(t, gsyn1)
    axes[2].plot(t, gsyn3)
    axes[3].plot(t, gsyn2)
    plt.show()


if __name__ == '__main__':
    main()