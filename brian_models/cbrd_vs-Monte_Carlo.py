import sys
sys.path.extend(['/home/ivan/PycharmProjects/SNNoptimization'])
import numpy as np
import tensorflow as tf
from brian2 import *

defaultclock.dt = 0.1 * ms
import pickle
import net as MCnet
import h5py
from scipy.signal.windows import parzen
import cbrd_tfdiffeq as ctfeq
import channels as Chs


METHOD = 'heun'  # 'exponential_euler'
NNP = 2000
PCONN = 0.5
kdr_channel = {
    "channel_class" : ctfeq.BaseChannel,

    "gmax" : 23.0,
    "Erev" : -90.0,

    "degrees" : [4, ],
    "x_reset" : [0.45,],
}

ka_channel = {
    "channel_class" : Chs.KA_channel,

    "gmax" : 10.0,
    "Erev" : -90.0,

    "degrees" : [1, 1],
    "x_reset" : [0.31, -0.05],
}

##### block of neurons params #########
pvbas_params = {
    "name" : "pvbas",
    "neuron_class" : ctfeq.HH_Neuron,
    "Vreset": -40.0,
    "Vt": -55.0,
    "gl": 0.18,
    "El": -60.0,
    "C": 1.0, #
    "sigma": 0.3,
    "ref_dvdt": 2.5,   # AP duration
    "refactory": 15.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params"  : [kdr_channel, ka_channel],

    "target" : {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 24, #20.0,
        "phase": 1.5707963267948966,
    },
}
##### block of generators params #########
ca3pyr_params = {
    "name" : "ca3pyr",
    "R": 0.3,
    "freq": 7.0,
    "mean_spike_rate": 0.5, # 5,
    "phase": 1.58,
}

ca3pyr2pvbas = {
    "w": 0.5,
    "pre_name": "ca3pyr",
    "post_name": "pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 100*0.908653493,
    "Erev": 0.0,
}

params_net = {
    "params_neurons" : [pvbas_params, ],
    "params_generators" : [ca3pyr_params,],
    "params_synapses" : [ca3pyr2pvbas,]
}
############################################################################
#### run simulation ########################################################
delta_t = 0.1
duration = 200.0
t = tf.range(0.0, duration, delta_t, dtype=tf.float64)
cbrd_net = ctfeq.Network(params_net)
y0 = cbrd_net.get_y0()

solution = cbrd_net.run_simulation(t, y0)

hf = h5py.File('/home/ivan/Data/phase_relations/com.hdf5', 'w')
solution_dset = hf.create_dataset('solution', data=solution.numpy() )
hf.close()


#params_net["params_neurons"][0]["Iext"] = -0.5
mc_net, SpMtrs = MCnet.get_net_with_params_net(params_net)
mc_net.run(duration * ms, report='text')


mc_pop_freq, _ = np.histogram(SpMtrs[1].t/ms, bins = t.numpy(), range=[0, duration])
mc_pop_freq = mc_pop_freq / 2000 / delta_t


gsyn = ca3pyr2pvbas['gbarS'] * solution[:, 1]

fig, axes = plt.subplots(nrows=3, sharex=True)
axes[0].plot(t, gsyn, label="gsyn")

axes[1].plot(t, solution[:, 3], label="CBRD pop freq")
axes[1].plot(t[:-1], mc_pop_freq, label="Monte-Carlo pop freq")

axes[2].plot(t, solution[:, 802], label="CBRD Vm") # 1602

for ax in axes:
    ax.legend(loc='upper right')

plt.show()











