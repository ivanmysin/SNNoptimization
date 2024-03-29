#from code_generated_params import params_net
from lif_net_params import params_net
import h5py
import pickle

#optimized_results = "/home/ivan/Data/Opt_res/HH_solution_345!!!.hdf5" #"/home/ivan/Data/Opt_res/LIF_solution_500.hdf5" #"
optimized_results = "/home/ivan/Data/Opt_res/!!!LIF_solution_310.hdf5"

with h5py.File(optimized_results, "r") as h5file:
    sol_dset = h5file["solution"]
    for neuron_params in params_net["params_neurons"]:
        iext_attr_name = neuron_params["name"] + "_Iext"
        neuron_params["Iext"] = sol_dset.attrs[iext_attr_name]

    for syn_idx, synapse_params in enumerate(params_net["params_synapses"]):
        synapse_params["w"] = h5file["Wplasticsyns:0"][syn_idx]
        synapse_params["tau_f"] = h5file["tau_f:0"][syn_idx]
        synapse_params["tau_r"] = h5file["tau_r:0"][syn_idx]
        synapse_params["tau_d"] = h5file["tau_d:0"][syn_idx]
        synapse_params["Uinc"] = h5file["Uinc:0"][syn_idx]
        synapse_params["gbarS"] = h5file["SynapticConductance:0"][syn_idx]

with open('/home/ivan/Data/Opt_res/LIF_params_net.pickle', 'wb') as file:
    pickle.dump(params_net, file)
