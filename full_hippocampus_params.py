import neuron_models
import cbrd_tfdiffeq

ca3pyr_soma_params = {
    "name": "ca3pyr_soma",
    "neuron_class": neuron_models.Soma,
    "is_sim_rho": True,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target": {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 30,  # 20.0,
        "phase": 3.14,
    },
}

ca3pyr_dend_params = {
    "name": "ca3pyr_dend",
    "neuron_class": neuron_models.Dendrite,
    "is_sim_rho": False,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 0.0,  # AP duration
    "refactory": 0.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,
    "channels_params": [],
    "target": None,
}

ca3pvbas_params = {
    "name": "ca3pvbas",
    "neuron_class":  neuron_models.LIFCompartment, # cbrd_tfdiffeq.HH_Neuron,
    "is_sim_rho": True,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],

    "target": {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 24,  # 20.0,
        "phase": 1.5707963267948966,
    },
}
#######################################################################################
ec2_params = {
    "name" : "ec2",
    "R": 0.2,
    "freq": 7.0,
    "mean_spike_rate":  1.5, # 5, #
    "phase": -1.57,
}
#######################################################################################
ca3pyr2ca3pvbas = {
    "w": 0.5,
    "pre_name": "ca3pyr_soma",
    "post_name": "ca3pvbas",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 5*0.991873144,
    "Erev": 0.0,
}

ec22ca3pyr = {
    "w": 0.5,
    "pre_name": "ec2",
    "post_name": "ca3pyr_dend",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 5*0.991873144,
    "Erev": 0.0,
}

ca3pvbas2ca3pyr = {
    "w": 0.5,
    "pre_name": "ca3pvbas",
    "post_name": "ca3pyr_soma",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 5*0.991873144,
    "Erev": -75.0,
}
#######################################################################################
params_net = {
"params_neurons" : [ca3pyr_soma_params, ca3pyr_dend_params, ca3pvbas_params],
"params_generators" : [ec2_params, ],
#"params_generators" : [ca1pyr_params, ],
"params_synapses" : [ec22ca3pyr, ca3pyr2ca3pvbas, ca3pvbas2ca3pyr],
#"params_synapses" : [],
}