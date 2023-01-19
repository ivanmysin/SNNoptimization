import numpy as np
import matplotlib.pyplot as plt
import h5py

N = 200
dt = 0.01
duration  = 1800

datafile = h5py.File('/home/ivan/Data/interneurons_theta/Monte_Carlo.hdf5', 'r')

spike_rates = []
for dset_name, dset in datafile.items():
    if dset_name.find('_times') == -1: continue

    name = dset_name.split('_')[0]
    firings = dset[:]
    spike_rate, bins = np.histogram(firings, bins=duration, density=False, range=[0, duration])
    spike_rate = spike_rate / (1000*N*dt)
    spike_rates.append({"name":name, 'spike_rate':spike_rate})
datafile.close()

fig, axes = plt.subplots(nrows=len(spike_rates), sharex=True)

sine = 0.5*(np.cos(2*np.pi*8*bins[1:]*0.001) + 1)
for idx, sp in enumerate(spike_rates):
    axes[idx].plot(bins[1:], sp["spike_rate"])

    axes[idx].plot(bins[1:], np.max(sp["spike_rate"])*sine)
    axes[idx].set_title(sp["name"])


plt.show()