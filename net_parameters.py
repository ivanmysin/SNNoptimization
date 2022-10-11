########################################
##### block of neurons params ##########

pvbas_params = {
    "name" : "pvbas",
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,
    "sigma": 0.3,
    "ref_dvdt": 3.0,
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 5,
        "phase": 1.5707963267948966,
    }
}

olm_params = {
    "name" : "olm",
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.5,
    "sigma": 0.3,
    "ref_dvdt": 3.0,
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.3,
    "N": 400,
    "dts": 0.5,

    "target": {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 5,
        "phase": 3.14,
    },
}

##########################################
##### block of generators params #########
ca3pyr_params = {
    "name" : "ca3pyr",
    "R": 0.3,
    "freq": 5,
    "mean_spike_rate": 5.0,
    "phase": 1.3,
}

ca1pyr_params = {
    "name": "ca1pyr",
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 5,
    "phase": 3.14,
}

########################################
##### block of synapses params #########
ca3pyr2pvbas = {
    "w": 0.1,
    "pre_name": "ca3pyr",
    "post_name": "pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 10 * 0.908653493,
    "Erev": 0.0,
}
ca1pyr2olm = {
    "w": 0.1,
    "pre_name": "ca1pyr",
    "post_name": "olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 10* 1.699075536,
    "Erev": 0.0,
}
olm2pvbas = {
    "w": 0.01,
    "pre_name": "olm",
    "post_name": "pvbas",
    "tau_f": 16.57863002,
    "tau_r": 650.1346414,
    "tau_d": 5.685709176,
    "Uinc": 0.230148227,
    "gbarS": 1.567269637,
    "Erev": -75.0,
}

olm2aac = {
    "w": 0.01,
    "pre_name": "olm",
    "post_name": "aac",
    "tau_f": 16.57863002,
    "tau_r": 650.1346414,
    "tau_d": 5.685709176,
    "Uinc": 0.230148227,
    "gbarS": 1.567269637,
    "Erev": -75.0,
}


params_net = {
    "params_neurons" : [pvbas_params, olm_params],
    "params_generators" : [ca3pyr_params, ca1pyr_params],
    "params_synapses" : [ca3pyr2pvbas, ca1pyr2olm, olm2pvbas ],
}
