import numpy as np
import tensorflow as tf
import cbrd_tfdiffeq

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
argmax = tf.math.argmax

SQRT_FROM_2 = np.sqrt(2)
SQRT_FROM_2_PI = 0.7978845608028654
PI = np.pi

class Networkmcomps(cbrd_tfdiffeq.Network):
    def __init__(self, params, dt=0.1):
        super(cbrd_tfdiffeq.Network, self).__init__(name="Network", dtype=tf.float64)

        params_neurons = params["params_neurons"]

        self.synapses = []
        params_synapses = self._set_connections(params_neurons, params["params_generators"], params["params_synapses"])
        Syn = cbrd_tfdiffeq.PlasticSynapse(params_synapses, dt=dt)
        self.synapses.append(Syn)
        # for idx, param_synapse in enumerate(params_synapses):
        #     Syn = PlasticSynapse(param_synapse)
        #     Syn.start_idx = idx * 3 # 3 - число динамических переменных для синапса
        #     Syn.end_idx = Syn.start_idx + 3
        #     self.synapses.append(Syn)

        start_idx4_neurons = self.synapses[-1].end_idx
        self.neurons = []

        ro_0_indexes = []
        start_idx = start_idx4_neurons
        for idx, param_neuron in enumerate(params_neurons):
            Pop = param_neuron["neuron_class"](param_neuron, dt=dt)
            end_idx = Pop.set_indexes(start_idx)
            # start_idx = start_idx4_neurons + idx * Pop.n_dynamic_vars * Pop.N
            # Pop.start_idx = start_idx
            # Pop.end_idx = start_idx + Pop.n_dynamic_vars * Pop.N
            #if param_neuron["is_sim_rho"]:
            ro_0_indexes.append(start_idx)

            start_idx = end_idx
            self.neurons.append(Pop)

        self.ro_0_indexes = tf.convert_to_tensor(ro_0_indexes, dtype=tf.int32)

        self.generators = []
        generator = cbrd_tfdiffeq.VonMissesGenerators(params["params_generators"])

        self.generators.append(generator)

    def set_compartmets(self, ntwocomps, strength):
        for neuron_idx in range(0, ntwocomps//2, 2):
            self.neurons[neuron_idx].add_compartment(self.neurons[neuron_idx + 1], strength[neuron_idx])
            self.neurons[neuron_idx+1].add_compartment(self.neurons[neuron_idx], strength[neuron_idx+1])


    @tf.function(input_signature=[tf.TensorSpec(shape=(), dtype=tf.float64), tf.TensorSpec(shape=(None,), dtype=tf.float64)])
    def __call__(self, t, y):
        t = tf.cast(t, dtype=tf.float64)
        dy_dt = []
        neurons_firings = tf.reshape(tf.gather(y, self.ro_0_indexes), shape=(-1,))

        all_firings = [neurons_firings, ]
        for generator in self.generators:
            artifitial_firing = generator(t)
            # firings = tf.concat(firings, artifitial_firing, axis=0)
            all_firings.append(artifitial_firing)

        firings = tf.concat(all_firings, axis=0)

        for synapse in self.synapses:
            y4syn = y[synapse.start_idx:synapse.end_idx]
            SRpre = tf.reshape(tf.gather(firings, synapse.pre_indxes), shape=(-1,))
            dsyn_dt = synapse(t, y4syn, SRpre=SRpre)
            dy_dt.append(dsyn_dt)

        argmax_rho_H = -1
        for neuron_idx, neuron in enumerate(self.neurons):
            Vpost = y[neuron.V_start_idx:neuron.V_end_idx]

            gsyn_full = 0.0
            Isyn_full = 0.0
            for synapse in self.synapses:
                gsyn, Isyn = synapse.get_G_Isyn(y, Vpost, neuron_idx)
                gsyn_full = gsyn_full + gsyn
                Isyn_full = Isyn_full + Isyn

            if tf.size(Isyn_full) == 0:
                Isyn_full = tf.zeros(neuron.N, dtype=tf.float64)
                gsyn_full = tf.zeros(neuron.N, dtype=tf.float64)

            dneur_dt, argmax_rho_H_ = neuron(t, y, argmax_rho_H, gsyn=gsyn_full, Isyn=Isyn_full)  # for LIF y4neuron

            if argmax_rho_H_ !=  None:
                argmax_rho_H = argmax_rho_H_

            dy_dt.append(dneur_dt)

        dy_dt = tf.concat(dy_dt, axis=0)
        return dy_dt
