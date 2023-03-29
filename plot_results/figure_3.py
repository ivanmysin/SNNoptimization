import numpy as np
import matplotlib.pyplot as plt
from plotting_params import plotting_colors
from scipy.signal.windows import parzen
import h5py
import pickle
params = {'legend.fontsize': '16',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large',
          }
plt.rcParams.update(params)
TEXTFONTSIZE = 'xx-large'

Parzen = parzen(101)
Parzen = Parzen / np.sum(Parzen)

with open('/home/ivan/Data/Opt_res/LIF_params_net.pickle', 'rb') as file:
    params_net = pickle.load(file)

path = '/home/ivan/Data/phase_relations/!!!LIF_solution_310.hdf5'


hf = h5py.File(path, 'r')
dset_solution = hf['solution']
dset_gbarS = hf['SynapticConductance:0']

nsyns = dset_gbarS.size


start_R_idx = nsyns
end_R_idx = start_R_idx + nsyns
Y = dset_solution[:, start_R_idx : end_R_idx]




t = np.linspace(0, 1800, dset_solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * 0.001*t * 7.0) + 1)

gridspec_kw = {
    "width_ratios" : [0.15, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1],
}
fig, axes = plt.subplots(nrows=2, ncols=len(plotting_colors["neurons_order"])+1, figsize=(30, 5), gridspec_kw=gridspec_kw)


neuron_idxs_in_sol = np.asarray([dset_solution.attrs[neuron_name] for neuron_name in plotting_colors["neurons_order"]])
sourse_neurons_idxes = np.argsort(neuron_idxs_in_sol)

pop_indxes_keys = {}
for neuron_name in plotting_colors["neurons_order"]:
    pop_indxes_keys[neuron_name] = dset_solution.attrs[neuron_name]

for neuron_idx, (neuron_name, neuron_idx_in_sol) in enumerate(sorted(pop_indxes_keys.items(), key=lambda item: item[1])):

    plot_idx = neuron_idx + 1

    axes[0, plot_idx].set_title(neuron_name)

    if neuron_idx == 0:
        axes[0, plot_idx].set_ylabel(r"$\mu S$")
        axes[1, plot_idx].set_ylabel(r"$\mu S$")
    axes[1, plot_idx].set_xlabel("Time (ms)")
    axes[0, plot_idx].xaxis.set_ticklabels([])

    exc_g = 0
    inh_g = 0
    for idx in range(nsyns):
        syn = params_net["params_synapses"][idx]
        if neuron_name != syn["post_name"]:
            continue

        g_syn = Y[:, idx] * 1000 * dset_gbarS[idx]
        if syn["Erev"] == 0.0:
            exc_g += g_syn
            ax = axes[0, plot_idx]
        elif syn["Erev"] == -75.0:
            inh_g += g_syn
            ax = axes[1, plot_idx]
        else:
            ax = None

        color = plotting_colors["neuron_colors"][syn["pre_name"]]
        ax.plot(t, g_syn, linestyle="-", label=syn["pre_name"], color=color)

    mean_reletion = np.mean(exc_g[10000:] / inh_g[10000:])
    std_reletion = np.std(exc_g[10000:] / inh_g[10000:])
    print(neuron_name, mean_reletion, std_reletion)

    axes[0, plot_idx].plot(t, exc_g, linestyle=(0, (1, 1)), label="sum exc", color='orange', linewidth=2)
    axes[1, plot_idx].plot(t, inh_g, linestyle=(0, (1, 1)), label="sum inh", color='magenta', linewidth=2)

    sine_amples_exc = 0.7*np.max(exc_g[10000:]) * sine
    axes[0, plot_idx].plot(t, sine_amples_exc, linestyle='--', label="cos", color='black')

    sine_amples_inh = 0.7*np.max(inh_g[10000:]) * sine
    axes[1, plot_idx].plot(t, sine_amples_inh, linestyle="--", label="cos", color='black')

    axes[0, plot_idx].set_ylim(0.0, 1.1*np.max(exc_g[10000:]))
    axes[1, plot_idx].set_ylim(0.0, 1.1*np.max(inh_g[10000:]))

for ax1 in axes:
    for ax in ax1:
        ax.set_xlim(1000, 1284)

lines = []
labels = ['sum exc', 'sum inh', "ec3", "ca3pyr", "ca1pyr", 'pvbas', 'olm', "cckbas", "bis", "ivy", "ngf", 'cos']


for label in labels:
    for ax in fig.axes:
        Line, Label = ax.get_legend_handles_labels()
        try:
            line_idx = Label.index(label)
            lines.append(Line[line_idx])
            print(label)
            break
        except ValueError:
            continue

#print(len(labels), len(lines))

fig.legend(lines, labels,  ncol=15, loc='lower left', bbox_to_anchor =(0.15, 0.1), )


ax0 = axes[0, 0]
ax0.axis("off")
ax0.set_xlim(0, 1)
ax0.set_ylim(0, 1)
ax0.text(0.0, 0.5, " Conductivity of \n exciting inputs", fontsize=TEXTFONTSIZE)

ax0 = axes[1, 0]
ax0.axis("off")
ax0.set_xlim(0, 1)
ax0.set_ylim(0, 1)
ax0.text(0.0, 0.5, " Conductivity of \n inhibitory inputs", fontsize=TEXTFONTSIZE)

fig.subplots_adjust(bottom=0.4, wspace=0.4, hspace=0.4, left=0.05, right=0.95)
#fig.tight_layout()

fig.savefig('/home/ivan/Data/phase_relations/figures/Fig_3.png', dpi=500)
hf.close()
plt.show()
