import sys
sys.path.extend(['/home/ivan/PycharmProjects/SNNoptimization/plot_results/'])
import numpy as np
import matplotlib.pyplot as plt
import h5py
from plotting_params import plotting_colors

resfile = h5py.File('/home/ivan/Data/interneurons_theta/Monte_Carlo.hdf5', "r")

fig, axes = plt.subplots(nrows=len(plotting_colors["neurons_order"]), constrained_layout=True, figsize=(10, 10))

phases4cos = np.linspace(-np.pi, np.pi, 100)
cos = 0.25*0.5*(np.cos(phases4cos) + 1)
for pop_idx, pop_name in enumerate(plotting_colors["neurons_order"]):
    neurons_indexes = resfile[pop_name + "_indexes"][:]
    neurons_times = resfile[pop_name + "_times"][:]
    neurons_phases = (2*np.pi*7*0.001*neurons_times)%(2*np.pi)
    neurons_phases[neurons_phases > np.pi] -= 2*np.pi

    hist, bins = np.histogram(neurons_phases, density=True, range=[-np.pi, np.pi], bins=30)

    axes[pop_idx].plot(bins[:-1], hist, color=plotting_colors["neuron_colors"][pop_name])
    axes[pop_idx].plot(phases4cos, cos, color="k", linestyle="--")
    axes[pop_idx].set_title(pop_name)



resfile.close()
plt.show()