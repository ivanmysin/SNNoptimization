import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import h5py
from code_generated_params import params_net
import pandas as pd
from pprint import pprint
import cbrd_tfdiffeq

# "ca3pyr","ca1pyr","ec3",
neurons_names = ["pvbas", "olm", "cckbas", "bis", "aac", "ivy", "ngf"]
dataphases = pd.read_csv("inputs_data.csv", comment="#")
"""
targets = []

for name in neurons_names:
    params = {
        "R": float(dataphases[name][dataphases["Parameter"] == "R"]),
        "freq": 5,
        "mean_spike_rate": 5,
        "phase": np.deg2rad( float(dataphases[name][dataphases["Parameter"] == "phi"]) ),
    }
    targets.append(params)

gererators = cbrd_tfdiffeq.VonMissesGenerators(targets)

t = tf.range(0, 500, 0.1, dtype=tf.float64)
t = tf.reshape(t, shape=(-1, 1))

targets_spikes_rates = gererators(t)

t = t.numpy()
t = t.ravel() * 0.001
sine = 0.5 * (np.cos(2 * np.pi * t * 5) + 1)

fig, axes = plt.subplots(nrows=len(targets) )
for idx, ax in enumerate(axes):
    #ax.plot(t, firings[:, idx], label=neurons_names[idx])
    sine_ampls = sine * np.max(targets_spikes_rates[:, idx])
    ax.plot(t, sine_ampls, label = "cos")
    ax.plot(t, targets_spikes_rates[:, idx], label = neurons_names[idx])
    ax.legend(loc = "upper right")

"""
hf = h5py.File('/home/ivan/Data/interneurons_theta/solution_0.hdf5', 'r')
solution = hf['solution'][:]
hf.close()

number_neurons = len(params_net["params_neurons"])
number_synapses = len(params_net["params_synapses"])

fir_start_idx = 3 * number_synapses

firings = solution[:, fir_start_idx+1::800]

t = np.linspace(0, 1.2, solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * t * 5) + 1)

fig, axes = plt.subplots(nrows=number_neurons)
for idx, ax in enumerate(axes):
    ax.plot(t, firings[:, idx], label=neurons_names[idx])
    sine_ampls = sine * np.max(firings[:, idx])
    ax.plot(t, sine_ampls, label = "cos")
    #ax.plot(t, targets_spikes_rates[:, idx], label = "target")
    ax.legend(loc = "upper right")




plt.show()
