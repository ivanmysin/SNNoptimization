import numpy as np
import matplotlib.pyplot as plt
import h5py



resfile = h5py.File('/home/ivan/Data/interneurons_theta/Monte_Carlo.hdf5', "r")
pop_name = 'aac'
# pop_times = resfile["ec3_times"][:]
# pop_indexes = resfile["ec3_indexes"][:]
pop_times = resfile[pop_name + "_times"][:]
pop_indexes = resfile[pop_name + "_indexes"][:]
resfile.close()

pop_freq, bins = np.histogram(pop_times, range=[0, 1800], bins=18001)
pop_freq = pop_freq / 2000 / 0.0001

mean_freq = pop_times.size / 1.8 / 2000
print(mean_freq)

fig, axes = plt.subplots(nrows=2)
axes[0].plot(bins[:-1], pop_freq)
axes[1].scatter(pop_times, pop_indexes)
#axes[pops_idx].set_title(SpkMon.source.name)
plt.show()