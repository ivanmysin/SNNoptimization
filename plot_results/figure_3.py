import numpy as np
import matplotlib.pyplot as plt
from plotting_params import plotting_colors
import h5py
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large',
          }
plt.rcParams.update(params)
TEXTFONTSIZE = 'xx-large'

path = '/home/ivan/Data/phase_relations/!!!LIF_solution_310.hdf5'


hf = h5py.File(path, 'r')
dset_solution = hf['solution']
try:
    dset_targets = hf['targets']
    targets = dset_targets[:]
except KeyError:
    targets = np.zeros_like(dset_solution.shape)


t = np.linspace(0, 1800, dset_solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * 0.001*t * 7.0) + 1)

gridspec_kw = {
    "width_ratios" : [0.8, 0.2],
}
fig, axes = plt.subplots( nrows=len(plotting_colors["neurons_order"]), ncols=2, \
                          gridspec_kw=gridspec_kw, constrained_layout=True, figsize=(15, 10))


neuron_idxs_in_sol = np.asarray([dset_solution.attrs[neuron_name] for neuron_name in plotting_colors["neurons_order"]])
sourse_neurons_idxes = np.argsort(neuron_idxs_in_sol)

pop_indxes_keys = {}
for neuron_name in plotting_colors["neurons_order"]:
    pop_indxes_keys[neuron_name] = dset_solution.attrs[neuron_name]

for neuron_idx, (neuron_name, neuron_idx_in_sol) in enumerate(sorted(pop_indxes_keys.items(), key=lambda item: item[1])):

    ax2 = axes[neuron_idx, 1]
    ax2.axis("off")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.text(0, 0.5, neuron_name, fontsize=TEXTFONTSIZE)

    ax = axes[neuron_idx, 0]
    if neuron_idx == 0:
        ax.set_title("Population frequency")
    if neuron_idx == len(plotting_colors["neurons_order"]) - 1:
        ax.set_xlabel("Time (ms)")
    if neuron_idx == int(len(plotting_colors["neurons_order"])//2):
        ax.set_ylabel("sp/sec")


    firings = 1000 * dset_solution[:, neuron_idx_in_sol]
    target = 1000 * dset_targets[:, neuron_idx]
    ax.plot(t, firings, color=plotting_colors["neuron_colors"][neuron_name])
    sine_ampls = sine * np.max(target)
    ax.plot(t, sine_ampls, linestyle="--", label = "cos", color='black')
    ax.plot(t, target, label = "target", color='green')

    ax.set_ylim(0, 1.2*np.max(firings[10000:]) )


    if neuron_idx == 0:
        ax.legend(loc="upper right")

    #ax.set_ylim(0, 1.2*np.max(target))
    ax.set_xlim(800, 1800)

fig.savefig('/home/ivan/Data/phase_relations/figures/Fig_3.png')
hf.close()
plt.show()
