import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam, Adadelta, Adagrad, RMSprop
import cbrd_tfdiffeq
from code_generated_params import params_net
import h5py
from time import time

optimized_results = '/media/LD/Data/SSN_simulated/HHolmx10/solution_168.hdf5'

with h5py.File(optimized_results, "r") as h5file:
    sol_dset = h5file["solution"]
    for neuron_params in params_net["params_neurons"]:
        iext_attr_name = neuron_params["name"] + "_Iext"
        # if neuron_params["name"] == 'olm___':
        #     neuron_params["Iext"] = 0.0
        # else:
        neuron_params["Iext"] = sol_dset.attrs[iext_attr_name]

    for syn_idx, synapse_params in enumerate(params_net["params_synapses"]):
        gbarS = h5file["SynapticConductance:0"][syn_idx]
        synapse_params["w"] = h5file["Wplasticsyns:0"][syn_idx]
        

        synapse_params["tau_f"] = h5file["tau_f:0"][syn_idx]
        synapse_params["tau_r"] = h5file["tau_r:0"][syn_idx]
        synapse_params["tau_d"] = h5file["tau_d:0"][syn_idx]
        synapse_params["Uinc"] = h5file["Uinc:0"][syn_idx]
        synapse_params["gbarS"] = gbarS


path4savingresults_template = '/media/LD/Data/SSN_simulated/HHolmx10/solution_{:03}.hdf5'  

Optimizer = Adam(learning_rate=0.001) # Adagrad #Adadelta
t = tf.range(0.0, 1800.0, 0.1, dtype=tf.float64)
generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])
Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

net = cbrd_tfdiffeq.Network(params_net)
net.set_optimizator(Optimizer)

number_of_simulation_0 = 168
for idx in range(500):
    timer = time()
    number_of_simulation = number_of_simulation_0 + idx + 1

    path = path4savingresults_template.format(number_of_simulation)
    solution, clearloss, fullloss = net.fit(t, generators4targets, path4saving=path, n_inter=1, win4_start = 10000, win4grad = 500)

    net.save_simulation_data(path, solution, Targets_spikes_rates)
    print("Прогон № ", str(number_of_simulation), ", Clear Loss = ", float(clearloss), ", Full Loss = ", float(fullloss), ", time = ", str((time() - timer)/60), " mins" )




