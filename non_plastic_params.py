import cbrd_tfdiffeq as ctfeq
########################################
##### block of synapses params #########

synapses_params = [
    {   'Erev': 0,
        'delay': 2.5,
        'gbarS': 0.991873144,
        'pconn': 0.5,
        'post_name': 'aac',
        'pre_name': 'ca3pyr',
        'tau_decay': 6.3,
        'tau_rise': 2},
    {   'Erev': 0,
        'delay': 1.2,
        'gbarS': 1.494119161,
        'pconn': 0.5,
        'post_name': 'aac',
        'pre_name': 'ca1pyr',
        'tau_decay': 0.6,
        'tau_rise': 0.3},
    {   'Erev': 0,
        'delay': 10.0,
        'gbarS': 1.529326081,
        'pconn': 0.5,
        'post_name': 'aac',
        'pre_name': 'ec3',
        'tau_decay': 6.3,
        'tau_rise': 2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 3.523878672,
        'pconn': 0.1,
        'post_name': 'aac',
        'pre_name': 'pvbas',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.337587481,
        'pconn': 0.1,
        'post_name': 'aac',
        'pre_name': 'cckbas',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'aac',
        'pre_name': 'ngf',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.655937714,
        'pconn': 0.1,
        'post_name': 'aac',
        'pre_name': 'olm',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.44425622,
        'pconn': 0.1,
        'post_name': 'aac',
        'pre_name': 'bis',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.479657319,
        'pconn': 0.1,
        'post_name': 'aac',
        'pre_name': 'ivy',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': 0,
        'delay': 1.5,
        'gbarS': 0.908653493,
        'pconn': 0.5,
        'post_name': 'pvbas',
        'pre_name': 'ca3pyr',
        'tau_decay': 6.3,
        'tau_rise': 2.0},
    {   'Erev': 0,
        'delay': 1.2,
        'gbarS': 1.350968596,
        'pconn': 0.5,
        'post_name': 'pvbas',
        'pre_name': 'ca1pyr',
        'tau_decay': 0.2,
        'tau_rise': 0.07},
    {   'Erev': 0.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'pvbas',
        'pre_name': 'ec3',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 3.315200522,
        'pconn': 0.1,
        'post_name': 'pvbas',
        'pre_name': 'pvbas',
        'tau_decay': 4.8,
        'tau_rise': 0.8},
    {   'Erev': -75,
        'delay': 4.5,
        'gbarS': 1.236161794,
        'pconn': 0.1,
        'post_name': 'pvbas',
        'pre_name': 'cckbas',
        'tau_decay': 4.49,
        'tau_rise': 0.43},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.388199859,
        'pconn': 0.1,
        'post_name': 'pvbas',
        'pre_name': 'ngf',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.567269637,
        'pconn': 0.1,
        'post_name': 'pvbas',
        'pre_name': 'olm',
        'tau_decay': 7.5,
        'tau_rise': 0.25},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.469428253,
        'pconn': 0.1,
        'post_name': 'pvbas',
        'pre_name': 'bis',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.509851331,
        'pconn': 0.1,
        'post_name': 'pvbas',
        'pre_name': 'ivy',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': 0.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'cckbas',
        'pre_name': 'ca3pyr',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': 0.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'cckbas',
        'pre_name': 'ca1pyr',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': 0.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'cckbas',
        'pre_name': 'ec3',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 3.102685857,
        'pconn': 0.1,
        'post_name': 'cckbas',
        'pre_name': 'pvbas',
        'tau_decay': 2.67,
        'tau_rise': 0.29},
    {   'Erev': -75,
        'delay': 2.7,
        'gbarS': 1.397935548,
        'pconn': 0.1,
        'post_name': 'cckbas',
        'pre_name': 'cckbas',
        'tau_decay': 4.2,
        'tau_rise': 0.2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.590137208,
        'pconn': 0.1,
        'post_name': 'cckbas',
        'pre_name': 'ngf',
        'tau_decay': 10.0,
        'tau_rise': 0.5},
    {   'Erev': -75.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'cckbas',
        'pre_name': 'olm',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.578235331,
        'pconn': 0.1,
        'post_name': 'cckbas',
        'pre_name': 'bis',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'cckbas',
        'pre_name': 'ivy',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': 0,
        'delay': 10.2,
        'gbarS': 1.650136928,
        'pconn': 0.5,
        'post_name': 'ngf',
        'pre_name': 'ec3',
        'tau_decay': 3,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.588573475,
        'pconn': 0.1,
        'post_name': 'ngf',
        'pre_name': 'ngf',
        'tau_decay': 42,
        'tau_rise': 3.1},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.726166607,
        'pconn': 0.1,
        'post_name': 'ngf',
        'pre_name': 'olm',
        'tau_decay': 10.2,
        'tau_rise': 1.3},
    {   'Erev': 0.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'olm',
        'pre_name': 'ca3pyr',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': 0,
        'delay': 1.2,
        'gbarS': 16.99075536,
        'pconn': 0.5,
        'post_name': 'olm',
        'pre_name': 'ca1pyr',
        'tau_decay': 0.6,
        'tau_rise': 0.3},
    {   'Erev': -75.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'olm',
        'pre_name': 'bis',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.249240474,
        'pconn': 0.1,
        'post_name': 'olm',
        'pre_name': 'ivy',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': 0,
        'delay': 1.2,
        'gbarS': 1.150542157,
        'pconn': 0.5,
        'post_name': 'bis',
        'pre_name': 'ca3pyr',
        'tau_decay': 8.0,
        'tau_rise': 1.3},
    {   'Erev': 0,
        'delay': 1.2,
        'gbarS': 2.155417698,
        'pconn': 0.5,
        'post_name': 'bis',
        'pre_name': 'ca1pyr',
        'tau_decay': 8.0,
        'tau_rise': 1.3},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 2.88716469,
        'pconn': 0.1,
        'post_name': 'bis',
        'pre_name': 'pvbas',
        'tau_decay': 2.67,
        'tau_rise': 0.29},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.464067105,
        'pconn': 0.1,
        'post_name': 'bis',
        'pre_name': 'cckbas',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.461626916,
        'pconn': 0.1,
        'post_name': 'bis',
        'pre_name': 'bis',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'bis',
        'pre_name': 'ivy',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': 0.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'ivy',
        'pre_name': 'ca3pyr',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': 0,
        'delay': 1.2,
        'gbarS': 2.125086979,
        'pconn': 0.5,
        'post_name': 'ivy',
        'pre_name': 'ca1pyr',
        'tau_decay': 0.6,
        'tau_rise': 0.3},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 3.391835068,
        'pconn': 0.1,
        'post_name': 'ivy',
        'pre_name': 'pvbas',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.58994451,
        'pconn': 0.1,
        'post_name': 'ivy',
        'pre_name': 'cckbas',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': -75.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'ivy',
        'pre_name': 'bis',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.624924882,
        'pconn': 0.1,
        'post_name': 'ivy',
        'pre_name': 'ivy',
        'tau_decay': 4.0,
        'tau_rise': 0.5},
    {   'Erev': 0.0,
        'gbarS': 1,
        'pconn': 1,
        'post_name': 'ivy',
        'pre_name': 'ec3',
        'tau_decay': 5,
        'tau_rise': 2},
    {   'Erev': 0,
        'delay': 1.5,
        'gbarS': 1.650136928,
        'pconn': 0.5,
        'post_name': 'ngf',
        'pre_name': 'ca3pyr',
        'tau_decay': 3,
        'tau_rise': 0.5},
    {   'Erev': -75,
        'delay': 1.2,
        'gbarS': 1.588573475,
        'pconn': 0.1,
        'post_name': 'ngf',
        'pre_name': 'ivy',
        'tau_decay': 42,
        'tau_rise': 3.1}
]

##########################################
##### block of generators params #########
ca3pyr_params = {
    "name" : "ca3pyr",
    "R": 0.3,
    "freq": 7.0,
    "mean_spike_rate": 0.5, # 5, #
    "phase": 1.58,
}

ca1pyr_params = {
    "name" : "ca1pyr",
    "R": 0.2,
    "freq": 7.0,
    "mean_spike_rate": 0.5, # 5, #
    "phase": 3.14,
}

ec3_params = {
    "name" : "ec3",
    "R": 0.2,
    "freq": 7.0,
    "mean_spike_rate":  1.5, # 5, #
    "phase": -1.57,
}


########################################
##### block of neurons params #########
pvbas_params = {
    "name" : "pvbas",
    "neuron_class" : ctfeq.HH_Neuron,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0, #
    "sigma": 0.3,
    "ref_dvdt": 3.0,   # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params"  : [],

    "target" : {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 24, #20.0,
        "phase": 1.5707963267948966,
    },
}

cckbas_params = {
    "name" : "cckbas",
    "neuron_class": ctfeq.HH_Neuron,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 9.0, # 20.0,
        "phase": -1.5707963267948966,
    },
}

bis_params = {
    "name" : "bis",
    "neuron_class" : ctfeq.HH_Neuron,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 27.0, # 20.0,
        "phase": 3.141592653589793,
    },
}

aac_params = {
    "name" : "aac",
    "neuron_class": ctfeq.HH_Neuron,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 29.0, # 20.0,
        "phase": 0.0,
    },
}

ivy_params = {
    "name" : "ivy",
    "neuron_class": ctfeq.HH_Neuron,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 4.0, # 20.0,
        "phase": -1.5707963267948966,
    },
}

ngf_params = {
    "name" : "ngf",
    "neuron_class": ctfeq.HH_Neuron,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 8.0, #20.0,
        "phase": 0.0,
    },
}




olm_params = {
    "name": "olm",
    "neuron_class": ctfeq.HH_Neuron,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target": {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 30, #20.0,
        "phase": 3.14,
    },

}

params_net = {
"params_neurons" : [pvbas_params, olm_params, cckbas_params, bis_params, aac_params, ivy_params, ngf_params],
#"params_neurons" : [olm_params, ], # cckbas_params, ngf_params
"params_generators" : [ca3pyr_params, ca1pyr_params, ec3_params],
#"params_generators" : [ca1pyr_params, ],
"params_synapses" : synapses_params,
#"params_synapses" : [ca1pyr2olm, ],
}