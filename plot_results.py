import numpy as np
import matplotlib.pyplot as plt
import h5py
import tensorflow as tf
import cbrd_tfdiffeq
from code_generated_params import params_net

generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])


path = '/media/reseacher/3baf6c7e-8a20-4236-b3c9-a0ae7bed9266/Data/SSN_simulated/HHolmx10/solution_113.hdf5'
#path = '/media/reseacher/8f91cdcb-03d4-4fce-b560-a5796564d923/home/reseacher/Data/snn3/solution_500.hdf5'

hf = h5py.File(path, 'r')
dset_solution = hf['solution']
dset_targets = hf['targets']
solution = dset_solution[:]
targets = dset_targets[:]

t = np.linspace(0, 1.8, dset_solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * t * 8.0) + 1)

pop_indxes_keys = {}
for key, value in dset_solution.attrs.items(): #  :
    #pop_indxes_keys[neuron["name"]] = 0
    if key.find("Iext") == -1:
        pop_indxes_keys[key] = value


Targets_spikes_rates = generators4targets(1000.0 * tf.reshape(t, shape=(-1, 1)))


fig, axes = plt.subplots( nrows=len(pop_indxes_keys.keys()), sharex=True )
if len(pop_indxes_keys) == 1:
    axes = [axes, ]
for idx, (neuron_name, neuron_idx) in enumerate(sorted(pop_indxes_keys.items(),key=lambda item:item[1] )):
    ax = axes[idx]
    firings = dset_solution[:, neuron_idx]
    target = targets[:, idx]
    ax.plot(t, firings, label=neuron_name)
    sine_ampls = sine * np.max(target)
    ax.plot(t, sine_ampls, linestyle="--", label = "cos", color='black')
    ax.plot(t, Targets_spikes_rates[:, idx], linewidth=2, label = "full target", color='red')
    #ax.plot(t, target, label = "target", linewidth=1, color='green')
    ax.legend(loc = "upper right")

    ax.set_ylim(0, np.max(target))

hf.close()
plt.show()
