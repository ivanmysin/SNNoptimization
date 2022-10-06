
########################################
##### block of neurons params #########
pvbas_params = {
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
    "dts": 0.5
}

olm_params = {
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
    "dts": 0.5
}

cckbas_params = {
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.5,
    "sigma": 0.3,
    "ref_dvdt": 3.0,
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5
}
bis_params = {
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,
    "sigma": 0.3,
    "ref_dvdt": 5.0,
    "refactory": 5.0,  # refactory for threshold
    "Iext": 0.2,
    "N": 400,
    "dts": 0.5
}

aac_params = {
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
    "dts": 0.5
}

ivy_params = {
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.7,
    "sigma": 0.3,
    "ref_dvdt": 3.0,
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5
}

ngf_params = {
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.4,
    "sigma": 0.3,
    "ref_dvdt": 3.0,
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.2,
    "N": 400,
    "dts": 0.5
}
########################################
##### block of synapses params #########
pvbas2pvbas = {
    "w": 1.6,
    "pre": 0,  # None,
    "post": 1,  # None,
    "tau_f": 12.0,  # ms
    "tau_r": 1912.0,  # ms   # Synaptic depression rate
    "tau_d": 2.8,  #
    "Uinc": 0.153,
    "gbarS": 1.0,
    "Erev": -75.0,

}

##########################################
##### block of generators params #########
ca3pyr = {
    "R": 0.3,
    "freq": 5,
    "mean_spike_rate": 5,
    "phase": 1.3,
}

ca1pyr = {
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 5,
    "phase": 3.14,
}

ec3 = {
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 5,
    "phase": -1.04,
}

params_net = {
        "params_neurons" : [pvbas_params, olm_params, cckbas_params, bis_params, aac_params, ivy_params, ngf_params,],
        "params_synapses" : [pvbas2pvbas, ],
        "params_generators" : [ca3pyr, ca1pyr, ec3],
    }