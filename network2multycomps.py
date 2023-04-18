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

    def set_compartmets(self):
        pass

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
