import numpy as np
import matplotlib.pyplot as plt
import h5py

hf = h5py.File('/home/ivan/Data/interurons_test/solution_011.hdf5', 'r')
dset_solution = hf['solution']
dset_targets = hf['targets']
solution = dset_solution[:]
targets = dset_targets[:]

t = np.linspace(0, 1.8, solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * t * 8.0) + 1)

pop_indxes_keys = {}
for key, value in dset_solution.attrs.items():
    if key.find("Iext") == -1:
        pop_indxes_keys[key] = value


fig, axes = plt.subplots( nrows=len(pop_indxes_keys.keys()), sharex=True )
if len(pop_indxes_keys) == 1:
    axes = [axes, ]
for idx, (neuron_name, neuron_idx) in enumerate(sorted(pop_indxes_keys.items(),key=lambda item:item[1] )):
    ax = axes[idx]
    firings = solution[:, neuron_idx]
    target = targets[:, idx]
    ax.plot(t, firings, label=neuron_name)
    sine_ampls = sine * np.max(target)
    ax.plot(t, sine_ampls, linestyle="--", label = "cos")
    #ax.plot(t[10000:], target, label = "target")
    ax.legend(loc = "upper right")

    #ax.set_ylim(0, np.max(target))

hf.close()
plt.show()
