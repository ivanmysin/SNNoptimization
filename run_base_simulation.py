import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam, Adadelta, Adagrad, RMSprop
import cbrd_tfdiffeq
from code_generated_params import params_net
import h5py

optimized_results = '/media/LD/Data/SSN_simulated/HHolmx10/solution_097.hdf5'
#'/media/reseacher/8f91cdcb-03d4-4fce-b560-a5796564d923/home/reseacher/Data/snn3/solution_500.hdf5'
#"/media/reseacher/3baf6c7e-8a20-4236-b3c9-a0ae7bed9266/Data/SSN_simulated/HH/solution_199.hdf5" #"/media/bigdisk/Data/SSN_simulated/HH/solution_201.hdf5"

with h5py.File(optimized_results, "r") as h5file:
    sol_dset = h5file["solution"]
    for neuron_params in params_net["params_neurons"]:
        iext_attr_name = neuron_params["name"] + "_Iext"
        if neuron_params["name"] == 'olm___':
            neuron_params["Iext"] = 0.0
        else:
            neuron_params["Iext"] = sol_dset.attrs[iext_attr_name]

    for syn_idx, synapse_params in enumerate(params_net["params_synapses"]):
        if synapse_params["post_name"] == 'olm_______':
            print("OLM !!!")
            gbarS = 10.0 * h5file["SynapticConductance:0"][syn_idx]
        else:
            gbarS = h5file["SynapticConductance:0"][syn_idx]
        
        synapse_params["w"] = h5file["Wplasticsyns:0"][syn_idx]
        synapse_params["tau_f"] = h5file["tau_f:0"][syn_idx]
        synapse_params["tau_r"] = h5file["tau_r:0"][syn_idx]
        synapse_params["tau_d"] = h5file["tau_d:0"][syn_idx]
        synapse_params["Uinc"] = h5file["Uinc:0"][syn_idx]
        synapse_params["gbarS"] = gbarS


path4savingresults_template = '/media/LD/Data/SSN_simulated/HHolmx10/solution_{:03}.hdf5'  
#'/media/reseacher/3baf6c7e-8a20-4236-b3c9-a0ae7bed9266/Data/SSN_simulated/HHolmx10/solution_{:03}.hdf5'  #'/home/ivan/Data/interurons_test/solution_{:03}.hdf5'
Optimizer = Adam(learning_rate=0.001) # Adagrad( #Adadelta
t = tf.range(0.0, 1800.0, 0.1, dtype=tf.float64)
generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])
Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

net = cbrd_tfdiffeq.Network(params_net)
net.set_optimizator(Optimizer)
#net.load_trained_variables('/media/reseacher/3baf6c7e-8a20-4236-b3c9-a0ae7bed9266/Data/SSN_simulated/HH/solution_003.hdf5')
"""
y0 = net.get_y0()
solution = net.run_simulation(t, y0)

path = path4savingresults_template.format(0)
net.save_simulation_data(path, solution, Targets_spikes_rates)

"""
number_of_simulation_0 = 97
for idx in range(500):
    number_of_simulation = number_of_simulation_0 + idx + 1

    path = path4savingresults_template.format(number_of_simulation)
    solution, clearloss, fullloss = net.fit(t, generators4targets, path4saving=path, n_inter=1, win4_start = 10000, win4grad = 500)

    net.save_simulation_data(path, solution, Targets_spikes_rates)
    print("Прогон № ", str(number_of_simulation), ", Clear Loss = ", float(clearloss), ", Full Loss = ", float(fullloss) )




