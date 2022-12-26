import numpy as np
import tensorflow as tf
from tfdiffeq import odeint
import cbrd_tfdiffeq as ctfeq
import channels as Chs
import matplotlib.pyplot as plt
import h5py


#Kdr_channelOLM

kdr_channel = {
    "channel_class" : ctfeq.BaseChannel,

    "gmax" : 0.0, # 23.0, # 40.0,
    "Erev" : -90.0,

    "degrees" : [4, ],
    "x_reset" : [0.65, ], #[0.45,],
}

ka_channel = {
    "channel_class" : Chs.KA_channel,

    "gmax" : 0.0, #10.0,
    "Erev" : -90.0,

    "degrees" : [1, 1],
    "x_reset" : [0.31, -0.05],
}

##################################################################
kdr_channelPyrChizhovGraham = {
    "channel_class" : Chs.Kdr_channelPyrChizhovGraham,

    "gmax" : 0.76, # 10.0,
    "Erev" : -90.0,

    "degrees" : [1, 1],
    "x_reset" : [0.26, 0.47],
}

pyr_params = {
    "name" : "pyr",
    "Vreset": -40.0,
    "Vt": -55.0, #-65.0,
    "gl": 0.025, # 0.18, # 0.1,
    "El": -61.22, #-60.0,
    "C": 0.7, #
    "sigma": 0.3,
    "ref_dvdt": 1.5,   # AP duration
    "refactory": 10.0,  # refactory for threshold
    "Iext": 1.5,
    "N": 400,
    "dts": 0.5,

    "channels_params"  : [kdr_channelPyrChizhovGraham, ], #[kdr_channel, ka_channel],

    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 1.5707963267948966,
    },
}




population = ctfeq.HH_Neuron(pyr_params, dt=0.1)
y0 = population.get_y0()

#print(y0)
t = tf.range(0.0, 100.0, 0.1, dtype=tf.float64)
# dydt = population(t[0], y0)
# print(dydt)

solution = odeint(population, y0, t, method="euler")
firing_cbrd = solution[:, 0]
Vm = solution[:, 799]
n = solution[:, 1199]
a = solution[:, 1599]
#b = solution[:, 1999]

with h5py.File("com.hdf5", "w") as file:
    file.create_dataset("Vm", data=Vm)
    file.create_dataset("SpikeRate", data=firing_cbrd)
    file.create_dataset("Solution", data=solution)


fig, axes = plt.subplots(nrows=5, sharex=True)
axes[0].plot(t, firing_cbrd, linewidth=1)
axes[0].set_title("Firing rate")
axes[1].plot(t, Vm, linewidth=4)
axes[2].plot(t, n, linewidth=4)

###firing_monte_carlo = get_monte_carlo()
axes[3].plot(t, a, linewidth=1)
#axes[4].plot(t, b, linewidth=1)
####axes.plot(t, firing_monte_carlo, linewidth=1)
# axes.set_ylim(0, None)
# axes.set_xlim(0, None)
plt.show()