import numpy as np
import tensorflow as tf
from tfdiffeq import odeint
import cbrd_tfdiffeq as ctfeq
import matplotlib.pyplot as plt
from scipy.signal.windows import parzen


kdr_channel = {
    "channel_class" : ctfeq.BaseChannel,

    "gmax" : 40.0,
    "Erev" : -90.0,

    "degrees" : [4, ],
    "x_reset" : [0.45,],
}

int_params = {
    "name" : "int",
    "Vreset": -40.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,
    "sigma": 0.3,
    "ref_dvdt": 1.5,   # AP duration
    "refactory": 5.0,  # refactory for threshold
    "Iext": 1.5,
    "N": 400,
    "dts": 0.5,

    "channels_params"  : [kdr_channel, ],

    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 1.5707963267948966,
    },
}


population = ctfeq.HH_Neuron(int_params, dt=0.1)
y0 = population.get_y0()

#print(y0)
t = tf.range(0.0, 200.0, 0.1, dtype=tf.float64)
# dydt = population(t[0], y0)
# print(dydt)

solution = odeint(population, y0, t, method="euler")
firing_cbrd = solution[:, 0]
# Vm = solution[:, 798]
# n = solution[:, 1198]
fig, axes = plt.subplots(nrows=1, sharex=True)
# axes[0].plot(t, Vm, linewidth=4)
# axes[1].plot(t, n, linewidth=4)

###firing_monte_carlo = get_monte_carlo()
axes.plot(t, firing_cbrd, linewidth=1)
####axes.plot(t, firing_monte_carlo, linewidth=1)
# axes.set_ylim(0, None)
# axes.set_xlim(0, None)
plt.show()