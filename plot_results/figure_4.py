import numpy as np
import matplotlib.pyplot as plt
from plotting_params import plotting_colors
from scipy.signal.windows import parzen
import h5py
import pickle
import os
params = {'legend.fontsize': '16',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large',
          }
plt.rcParams.update(params)
TEXTFONTSIZE = 'xx-large'

Parzen = parzen(101)
Parzen = Parzen / np.sum(Parzen)

T_st_idx = 10000 # start of t

hf = h5py.File('/home/ivan/Data/phase_relations/!!!LIF_solution_310.hdf5', 'r')
dset_solution = hf['solution']
neuron_idx_in_sols = []
for neuron_name in plotting_colors["neurons_order"]:
    neuron_idx_in_sols.append( dset_solution.attrs[neuron_name] )
hf.close()

path2files = '/home/ivan/Data/phase_relations/theta_freqs/'
files = os.listdir(path2files)
theta_freqs = [float(f.split(".")[0]) for f in files]
theta_phases4plots = np.linspace(-np.pi, np.pi, 100)
sine = 0.5 * (np.cos(theta_phases4plots) + 1)

fig, axes = plt.subplots(nrows=len(plotting_colors["neurons_order"]), ncols=len(theta_freqs)+1, \
                        constrained_layout=True, figsize=(15, 15)  )

for freq_idx, (freq, file) in enumerate(sorted(zip(theta_freqs, files), key=lambda pair: pair[0])):
    if file.find('hdf5') == -1: continue
    filepath = path2files + file

    hf = h5py.File(filepath, 'r')
    dset_solution = hf['solution']
    t = np.linspace(0, 1800, dset_solution.shape[0])[T_st_idx:]
    theta_phases = (2 * np.pi * 0.001 * t * freq)%(2 * np.pi)
    theta_phases[theta_phases > np.pi] -= 2 * np.pi

    for neuron_idx, neuron_name in enumerate(plotting_colors["neurons_order"]):
        neuron_idx_in_sol = neuron_idx_in_sols[neuron_idx]
        ax = axes[neuron_idx, freq_idx+1]

        if neuron_idx == 0:
            ax.set_title(str(int(freq)) + " Hz")

        if (neuron_idx == len(plotting_colors["neurons_order"]) - 1) and (freq_idx == int(len(theta_freqs) // 2)):
            ax.set_xlabel("Phase (rad)")

        if neuron_idx < (len(plotting_colors["neurons_order"]) - 1):
            ax.xaxis.set_ticklabels([])

        if (neuron_idx == int(len(plotting_colors["neurons_order"]) // 2)) and (freq_idx == 0):
            ax.set_ylabel("Hz/rad")

        if freq_idx > 0:
            ax.yaxis.set_ticklabels([])


        firings = 1000 * dset_solution[T_st_idx:, neuron_idx_in_sol]
        firings_hist, firings_bins = np.histogram(theta_phases, bins=20, weights=firings, density=True, range=[-np.pi, np.pi])
        firings_bins = 0.5*(firings_bins[:-1] + firings_bins[1:])
        ax.plot(firings_bins, firings_hist, color=plotting_colors["neuron_colors"][neuron_name], linewidth=2, label="CBRD")

        # neurons_indexes = montecarlofile[neuron_name + "_indexes"][:]
        # neurons_times = montecarlofile[neuron_name + "_times"][:]
        # montecarlofirings, _ = np.histogram(neurons_times, bins=t)
        # montecarlofirings = montecarlofirings / np.max(neurons_indexes + 1)
        # montecarlofirings = montecarlofirings / (0.001 * (t[1] - t[0]))
        # montecarlofirings = np.convolve(montecarlofirings, Parzen, mode='same')

        # ax.plot(t[:-1], montecarlofirings, linestyle="--", color=plotting_colors["neuron_colors"][neuron_name],
        #         label="Monte-Carlo")
        sine_ampls = sine * 0.7 * np.max(firings_hist)
        ax.plot(theta_phases4plots, sine_ampls, linestyle="--", label="cos", color='black')
        ax.set_ylim(0, 0.45)
        ax.set_xlim(-np.pi, np.pi)

    hf.close()

for ax2, neuron_name in zip(axes[:, 0], plotting_colors["neurons_order"]):
    ax2.axis("off")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.text(0.0, 0.5, neuron_name, fontsize=TEXTFONTSIZE)

fig.savefig('/home/ivan/Data/phase_relations/figures/Fig_4.png', dpi=250)
plt.show()