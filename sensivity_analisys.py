import numpy as np
import tensorflow as tf
import cbrd_tfdiffeq
from code_generated_params import params_net
import h5py
import pickle
import matplotlib.pyplot as plt

#optimized_results = '/home/ivan/Data/Opt_res/HH_solution_345!!!.hdf5'
with open('/home/ivan/Data/Opt_res/params_net.pickle', 'rb') as file:
    params_net = pickle.load(file)

path4savingresults = '/home/ivan/Data/phase_relations/test_solution.hdf5'


t = tf.range(0.0, 1243.0, 0.1, dtype=tf.float64)
net = cbrd_tfdiffeq.Network(params_net)
y0 = net.get_y0()
solution = net.run_simulation(t, y0)

file = h5py.File(path4savingresults, mode='w')
file.create_dataset('solution', data=solution)
file.create_dataset('ro_0_indexes', data=net.ro_0_indexes)

file.close()

t = np.linspace(0, 1.8, solution.shape[0])
sine = 0.5 * (np.cos(2 * np.pi * t * 6.0) + 1)

fig, axes = plt.subplots( nrows=7, sharex=True )
for idx in range(7):
    ax = axes[idx]
    neuron_idx = net.ro_0_indexes[idx]
    neuron_name = params_net['params_neurons'][idx]['name']
    firings = solution[10000:, neuron_idx]
    ax.plot(t[10000:], firings, label=neuron_name)

    sine_ampls = np.max(firings) * sine
    ax.plot(t[10000:], sine_ampls[10000:], linestyle="--", label = "cos", color='black')

    ax.legend(loc = "upper right")



plt.show()
