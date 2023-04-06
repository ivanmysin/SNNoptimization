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

    "gmax" : 23.0, # 40.0,
    "Erev" : -90.0,

    "degrees" : [4, ],
    "x_reset" : [0.45,], # [0.65, ], #
}

kdr_channel4olm = {
    "channel_class" : Chs.Kdr_channelOLM,
    "gmax": 36.0,
    "Erev": -77.0,

    "degrees": [4, ],
    "x_reset": [0.8, ],

}

ka_channel = {
    "channel_class" : Chs.KA_channel,

    "gmax" : 10.0,
    "Erev" : -90.0,

    "degrees" : [1, 1],
    "x_reset" : [0.31, -0.05],
}

na_persis_channel = {
    "channel_class" : Chs.PersistentPotassiumChannel,

    "gmax" : 2.5,
    "Erev" : 50.0,

    "degrees" : [1, ],
    "x_reset" : [0.95, ],
}

h_channel4OLM = {
    "channel_class" : Chs.H_Channel4OLM,

    "gmax" : 1.5,
    "Erev" : -20.0,

    "degrees" : [1, 1],
    "x_reset" : [-0.015, -0.01],
}

##################################################################
kdr_channelPyrChizhovGraham = {
    "channel_class" : Chs.Kdr_channelPyrChizhovGraham,

    "gmax" : 0.76, # 10.0,
    "Erev" : -90.0,

    "degrees" : [1, 1],
    "x_reset" : [0.26, 0.47],
}
######################################################################################################
olm_params = {
    "name" : "olm",
    "Vreset": -40.0,
    "Vt": -55.0, #-65.0, -60.0, #
    "gl": 0.3, # 0.18, #0.1, #, # 0.025, #
    "El": -54.4, #-61.22, #
    "C": 1.0, #
    "sigma": 0.3,
    "ref_dvdt": 2.0,   # AP duration
    "refactory": 15.0,  # refactory for threshold
    "Iext": -0.5,
    "N": 400,
    "dts": 0.5,

    "channels_params"  : [kdr_channel4olm, na_persis_channel, h_channel4OLM],

    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 1.5707963267948966,
    },
}

ngf_params = {
    "name" : "ngf",
    "Vreset": -40.0,
    "Vt": -55.0, #-65.0, -60.0, #
    "gl": 0.18,
    "El": -60.0,
    "C": 1.0, #
    "sigma": 0.3,
    "ref_dvdt": 2.5,   # AP duration
    "refactory": 15.0,  # refactory for threshold
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "channels_params"  : [kdr_channel],

    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 1.5707963267948966,
    },
}

common_int_params = {
    "name" : "common_int",
    "Vreset": -40.0,
    "Vt": -55.0, #-65.0, -60.0, #
    "gl": 0.18,
    "El": -60.0,
    "C": 1.0, #
    "sigma": 0.3,
    "ref_dvdt": 2.5,   # AP duration
    "refactory": 15.0,  # refactory for threshold
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "channels_params"  : [kdr_channel, ka_channel],

    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 1.5707963267948966,
    },
}

###############################################################################
kdr_channel_OLM_saraga = {
    "channel_class" : Chs.Kdr_channelOLM_Saraga,
    "gmax" : 23.0,
    "Erev" : -100.0,
    "degrees" : [4, ],
    "x_reset" : [0.67, ],
}

ka_channel_OLM_saraga = {
    "channel_class" : Chs.KA_channelOLM_Saraga,
    "gmax" : 16.0,
    "Erev" : -100.0,
    "degrees" : [1, 1],
    "x_reset" : [0.25, 0.0],
}

h_channel_OLM_saraga = {
    "channel_class" : Chs.H_channelOLM_Saraga,
    "gmax" : 8.0,
    "Erev" : -32.0,
    "degrees" : [1,],
    "x_reset" : [0.0001, ],
}

olm_saraga_params = {
    "name": "olm",
    "Vreset": -40.0,
    "Vt": -61.0,
    "gl": 0.05,
    "El": -70.0,
    "C": 1.3,  #
    "sigma": 0.3,
    "ref_dvdt": 2.0,  # AP duration
    "refactory": 15.0,  # refactory for threshold
    "Iext": -0.5,
    "N": 400,
    "dts": 0.5,

    "channels_params": [kdr_channel_OLM_saraga, ka_channel_OLM_saraga, h_channel_OLM_saraga],

    "target": {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 1.5707963267948966,
    },

}

###############################################################################


#population = ctfeq.HH_Neuron(olm_params, dt=0.1)
# population = ctfeq.HH_Neuron(ngf_params, dt=0.1)
#population = ctfeq.HH_Neuron(common_int_params, dt=0.1)
population = ctfeq.HH_Neuron(olm_saraga_params, dt=0.1)
y0 = population.get_y0()
t = tf.range(0.0, 150.0, 0.1, dtype=tf.float64)
# dydt = population(t[0], y0)
# print(dydt)

solution = odeint(population, y0, t, method="euler")
firing_cbrd = solution[:, 0]
Vm = solution[:, 797]

with h5py.File("com.hdf5", "w") as file:
    file.create_dataset("Vm", data=Vm)
    file.create_dataset("SpikeRate", data=firing_cbrd)
    file.create_dataset("Solution", data=solution)

n = solution[:, 1197]
a = solution[:, 1597]
b = solution[:, 1999]

fig, axes = plt.subplots(nrows=5, sharex=True)
axes[0].plot(t, firing_cbrd, linewidth=1)
axes[0].set_title("Firing rate")
axes[1].plot(t, Vm, linewidth=4)
axes[2].plot(t, n, linewidth=4)

###firing_monte_carlo = get_monte_carlo()
# axes[3].plot(t, a, linewidth=4)
# axes[4].plot(t, b, linewidth=4)
####axes.plot(t, firing_monte_carlo, linewidth=1)
# axes.set_ylim(0, None)
# axes.set_xlim(0, None)
plt.show()