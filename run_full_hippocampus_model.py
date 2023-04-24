import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
import cbrd_tfdiffeq
import network2multycomps
from full_hippocampus_code_generated_params import params_net
import h5py
from time import time

# optimized_results = '/media/LD/Data/SSN_simulated/solution_500.hdf5'
#
# with h5py.File(optimized_results, "r") as h5file:
#     sol_dset = h5file["solution"]
#     for neuron_params in params_net["params_neurons"]:
#         iext_attr_name = neuron_params["name"] + "_Iext"
#         neuron_params["Iext"] = sol_dset.attrs[iext_attr_name]
#
#     w_coeff = 1
#     for syn_idx, synapse_params in enumerate(params_net["params_synapses"]):
#         if synapse_params["pre_name"] in ["ca3pyr", "ca1pyr"]:
#             w_coeff = 10
#         if synapse_params["pre_name"] in ["ec3", ]:
#             w_coeff = 3.33
#
#         gbarS = h5file["SynapticConductance:0"][syn_idx]
#         synapse_params["w"] = w_coeff * h5file["Wplasticsyns:0"][syn_idx]
#
#         synapse_params["tau_f"] = h5file["tau_f:0"][syn_idx]
#         synapse_params["tau_r"] = h5file["tau_r:0"][syn_idx]
#         synapse_params["tau_d"] = h5file["tau_d:0"][syn_idx]
#         synapse_params["Uinc"] = h5file["Uinc:0"][syn_idx]
#         synapse_params["gbarS"] = gbarS
#         w_coeff = 1

path4savingresults_template = '/media/LD/Data/SSN_simulated/Full_hippocampus/solution_{:03}.hdf5'

Optimizer = Adam(learning_rate=0.001)  # Adagrad #Adadelta
t = tf.range(0.0, 18.0, 0.1, dtype=tf.float64)
# generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])
# Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

net = network2multycomps.Networkmcomps(params_net)
n_two_coms = 2*18
stength = tf.zeros(n_two_coms, dtype=tf.float64) + 3.0 #  [3.0, 3.0]
net.set_compartmets(n_two_coms, stength)
net.set_optimizator(Optimizer)

#print(len(net.neurons), tf.size(net.ro_0_indexes))

#y0 = net.get_y0()
# solution = net.run_simulation(t, y0)
#
# file = h5py.File('/home/ivan/Data/Full_rhythms/tests/sol_test.hdf5', mode='w')
# file.create_dataset('solution', data=solution)
# file.close()



targets_firings = []
for cell_p in params_net['params_neurons']:
    if len(cell_p['target'].keys()) == 0:
        targets_firings.append(None)
    else:
        Gen = cbrd_tfdiffeq.VonMissesGenerators(cell_p['target'])
        tar_fir = Gen(t)
        targets_firings.append(tar_fir)

targets_lfp = []
for idx in range(n_two_coms//2):
    targets_lfp.append( tf.math.cos(2*np.pi*7*0.001*t) )

number_of_simulation_0 = 0
for idx in range(1000):
    timer = time()
    number_of_simulation = number_of_simulation_0 + idx + 1

    path = path4savingresults_template.format(number_of_simulation)
    solution, clearloss, fullloss = net.fit(t, targets_firings, targets_lfp, path4saving=path, n_inter=1, win4_start=10000,
                                            win4grad=500)

    #net.save_simulation_data(path, solution, Targets_spikes_rates)
    print("Прогон № ", str(number_of_simulation), ", Clear Loss = ", float(clearloss), ", Full Loss = ",
          float(fullloss), ", time = ", str((time() - timer) / 60), " mins")





