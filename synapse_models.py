import numpy as np
import tensorflow as tf
import cbrd_tfdiffeq

exp = tf.math.exp

class TwoExpSynapse(cbrd_tfdiffeq.SimlestSinapse):

    def __init__(self, params, dt, start_idx=0):
        super(cbrd_tfdiffeq.SimlestSinapse, self).__init__(name="TwoExpSynapse")
        self.dt = dt
        tau_rises = []
        tau_decays = []
        gbarSs = []
        Erevs = []
        pconns = []

        pre_indxes = []
        post_indxes = []
        for p in params:
            tau_rises.append(p["tau_rise"])
            tau_decays.append(p["tau_decay"])
            gbarSs.append(p["gbarS"])
            Erevs.append(p["Erev"])
            pconns.append(p["pconn"])

            pre_indxes.append(p["pre"])
            post_indxes.append(p["post"])

        self.tau_rise = tf.Variable(tau_rises, dtype=tf.float64, name='tau_rise', trainable=True)
        self.tau_decay = tf.Variable(tau_decays, dtype=tf.float64, name='tau_decay', trainable=True)

        self.gbarS = tf.Variable(gbarSs, dtype=tf.float64, name='SynapticConductance', trainable=True)
        self.Erev = tf.Variable(Erevs, dtype=tf.float64, name='Erev', trainable=False)
        self.Erev = tf.reshape(self.Erev, shape=(-1, 1))

        self.pconn = tf.Variable(pconns, dtype=tf.float64, name='pconns', trainable=True)

        self.pre_indxes = tf.convert_to_tensor(pre_indxes, dtype=tf.int32)
        self.post_indxes = tf.convert_to_tensor(post_indxes, dtype=tf.int32)

        self.num_synapses = len(params)
        self.num_dynamic_vars = 2  # g and dgdt
        self.start_idx = start_idx
        self.end_idx = self.start_idx + self.num_dynamic_vars * self.num_synapses


        self.start_g_idx = 0
        self.end_g_idx = self.num_synapses

        self.start_dgdt_idx = self.end_g_idx
        self.end_dgdt_idx = self.start_dgdt_idx + self.num_synapses

    def get_G_Isyn(self, y, Vpost, neuron_post_idx):
        gsyns = y[self.start_idx + self.start_g_idx:self.start_idx + self.end_g_idx]
        gsyn_tmp = tf.where(self.post_indxes == neuron_post_idx, gsyns, 0.0)

        gsyn = self.gbarS * gsyn_tmp
        gsyn = tf.reshape(gsyn, shape=(-1, 1))
        if tf.math.equal(tf.size(gsyn), 0):
            return tf.zeros_like(Vpost), tf.zeros_like(Vpost)
        else:
            Vdiff = self.Erev - tf.reshape(Vpost, shape=(1, -1))
            Itmp = gsyn * Vdiff
            Isyn = tf.reduce_sum(Itmp, axis=0)

        return gsyn, Isyn

    @tf.function
    def __call__(self, t, y, SRpre=0):
        Spre_normed = SRpre * self.pconn
        g = y[ self.start_g_idx : self.end_g_idx]
        dgdt = y[ self.start_dgdt_idx : self.end_dgdt_idx]
        d2gdt2 = (Spre_normed - g - (self.tau_rise+self.tau_decay)*dgdt ) / (self.tau_rise*self.tau_decay)
        dy_dt =  tf.concat([dgdt, d2gdt2], axis=0)
        return dy_dt

    def get_y0(self):
        gsyn0 = tf.zeros(self.num_dynamic_vars*self.num_synapses, dtype=tf.float64)
        return gsyn0