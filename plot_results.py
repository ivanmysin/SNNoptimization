import numpy as np
import matplotlib.pyplot as plt
import h5py

hf = h5py.File('/home/ivan/Data/interneurons_theta/solution_6.hdf5', 'r')
dset_solution = hf['solution']
dset_targets = hf['targets']
solution = dset_solution[:]
targets = dset_targets[:]

t = np.linspace(0, 1.2, solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * t * 5) + 1)







fig, axes = plt.subplots(nrows=7)
for idx, (neuron_name, neuron_idx) in enumerate(dset_solution.attrs.items()):
    ax = axes[idx]

    firings = solution[:, neuron_idx]
    target = targets[:, idx]
    ax.plot(t, firings, label=neuron_name)
    sine_ampls = sine * np.max(target)
    ax.plot(t, sine_ampls, label = "cos")
    ax.plot(t, target, label = "target")
    ax.legend(loc = "upper right")



hf.close()
plt.show()
