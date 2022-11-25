import numpy as np
import tensorflow as tf
from tfdiffeq import odeint
import cbrd_tfdiffeq as ctfeq
import matplotlib.pyplot as plt
from scipy.signal.windows import parzen

def get_monte_carlo():
    N = 5000

    duration = 200
    dt = 0.1

    Cm = 1.0
    Vreset = -90.0
    VT = -50.0
    gl = 0.1
    El = -60.0
    sigma = 0.3
    Iext_mean = 1.0
    Vm = np.zeros(N, dtype=np.float64) + Vreset

    n_iter = int(duration / dt)
    firings = np.zeros(n_iter, dtype=float)


    sigma = sigma / np.sqrt(dt)

    for idx in range(n_iter):
        Iext = np.random.normal(loc=Iext_mean, scale=sigma, size=Vm.size)
        Vm = Vm + dt * (gl * (El - Vm) + Iext) / Cm

        fired = (Vm >= VT)
        firings[idx] = np.mean(fired) / dt

        Vm[fired] = Vreset

    win = parzen(15)
    win = win / np.sum(win)
    firings = np.convolve(firings, win, mode='same')
    return firings
##############################################################################



pvbas_params = {
    "name" : "pvbas",
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,
    "sigma": 0.3,
    "ref_dvdt": 3.0,
    "refactory": 3.0,  # refactory for threshold
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 50.0,
        "phase": 1.5707963267948966,
    },
}

population = ctfeq.LIF_Neuron(pvbas_params, dt=0.1)
y0 = population.get_y0()
t = tf.range(0.0, 200.0, 0.1, dtype=tf.float64)
solution = odeint(population, y0, t, method="euler")

fig, axes = plt.subplots(nrows=1, sharex=True)
firing_cbrd = solution[:, 0]
firing_monte_carlo = get_monte_carlo()
axes.plot(t, firing_cbrd, linewidth=4)
axes.plot(t, firing_monte_carlo, linewidth=1)
axes.set_ylim(0, None)
axes.set_xlim(0, None)
plt.show()