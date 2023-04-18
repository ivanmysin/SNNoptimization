import sys
sys.path.append('../')
import tensorflow as tf
import neuron_models
import network2multycomps
import full_hippocampus_params
import h5py
import matplotlib.pyplot as plt

params_net = full_hippocampus_params.params_net
net = network2multycomps.Networkmcomps(params_net)

stength = [3.0, 3.0]
net.set_compartmets(1, stength)

y0 = net.get_y0()
t = tf.range(0, 1000, 0.1, dtype=tf.float64)

solution = net.run_simulation(t, y0)

h5pyfile = h5py.File('/home/ivan/Data/test/som.hdf5', mode='w')
h5pyfile.create_dataset('solution', data=solution)
h5pyfile.close()

fig, axes = plt.subplots(nrows=len(params_net["params_neurons"]))


for idx in range(len(params_net["params_neurons"])):
    try:
        firings = solution[:, net.neurons[idx].ro_start_idx]
    except AttributeError:
        continue

    axes[idx].plot(t, firings)
    axes[idx].set_title(net.neurons[idx].population_name)

plt.show()
