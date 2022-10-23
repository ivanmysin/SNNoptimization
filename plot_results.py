import numpy as np
import matplotlib.pyplot as plt
import h5py

hf = h5py.File('/home/ivan/Data/interneurons_theta/solution_062.hdf5', 'r')
dset_solution = hf['solution']
dset_targets = hf['targets']
solution = dset_solution[:]
targets = dset_targets[:]

t = np.linspace(0, 1.2, solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * t * 5) + 1)


fig, axes = plt.subplots( nrows=len(dset_solution.attrs.keys()), sharex=True )
for idx, (neuron_name, neuron_idx) in enumerate(sorted(dset_solution.attrs.items(),key=lambda item:item[1] )):
    ax = axes[idx]
    firings = solution[:, neuron_idx]
    target = targets[:, idx]
    ax.plot(t, firings, label=neuron_name)
    sine_ampls = sine * np.max(target)
    ax.plot(t, sine_ampls, linestyle="--", label = "cos")
    ax.plot(t, target, label = "target")
    ax.legend(loc = "upper right")

    ax.set_ylim(0, np.max(target))



hf.close()
plt.show()
