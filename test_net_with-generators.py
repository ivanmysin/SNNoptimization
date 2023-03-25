import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tfdiffeq import odeint, odeint_adjoint
import cbrd_tfdiffeq
import h5py
import pickle
#from code_generated_params import params_net

# optimized_results = "/home/ivan/Data/Opt_res/HH_solution_070.hdf5"
#
# with h5py.File(optimized_results, "r") as h5file:
#     sol_dset = h5file["solution"]
#     for neuron_params in params_net["params_neurons"]:
#         iext_attr_name = neuron_params["name"] + "_Iext"
#         neuron_params["Iext"] = sol_dset.attrs[iext_attr_name]
#
#     for syn_idx, synapse_params in enumerate(params_net["params_synapses"]):
#         synapse_params["w"] = h5file["Wplasticsyns:0"][syn_idx]
#         synapse_params["tau_f"] = h5file["tau_f:0"][syn_idx]
#         synapse_params["tau_r"] = h5file["tau_r:0"][syn_idx]
#         synapse_params["tau_d"] = h5file["tau_d:0"][syn_idx]
#         synapse_params["Uinc"] = h5file["Uinc:0"][syn_idx]
#         synapse_params["gbarS"] = h5file["SynapticConductance:0"][syn_idx]

with open('/home/ivan/Data/Opt_res/LIF_params_net.pickle', 'rb') as file:
    params_net = pickle.load(file)


t = tf.range(0.0, 1800.0, 0.1, dtype=tf.float64)
net = cbrd_tfdiffeq.Network(params_net)
y0 = net.get_y0()


solution = net.run_simulation(t, y0)

hf = h5py.File('/home/ivan/Data/phase_relations/com.hdf5', 'w')
solution_dset = hf.create_dataset('solution', data=solution.numpy() )
hf.close()


# fig, axes = plt.subplots(nrows=4, sharex=True)
# axes[0].plot(t, solution[:, 1], label="ca3pyr2pvbas")
# # axes[0].plot(t, solution[:, 2], label="olm2pvbas")
# # axes[0].legend(loc="upper left")
#
# axes[1].plot(t, solution[:, 3])
# # axes[1].plot(t, solution[:, 5])
# axes[2].plot(t, solution[:, 802]) # 1602
#
# axes[3].plot( solution[-1, 403:803] ) # 803:1603
# plt.show()
