import numpy as np
import matplotlib.pyplot as plt
import h5py

resfile = h5py.File('/home/ivan/Data/interneurons_theta/Monte_Carlo.hdf5', "r")

# pop_times = resfile["ca1pyr_times"][:]
# pop_indexes = resfile["ca1pyr_indexes"][:]
pop_times = resfile["pvbas_times"][:]
pop_indexes = resfile["pvbas_indexes"][:]
resfile.close()

pop_freq, bins = np.histogram(pop_times, range=[0, 1800], bins=18001)
pop_freq = pop_freq / 1000 / 1000

mean_freq = pop_times.size / 1.8 / 200
print(mean_freq)

fig, axes = plt.subplots(nrows=2, sharex=True)
axes[0].plot(bins[:-1], pop_freq)
axes[1].scatter(pop_times, pop_indexes)
#axes[pops_idx].set_title(SpkMon.source.name)
plt.show()