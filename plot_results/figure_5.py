import numpy as np
import matplotlib.pyplot as plt
from plotting_params import plotting_colors
from scipy.signal.windows import parzen
import h5py
params = {'legend.fontsize': '12',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large',
          }
plt.rcParams.update(params)
TEXTFONTSIZE = 'xx-large'




montecarlofile = h5py.File('/home/ivan/Data/phase_relations/MC_theta_freq/5.hdf5', "r")



gridspec_kw = {
    "width_ratios" : [0.1, 0.9],
}

plotting_order = plotting_colors["generators_order"] + plotting_colors["neurons_order"]

fig, axes = plt.subplots( nrows=len(plotting_order), ncols=2, \
                          gridspec_kw=gridspec_kw, constrained_layout=True, figsize=(15, 10))

t = np.linspace(0, 1800, 18000)
sine_ampls = 250 * (np.cos(2*np.pi*5*0.001*t) + 1)


for neuron_idx, neuron_name in enumerate(plotting_order):

    ax2 = axes[neuron_idx, 0]
    ax2.axis("off")
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.text(0.5, 0.5, neuron_name, fontsize=TEXTFONTSIZE)

    ax = axes[neuron_idx, 1]
    if neuron_idx == 0:
        ax.set_title("Raster plot")
    if neuron_idx == len(plotting_order) - 1:
        ax.set_xlabel("Time (ms)")
    else:
        ax.xaxis.set_ticklabels([])

    if neuron_idx == int(len(plotting_order)//2):
        ax.set_ylabel("Neuron index")

    neurons_indexes = montecarlofile[neuron_name + "_indexes"][:]
    neurons_times = montecarlofile[neuron_name + "_times"][:]


    ax.scatter(neurons_times, neurons_indexes, s=1, color=plotting_colors["neuron_colors"][neuron_name])

    if neuron_name in ["bis", "olm", "pvbas"]:
        cos_color = 'yellow'
    else:
        cos_color = 'black'
    ax.plot(t, sine_ampls, linestyle="--", label = "cos", color=cos_color)

    ax.set_ylim(0, 1000)
    ax.set_xlim(1000, 1600)

fig.savefig('/home/ivan/Data/phase_relations/figures/Fig_5.png', dpi=500)
montecarlofile.close()
plt.show()
