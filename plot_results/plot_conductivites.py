import numpy as np
from code_generated_params import params_net
import h5py
import pickle
import matplotlib.pyplot as plt
from plotting_params import plotting_colors

path = '/home/ivan/Data/Opt_res/solution_947.hdf5'

hf = h5py.File(path, 'r')
dset_solution = hf['solution']
dset_gbarS = hf['SynapticConductance:0']


nsyns = len(params_net["params_synapses"])
start_R_idx = nsyns
end_R_idx = start_R_idx + nsyns
Y = dset_solution[:, start_R_idx : end_R_idx]

t = np.linspace(0, 1.8, dset_solution.shape[0])


fig, axes = plt.subplots( nrows=3, sharex=True, figsize=(10, 10) )

post_neuron = "aac"

exc_g = 0
inh_g = 0
for idx in range(len(params_net["params_synapses"])):
    syn = params_net["params_synapses"][idx]
    if post_neuron != syn["post_name"]:
        continue

    g_syn = Y[:, idx] * dset_gbarS[idx]
    if syn["Erev"] == 0.0:
        exc_g += g_syn
        ax = axes[0]
    elif syn["Erev"] == -75.0:
        inh_g += g_syn
        ax = axes[1]
    else:
        pass

    color = plotting_colors["neuron_colors"][syn["pre_name"]]
    ax.plot(t, g_syn, linestyle="-", label=syn["pre_name"], color=color)


sine = 0.5 * (np.cos(2 * np.pi * t * 7.0) + 1)
axes[0].plot(t, exc_g, linestyle="-", label = "sum exc", color='orange', linewidth=5)
axes[1].plot(t, inh_g, linestyle="-", label = "sum inh", color='magenta', linewidth=5)

sine_amples_exc = np.max(exc_g[10000:]) * sine
axes[0].plot(t, sine_amples_exc, linestyle="--", label = "cos", color='black')

sine_amples_inh = np.max(inh_g[10000:]) * sine
axes[1].plot(t, sine_amples_inh, linestyle="--", label = "cos", color='black')

inh_exc_relation = sine_amples_inh/sine_amples_exc
axes[2].plot(t, inh_exc_relation, label = "relation", color='black')

print(inh_exc_relation[10000:])


for ax in axes:
    ax.set_xlim(1.0, 1.8)
    ax.set_ylim(0.0, None)
    ax.legend(loc='upper right')
plt.show()

hf.close()

