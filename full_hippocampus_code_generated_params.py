import neuron_models
from copy import deepcopy

THETA_FREQ = 5 # Hz

##### block of neurons params #########
## DG neurons
DG_granule_soma_background_params = {
    "name": "DG_granule_soma_background",
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
    "Iext": 0.1,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 0.5,
        "phase": 1.3089969389957472,
    },
}

DG_granule_dend_background_params = {
    "name": "DG_granule_dend_background",
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
    "target": {},
}

DG_granule_soma_active1_params = {
    "name": "DG_granule_soma_active1",
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
    "Iext": 0.1,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target": {},
}

DG_granule_dend_active1_params = {
    "name": "DG_granule_dend_active1",
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
    "target": {},
}

DG_granule_soma_active2_params = {
    "name": "DG_granule_soma_active2",
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
    "target": {},
}

DG_granule_dend_active2_params = {
    "name": "DG_granule_dend_active2",
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
    "target": {},
}

DG_granule_soma_active3_params = {
    "name": "DG_granule_soma_active3",
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
    "target": {},
}

DG_granule_dend_active3_params = {
    "name": "DG_granule_dend_active3",
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
    "target": {},
}

DG_granule_soma_active4_params = {
    "name": "DG_granule_soma_active4",
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
    "target": {},
}

DG_granule_dend_active4_params = {
    "name": "DG_granule_dend_active4",
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
    "target": {},
}
DG_granule_soma_active5_params = {
    "name": "DG_granule_soma_active5",
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
    "target": {},
}

DG_granule_dend_active5_params = {
    "name": "DG_granule_dend_active5",
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
    "target": {},
}
##



DG_mossy_params = {
    "name" : "DG_mossy",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 1.0,
        "phase": 1.3089969389957472,
    },
}

DG_aac_params = {
    "name" : "DG_aac",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 30.0,
        "phase": -1.8325957145940457,
    },
}

DG_cckbas_params = {
    "name" : "DG_cckbas",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 9.0,
        "phase": 2.8797932657906435,
    },
}

DG_pvbas_params = {
    "name" : "DG_pvbas",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 24.0,
        "phase": 0,
    },
}
#########################
# CA3 neurons
CA3_pyr_soma_background_params = {
    "name": "CA3_pyr_soma_background",
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
    "Iext": 0.1,
    "N": 400,
    "dts": 0.5,
    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 0.5,
        "phase": 1.58,
    },
}

CA3_pyr_dend_background_params = {
    "name": "CA3_pyr_dend_background",
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
    "target": {},
}


CA3_pyr_soma_active1_params = {
    "name": "CA3_pyr_soma_active1",
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
    "target": {},
}

CA3_pyr_dend_active1_params = {
    "name": "CA3_pyr_dend_active1",
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
    "target": {},
}

CA3_pyr_soma_active2_params = {
    "name": "CA3_pyr_soma_active2",
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
    "target": {},
}

CA3_pyr_dend_active2_params = {
    "name": "CA3_pyr_dend_active2",
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
    "target": {},
}

CA3_pyr_soma_active3_params = {
    "name": "CA3_pyr_soma_active3",
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
    "target": {},
}

CA3_pyr_dend_active3_params = {
    "name": "CA3_pyr_dend_active3",
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
    "target": {},
}

CA3_pyr_soma_active4_params = {
    "name": "CA3_pyr_soma_active4",
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
    "target": {},
}

CA3_pyr_dend_active4_params = {
    "name": "CA3_pyr_dend_active4",
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
    "target": {},
}

CA3_pyr_soma_active5_params = {
    "name": "CA3_pyr_soma_active5",
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
    "target": {},
}

CA3_pyr_dend_active5_params = {
    "name": "CA3_pyr_dend_active5",
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
    "target": {},
}

CA3_aac_params = {
    "name" : "CA3_aac",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 29.0,
        "phase": -1.561592653589793,
    },
}

CA3_cckbas_params = {
    "name" : "CA3_cckbas",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 9.0,
        "phase": -3.1323889803846896,
    },

}

CA3_pvbas_params = {
    "name" : "CA3_pvbas",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],

    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 24.0,
        "phase": 0.0,
    },
}

CA3_olm_params = {
    "name" : "CA3_olm",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 30.0,
        "phase": 1.58,
    },
}
###################################################################
### CA1 neurons
CA1_pyr_soma_background_params = {
    "name": "CA1_pyr_soma_background",
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
    "Iext": 0.1,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": THETA_FREQ,
        "mean_spike_rate": 0.5,
        "phase": 3.141592653589793,
    },
}

CA1_pyr_dend_background_params = {
    "name": "CA1_pyr_dend_background",
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
    "target": {},
}


CA1_pyr_soma_active1_params = {
    "name": "CA1_pyr_soma_active1",
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
    "target": {},
}

CA1_pyr_dend_active1_params = {
    "name": "CA1_pyr_dend_active1",
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
    "target": {},
}

CA1_pyr_soma_active2_params = {
    "name": "CA1_pyr_soma_active2",
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
    "target": {},
}

CA1_pyr_dend_active2_params = {
    "name": "CA1_pyr_dend_active2",
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
    "target": {},
}

CA1_pyr_soma_active3_params = {
    "name": "CA1_pyr_soma_active3",
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
    "target": {},
}

CA1_pyr_dend_active3_params = {
    "name": "CA1_pyr_dend_active3",
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
    "target": {},
}

CA1_pyr_soma_active4_params = {
    "name": "CA1_pyr_soma_active4",
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
    "target": {},
}

CA1_pyr_dend_active4_params = {
    "name": "CA1_pyr_dend_active4",
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
    "target": {},
}

CA1_pyr_soma_active5_params = {
    "name": "CA1_pyr_soma_active5",
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
    "target": {},
}

CA1_pyr_dend_active5_params = {
    "name": "CA1_pyr_dend_active5",
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
    "target": {},
}

CA1_aac_params = {
    "name" : "CA1_aac",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 0.0,
    },
}

CA1_cckbas_params = {
    "name" : "CA1_cckbas",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": -1.5707963267948966,
    },
}

CA1_pvbas_params = {
    "name" : "CA1_pvbas",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 1.5707963267948966,
    },
}

CA1_olm_params = {
    "name" : "CA1_olm",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 3.14,
    },
}

CA1_bis_params = {
    "name" : "CA1_bis",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 3.141592653589793,
    },
}

CA1_ivy_params = {
    "name" : "CA1_ivy",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": -1.5707963267948966,
    },
}
CA1_ngf_params = {
    "name" : "CA1_ngf",
    "neuron_class" : neuron_models.LIFCompartment,
    "is_sim_rho": True,
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
    "channels_params": [],
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 0.0,
    },
}

########################################################################
################# block of synapses params #############################
DG_mossy_2_DG_granule_soma_backgrond = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_granule_soma_backgrond",
    "tau_f": 20.22414499,
    "tau_r": 166.1624932,
    "tau_d": 5.357017163,
    "Uinc": 0.304520719,
    "gbarS": 2.394273388,
    "Erev": 0.0,
}
DG_mossy_2_DG_granule_soma_active1 = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_granule_soma_active1",
    "tau_f": 20.22414499,
    "tau_r": 166.1624932,
    "tau_d": 5.357017163,
    "Uinc": 0.304520719,
    "gbarS": 2.394273388,
    "Erev": 0.0,
}
DG_mossy_2_DG_granule_soma_active2 = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_granule_soma_active2",
    "tau_f": 20.22414499,
    "tau_r": 166.1624932,
    "tau_d": 5.357017163,
    "Uinc": 0.304520719,
    "gbarS": 2.394273388,
    "Erev": 0.0,
}
DG_mossy_2_DG_granule_soma_active3 = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_granule_soma_active3",
    "tau_f": 20.22414499,
    "tau_r": 166.1624932,
    "tau_d": 5.357017163,
    "Uinc": 0.304520719,
    "gbarS": 2.394273388,
    "Erev": 0.0,
}
DG_mossy_2_DG_granule_soma_active4 = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_granule_soma_active4",
    "tau_f": 20.22414499,
    "tau_r": 166.1624932,
    "tau_d": 5.357017163,
    "Uinc": 0.304520719,
    "gbarS": 2.394273388,
    "Erev": 0.0,
}
DG_mossy_2_DG_granule_soma_active5 = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_granule_soma_active5",
    "tau_f": 20.22414499,
    "tau_r": 166.1624932,
    "tau_d": 5.357017163,
    "Uinc": 0.304520719,
    "gbarS": 2.394273388,
    "Erev": 0.0,
}
EC2_stellate_2_DG_granule_dend_backgrond = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_granule_dend_backgrond",
    "tau_f": 18.71381627,
    "tau_r": 266.2388325,
    "tau_d": 5.333183152,
    "Uinc": 0.269729804,
    "gbarS": 1.824629341,
    "Erev": 0.0,
}
EC2_stellate_2_DG_granule_dend_active1 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_granule_dend_active1",
    "tau_f": 18.71381627,
    "tau_r": 266.2388325,
    "tau_d": 5.333183152,
    "Uinc": 0.269729804,
    "gbarS": 1.824629341,
    "Erev": 0.0,
}
EC2_stellate_2_DG_granule_dend_active2 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_granule_dend_active2",
    "tau_f": 18.71381627,
    "tau_r": 266.2388325,
    "tau_d": 5.333183152,
    "Uinc": 0.269729804,
    "gbarS": 1.824629341,
    "Erev": 0.0,
}
EC2_stellate_2_DG_granule_dend_active3 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_granule_dend_active3",
    "tau_f": 18.71381627,
    "tau_r": 266.2388325,
    "tau_d": 5.333183152,
    "Uinc": 0.269729804,
    "gbarS": 1.824629341,
    "Erev": 0.0,
}
EC2_stellate_2_DG_granule_dend_active4 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_granule_dend_active4",
    "tau_f": 18.71381627,
    "tau_r": 266.2388325,
    "tau_d": 5.333183152,
    "Uinc": 0.269729804,
    "gbarS": 1.824629341,
    "Erev": 0.0,
}
EC2_stellate_2_DG_granule_dend_active5 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_granule_dend_active5",
    "tau_f": 18.71381627,
    "tau_r": 266.2388325,
    "tau_d": 5.333183152,
    "Uinc": 0.269729804,
    "gbarS": 1.824629341,
    "Erev": 0.0,
}
DG_aac_2_DG_granule_soma_backgrond = {
    "w": 0.1,
    "pre_name": "DG_aac",
    "post_name": "DG_granule_soma_backgrond",
    "tau_f": 7.207859274,
    "tau_r": 532.2251779,
    "tau_d": 4.275954375,
    "Uinc": 0.302243658,
    "gbarS": 3.993398634,
    "Erev": -75.0,
}
DG_aac_2_DG_granule_soma_active1 = {
    "w": 0.1,
    "pre_name": "DG_aac",
    "post_name": "DG_granule_soma_active1",
    "tau_f": 7.207859274,
    "tau_r": 532.2251779,
    "tau_d": 4.275954375,
    "Uinc": 0.302243658,
    "gbarS": 3.993398634,
    "Erev": -75.0,
}
DG_aac_2_DG_granule_soma_active2 = {
    "w": 0.1,
    "pre_name": "DG_aac",
    "post_name": "DG_granule_soma_active2",
    "tau_f": 7.207859274,
    "tau_r": 532.2251779,
    "tau_d": 4.275954375,
    "Uinc": 0.302243658,
    "gbarS": 3.993398634,
    "Erev": -75.0,
}
DG_aac_2_DG_granule_soma_active3 = {
    "w": 0.1,
    "pre_name": "DG_aac",
    "post_name": "DG_granule_soma_active3",
    "tau_f": 7.207859274,
    "tau_r": 532.2251779,
    "tau_d": 4.275954375,
    "Uinc": 0.302243658,
    "gbarS": 3.993398634,
    "Erev": -75.0,
}
DG_aac_2_DG_granule_soma_active4 = {
    "w": 0.1,
    "pre_name": "DG_aac",
    "post_name": "DG_granule_soma_active4",
    "tau_f": 7.207859274,
    "tau_r": 532.2251779,
    "tau_d": 4.275954375,
    "Uinc": 0.302243658,
    "gbarS": 3.993398634,
    "Erev": -75.0,
}
DG_aac_2_DG_granule_soma_active5 = {
    "w": 0.1,
    "pre_name": "DG_aac",
    "post_name": "DG_granule_soma_active5",
    "tau_f": 7.207859274,
    "tau_r": 532.2251779,
    "tau_d": 4.275954375,
    "Uinc": 0.302243658,
    "gbarS": 3.993398634,
    "Erev": -75.0,
}
DG_pvbas_2_DG_granule_soma_backgrond = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_granule_soma_backgrond",
    "tau_f": 6.347428119,
    "tau_r": 433.8757913,
    "tau_d": 6.543457785,
    "Uinc": 0.331971356,
    "gbarS": 2.450937388,
    "Erev": -75.0,
}
DG_pvbas_2_DG_granule_soma_active1 = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_granule_soma_active1",
    "tau_f": 6.347428119,
    "tau_r": 433.8757913,
    "tau_d": 6.543457785,
    "Uinc": 0.331971356,
    "gbarS": 2.450937388,
    "Erev": -75.0,
}
DG_pvbas_2_DG_granule_soma_active2 = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_granule_soma_active2",
    "tau_f": 6.347428119,
    "tau_r": 433.8757913,
    "tau_d": 6.543457785,
    "Uinc": 0.331971356,
    "gbarS": 2.450937388,
    "Erev": -75.0,
}
DG_pvbas_2_DG_granule_soma_active3 = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_granule_soma_active3",
    "tau_f": 6.347428119,
    "tau_r": 433.8757913,
    "tau_d": 6.543457785,
    "Uinc": 0.331971356,
    "gbarS": 2.450937388,
    "Erev": -75.0,
}
DG_pvbas_2_DG_granule_soma_active4 = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_granule_soma_active4",
    "tau_f": 6.347428119,
    "tau_r": 433.8757913,
    "tau_d": 6.543457785,
    "Uinc": 0.331971356,
    "gbarS": 2.450937388,
    "Erev": -75.0,
}
DG_pvbas_2_DG_granule_soma_active5 = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_granule_soma_active5",
    "tau_f": 6.347428119,
    "tau_r": 433.8757913,
    "tau_d": 6.543457785,
    "Uinc": 0.331971356,
    "gbarS": 2.450937388,
    "Erev": -75.0,
}
DG_cckbas_2_DG_granule_soma_backgrond = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_granule_soma_backgrond",
    "tau_f": 7.799352565,
    "tau_r": 720.4611399,
    "tau_d": 9.162057501,
    "Uinc": 0.290305224,
    "gbarS": 1.325092735,
    "Erev": -75.0,
}
DG_cckbas_2_DG_granule_soma_active1 = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_granule_soma_active1",
    "tau_f": 7.799352565,
    "tau_r": 720.4611399,
    "tau_d": 9.162057501,
    "Uinc": 0.290305224,
    "gbarS": 1.325092735,
    "Erev": -75.0,
}
DG_cckbas_2_DG_granule_soma_active2 = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_granule_soma_active2",
    "tau_f": 7.799352565,
    "tau_r": 720.4611399,
    "tau_d": 9.162057501,
    "Uinc": 0.290305224,
    "gbarS": 1.325092735,
    "Erev": -75.0,
}
DG_cckbas_2_DG_granule_soma_active3 = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_granule_soma_active3",
    "tau_f": 7.799352565,
    "tau_r": 720.4611399,
    "tau_d": 9.162057501,
    "Uinc": 0.290305224,
    "gbarS": 1.325092735,
    "Erev": -75.0,
}
DG_cckbas_2_DG_granule_soma_active4 = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_granule_soma_active4",
    "tau_f": 7.799352565,
    "tau_r": 720.4611399,
    "tau_d": 9.162057501,
    "Uinc": 0.290305224,
    "gbarS": 1.325092735,
    "Erev": -75.0,
}
DG_cckbas_2_DG_granule_soma_active5 = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_granule_soma_active5",
    "tau_f": 7.799352565,
    "tau_r": 720.4611399,
    "tau_d": 9.162057501,
    "Uinc": 0.290305224,
    "gbarS": 1.325092735,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_DG_mossy = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "DG_mossy",
    "tau_f": 73.47908526,
    "tau_r": 428.5825544,
    "tau_d": 5.346932748,
    "Uinc": 0.151268414,
    "gbarS": 1.713023104,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_DG_mossy = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "DG_mossy",
    "tau_f": 73.47908526,
    "tau_r": 428.5825544,
    "tau_d": 5.346932748,
    "Uinc": 0.151268414,
    "gbarS": 1.713023104,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_DG_mossy = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "DG_mossy",
    "tau_f": 73.47908526,
    "tau_r": 428.5825544,
    "tau_d": 5.346932748,
    "Uinc": 0.151268414,
    "gbarS": 1.713023104,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_DG_mossy = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "DG_mossy",
    "tau_f": 73.47908526,
    "tau_r": 428.5825544,
    "tau_d": 5.346932748,
    "Uinc": 0.151268414,
    "gbarS": 1.713023104,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_DG_mossy = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "DG_mossy",
    "tau_f": 73.47908526,
    "tau_r": 428.5825544,
    "tau_d": 5.346932748,
    "Uinc": 0.151268414,
    "gbarS": 1.713023104,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_DG_mossy = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "DG_mossy",
    "tau_f": 73.47908526,
    "tau_r": 428.5825544,
    "tau_d": 5.346932748,
    "Uinc": 0.151268414,
    "gbarS": 1.713023104,
    "Erev": 0.0,
}
DG_mossy_2_DG_mossy = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_mossy",
    "tau_f": 71.64176434,
    "tau_r": 249.3294154,
    "tau_d": 4.257146466,
    "Uinc": 0.24460315,
    "gbarS": 2.067500893,
    "Erev": 0.0,
}
DG_aac_2_DG_mossy = {
    "w": 0.1,
    "pre_name": "DG_aac",
    "post_name": "DG_mossy",
    "tau_f": 20.21329933,
    "tau_r": 564.6371763,
    "tau_d": 4.312123649,
    "Uinc": 0.239970558,
    "gbarS": 2.800891905,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_DG_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "DG_aac",
    "tau_f": 63.20216278,
    "tau_r": 380.2380559,
    "tau_d": 5.130446879,
    "Uinc": 0.159623933,
    "gbarS": 1.58930527,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_DG_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "DG_aac",
    "tau_f": 63.20216278,
    "tau_r": 380.2380559,
    "tau_d": 5.130446879,
    "Uinc": 0.159623933,
    "gbarS": 1.58930527,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_DG_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "DG_aac",
    "tau_f": 63.20216278,
    "tau_r": 380.2380559,
    "tau_d": 5.130446879,
    "Uinc": 0.159623933,
    "gbarS": 1.58930527,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_DG_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "DG_aac",
    "tau_f": 63.20216278,
    "tau_r": 380.2380559,
    "tau_d": 5.130446879,
    "Uinc": 0.159623933,
    "gbarS": 1.58930527,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_DG_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "DG_aac",
    "tau_f": 63.20216278,
    "tau_r": 380.2380559,
    "tau_d": 5.130446879,
    "Uinc": 0.159623933,
    "gbarS": 1.58930527,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_DG_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "DG_aac",
    "tau_f": 63.20216278,
    "tau_r": 380.2380559,
    "tau_d": 5.130446879,
    "Uinc": 0.159623933,
    "gbarS": 1.58930527,
    "Erev": 0.0,
}
DG_mossy_2_DG_aac = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_aac",
    "tau_f": 76.01492823,
    "tau_r": 234.8042342,
    "tau_d": 4.065015021,
    "Uinc": 0.205689442,
    "gbarS": 2.068097096,
    "Erev": 0.0,
}
EC2_stellate_2_DG_aac = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_aac",
    "tau_f": 54.18080298,
    "tau_r": 285.5781328,
    "tau_d": 4.490819231,
    "Uinc": 0.182637823,
    "gbarS": 1.463541884,
    "Erev": 0.0,
}
DG_pvbas_2_DG_aac = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_aac",
    "tau_f": 8.941005694,
    "tau_r": 424.650686,
    "tau_d": 5.78494089,
    "Uinc": 0.252012918,
    "gbarS": 1.868477305,
    "Erev": -75.0,
}
DG_cckbas_2_DG_aac = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_aac",
    "tau_f": 15.81592861,
    "tau_r": 695.3628193,
    "tau_d": 7.243794134,
    "Uinc": 0.207843846,
    "gbarS": 1.427888246,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "DG_pvbas",
    "tau_f": 62.27805375,
    "tau_r": 151.2652578,
    "tau_d": 3.566153577,
    "Uinc": 0.196866987,
    "gbarS": 1.457495181,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "DG_pvbas",
    "tau_f": 62.27805375,
    "tau_r": 151.2652578,
    "tau_d": 3.566153577,
    "Uinc": 0.196866987,
    "gbarS": 1.457495181,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "DG_pvbas",
    "tau_f": 62.27805375,
    "tau_r": 151.2652578,
    "tau_d": 3.566153577,
    "Uinc": 0.196866987,
    "gbarS": 1.457495181,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "DG_pvbas",
    "tau_f": 62.27805375,
    "tau_r": 151.2652578,
    "tau_d": 3.566153577,
    "Uinc": 0.196866987,
    "gbarS": 1.457495181,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "DG_pvbas",
    "tau_f": 62.27805375,
    "tau_r": 151.2652578,
    "tau_d": 3.566153577,
    "Uinc": 0.196866987,
    "gbarS": 1.457495181,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "DG_pvbas",
    "tau_f": 62.27805375,
    "tau_r": 151.2652578,
    "tau_d": 3.566153577,
    "Uinc": 0.196866987,
    "gbarS": 1.457495181,
    "Erev": 0.0,
}
DG_mossy_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_pvbas",
    "tau_f": 69.31635444,
    "tau_r": 117.3653589,
    "tau_d": 3.395481676,
    "Uinc": 0.254508981,
    "gbarS": 1.995595549,
    "Erev": 0.0,
}
EC2_stellate_2_DG_pvbas = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_pvbas",
    "tau_f": 48.20006034,
    "tau_r": 144.4151725,
    "tau_d": 3.84947857,
    "Uinc": 0.213713686,
    "gbarS": 1.405758038,
    "Erev": 0.0,
}
DG_pvbas_2_DG_pvbas = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_pvbas",
    "tau_f": 7.44050779,
    "tau_r": 195.536072,
    "tau_d": 4.648072617,
    "Uinc": 0.309539318,
    "gbarS": 1.981409966,
    "Erev": -75.0,
}
DG_cckbas_2_DG_pvbas = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_pvbas",
    "tau_f": 11.45264621,
    "tau_r": 488.7789045,
    "tau_d": 6.292733699,
    "Uinc": 0.245051562,
    "gbarS": 1.570787778,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "DG_cckbas",
    "tau_f": 45.85426413,
    "tau_r": 500.5378384,
    "tau_d": 4.099285316,
    "Uinc": 0.195845379,
    "gbarS": 1.596171304,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "DG_cckbas",
    "tau_f": 45.85426413,
    "tau_r": 500.5378384,
    "tau_d": 4.099285316,
    "Uinc": 0.195845379,
    "gbarS": 1.596171304,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "DG_cckbas",
    "tau_f": 45.85426413,
    "tau_r": 500.5378384,
    "tau_d": 4.099285316,
    "Uinc": 0.195845379,
    "gbarS": 1.596171304,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "DG_cckbas",
    "tau_f": 45.85426413,
    "tau_r": 500.5378384,
    "tau_d": 4.099285316,
    "Uinc": 0.195845379,
    "gbarS": 1.596171304,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "DG_cckbas",
    "tau_f": 45.85426413,
    "tau_r": 500.5378384,
    "tau_d": 4.099285316,
    "Uinc": 0.195845379,
    "gbarS": 1.596171304,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "DG_cckbas",
    "tau_f": 45.85426413,
    "tau_r": 500.5378384,
    "tau_d": 4.099285316,
    "Uinc": 0.195845379,
    "gbarS": 1.596171304,
    "Erev": 0.0,
}
DG_mossy_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "DG_mossy",
    "post_name": "DG_cckbas",
    "tau_f": 63.78934339,
    "tau_r": 279.1407549,
    "tau_d": 4.504103823,
    "Uinc": 0.219156366,
    "gbarS": 1.544328401,
    "Erev": 0.0,
}
EC2_stellate_2_DG_cckbas = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "DG_cckbas",
    "tau_f": 43.72393768,
    "tau_r": 398.9853785,
    "tau_d": 4.548332535,
    "Uinc": 0.189213122,
    "gbarS": 1.203566354,
    "Erev": 0.0,
}
DG_pvbas_2_DG_cckbas = {
    "w": 0.1,
    "pre_name": "DG_pvbas",
    "post_name": "DG_cckbas",
    "tau_f": 8.531364444,
    "tau_r": 514.9536093,
    "tau_d": 6.463885991,
    "Uinc": 0.265266488,
    "gbarS": 1.55036801,
    "Erev": -75.0,
}
DG_cckbas_2_DG_cckbas = {
    "w": 0.1,
    "pre_name": "DG_cckbas",
    "post_name": "DG_cckbas",
    "tau_f": 14.24748768,
    "tau_r": 680.14242,
    "tau_d": 7.579118517,
    "Uinc": 0.197308499,
    "gbarS": 1.14109394,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_backgrond_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_backgrond_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_backgrond_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_backgrond_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_backgrond_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 78.58373418,
    "tau_r": 278.2857573,
    "tau_d": 6.657226902,
    "Uinc": 0.155284008,
    "gbarS": 1.384236627,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 27.51301394,
    "tau_r": 278.2582848,
    "tau_d": 9.515857529,
    "Uinc": 0.172423074,
    "gbarS": 0.603001931,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_pyr_dend_backgrond = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_pyr_dend_backgrond",
    "tau_f": 53.4779854,
    "tau_r": 258.3175848,
    "tau_d": 6.549624289,
    "Uinc": 0.184049794,
    "gbarS": 1.065020816,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_pyr_dend_active1 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_pyr_dend_active1",
    "tau_f": 53.4779854,
    "tau_r": 258.3175848,
    "tau_d": 6.549624289,
    "Uinc": 0.184049794,
    "gbarS": 1.065020816,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_pyr_dend_active2 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_pyr_dend_active2",
    "tau_f": 53.4779854,
    "tau_r": 258.3175848,
    "tau_d": 6.549624289,
    "Uinc": 0.184049794,
    "gbarS": 1.065020816,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_pyr_dend_active3 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_pyr_dend_active3",
    "tau_f": 53.4779854,
    "tau_r": 258.3175848,
    "tau_d": 6.549624289,
    "Uinc": 0.184049794,
    "gbarS": 1.065020816,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_pyr_dend_active4 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_pyr_dend_active4",
    "tau_f": 53.4779854,
    "tau_r": 258.3175848,
    "tau_d": 6.549624289,
    "Uinc": 0.184049794,
    "gbarS": 1.065020816,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_pyr_dend_active5 = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_pyr_dend_active5",
    "tau_f": 53.4779854,
    "tau_r": 258.3175848,
    "tau_d": 6.549624289,
    "Uinc": 0.184049794,
    "gbarS": 1.065020816,
    "Erev": 0.0,
}
CA3_aac_2_CA3_pyr_soma_backgrond = {
    "w": 0.1,
    "pre_name": "CA3_aac",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 16.57488328,
    "tau_r": 406.9544736,
    "tau_d": 7.702247407,
    "Uinc": 0.213532699,
    "gbarS": 1.808161849,
    "Erev": -75.0,
}
CA3_aac_2_CA3_pyr_soma_active1 = {
    "w": 0.1,
    "pre_name": "CA3_aac",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 16.57488328,
    "tau_r": 406.9544736,
    "tau_d": 7.702247407,
    "Uinc": 0.213532699,
    "gbarS": 1.808161849,
    "Erev": -75.0,
}
CA3_aac_2_CA3_pyr_soma_active2 = {
    "w": 0.1,
    "pre_name": "CA3_aac",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 16.57488328,
    "tau_r": 406.9544736,
    "tau_d": 7.702247407,
    "Uinc": 0.213532699,
    "gbarS": 1.808161849,
    "Erev": -75.0,
}
CA3_aac_2_CA3_pyr_soma_active3 = {
    "w": 0.1,
    "pre_name": "CA3_aac",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 16.57488328,
    "tau_r": 406.9544736,
    "tau_d": 7.702247407,
    "Uinc": 0.213532699,
    "gbarS": 1.808161849,
    "Erev": -75.0,
}
CA3_aac_2_CA3_pyr_soma_active4 = {
    "w": 0.1,
    "pre_name": "CA3_aac",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 16.57488328,
    "tau_r": 406.9544736,
    "tau_d": 7.702247407,
    "Uinc": 0.213532699,
    "gbarS": 1.808161849,
    "Erev": -75.0,
}
CA3_aac_2_CA3_pyr_soma_active5 = {
    "w": 0.1,
    "pre_name": "CA3_aac",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 16.57488328,
    "tau_r": 406.9544736,
    "tau_d": 7.702247407,
    "Uinc": 0.213532699,
    "gbarS": 1.808161849,
    "Erev": -75.0,
}
CA3_pvbas_2_CA3_pyr_soma_backgrond = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 20.6296542,
    "tau_r": 416.2817167,
    "tau_d": 7.792679312,
    "Uinc": 0.202850296,
    "gbarS": 1.462245456,
    "Erev": -75.0,
}
CA3_pvbas_2_CA3_pyr_soma_active1 = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 20.6296542,
    "tau_r": 416.2817167,
    "tau_d": 7.792679312,
    "Uinc": 0.202850296,
    "gbarS": 1.462245456,
    "Erev": -75.0,
}
CA3_pvbas_2_CA3_pyr_soma_active2 = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 20.6296542,
    "tau_r": 416.2817167,
    "tau_d": 7.792679312,
    "Uinc": 0.202850296,
    "gbarS": 1.462245456,
    "Erev": -75.0,
}
CA3_pvbas_2_CA3_pyr_soma_active3 = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 20.6296542,
    "tau_r": 416.2817167,
    "tau_d": 7.792679312,
    "Uinc": 0.202850296,
    "gbarS": 1.462245456,
    "Erev": -75.0,
}
CA3_pvbas_2_CA3_pyr_soma_active4 = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 20.6296542,
    "tau_r": 416.2817167,
    "tau_d": 7.792679312,
    "Uinc": 0.202850296,
    "gbarS": 1.462245456,
    "Erev": -75.0,
}
CA3_pvbas_2_CA3_pyr_soma_active5 = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 20.6296542,
    "tau_r": 416.2817167,
    "tau_d": 7.792679312,
    "Uinc": 0.202850296,
    "gbarS": 1.462245456,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_pyr_soma_backgrond = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_pyr_soma_backgrond",
    "tau_f": 14.22931029,
    "tau_r": 486.8334149,
    "tau_d": 8.653427988,
    "Uinc": 0.160380461,
    "gbarS": 1.241875378,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_pyr_soma_active1 = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_pyr_soma_active1",
    "tau_f": 14.22931029,
    "tau_r": 486.8334149,
    "tau_d": 8.653427988,
    "Uinc": 0.160380461,
    "gbarS": 1.241875378,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_pyr_soma_active2 = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_pyr_soma_active2",
    "tau_f": 14.22931029,
    "tau_r": 486.8334149,
    "tau_d": 8.653427988,
    "Uinc": 0.160380461,
    "gbarS": 1.241875378,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_pyr_soma_active3 = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_pyr_soma_active3",
    "tau_f": 14.22931029,
    "tau_r": 486.8334149,
    "tau_d": 8.653427988,
    "Uinc": 0.160380461,
    "gbarS": 1.241875378,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_pyr_soma_active4 = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_pyr_soma_active4",
    "tau_f": 14.22931029,
    "tau_r": 486.8334149,
    "tau_d": 8.653427988,
    "Uinc": 0.160380461,
    "gbarS": 1.241875378,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_pyr_soma_active5 = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_pyr_soma_active5",
    "tau_f": 14.22931029,
    "tau_r": 486.8334149,
    "tau_d": 8.653427988,
    "Uinc": 0.160380461,
    "gbarS": 1.241875378,
    "Erev": -75.0,
}
CA3_olm_2_CA3_pyr_dend_backgrond = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_pyr_dend_backgrond",
    "tau_f": 24.98828861,
    "tau_r": 477.7854118,
    "tau_d": 8.461853504,
    "Uinc": 0.195020367,
    "gbarS": 1.434237945,
    "Erev": -75.0,
}
CA3_olm_2_CA3_pyr_dend_active1 = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_pyr_dend_active1",
    "tau_f": 24.98828861,
    "tau_r": 477.7854118,
    "tau_d": 8.461853504,
    "Uinc": 0.195020367,
    "gbarS": 1.434237945,
    "Erev": -75.0,
}
CA3_olm_2_CA3_pyr_dend_active2 = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_pyr_dend_active2",
    "tau_f": 24.98828861,
    "tau_r": 477.7854118,
    "tau_d": 8.461853504,
    "Uinc": 0.195020367,
    "gbarS": 1.434237945,
    "Erev": -75.0,
}
CA3_olm_2_CA3_pyr_dend_active3 = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_pyr_dend_active3",
    "tau_f": 24.98828861,
    "tau_r": 477.7854118,
    "tau_d": 8.461853504,
    "Uinc": 0.195020367,
    "gbarS": 1.434237945,
    "Erev": -75.0,
}
CA3_olm_2_CA3_pyr_dend_active4 = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_pyr_dend_active4",
    "tau_f": 24.98828861,
    "tau_r": 477.7854118,
    "tau_d": 8.461853504,
    "Uinc": 0.195020367,
    "gbarS": 1.434237945,
    "Erev": -75.0,
}
CA3_olm_2_CA3_pyr_dend_active5 = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_pyr_dend_active5",
    "tau_f": 24.98828861,
    "tau_r": 477.7854118,
    "tau_d": 8.461853504,
    "Uinc": 0.195020367,
    "gbarS": 1.434237945,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_aac",
    "tau_f": 51.84326359,
    "tau_r": 470.2612852,
    "tau_d": 4.35002076,
    "Uinc": 0.164066878,
    "gbarS": 1.474575661,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_aac",
    "tau_f": 51.84326359,
    "tau_r": 470.2612852,
    "tau_d": 4.35002076,
    "Uinc": 0.164066878,
    "gbarS": 1.474575661,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_aac",
    "tau_f": 51.84326359,
    "tau_r": 470.2612852,
    "tau_d": 4.35002076,
    "Uinc": 0.164066878,
    "gbarS": 1.474575661,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_aac",
    "tau_f": 51.84326359,
    "tau_r": 470.2612852,
    "tau_d": 4.35002076,
    "Uinc": 0.164066878,
    "gbarS": 1.474575661,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_aac",
    "tau_f": 51.84326359,
    "tau_r": 470.2612852,
    "tau_d": 4.35002076,
    "Uinc": 0.164066878,
    "gbarS": 1.474575661,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_aac",
    "tau_f": 51.84326359,
    "tau_r": 470.2612852,
    "tau_d": 4.35002076,
    "Uinc": 0.164066878,
    "gbarS": 1.474575661,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_aac",
    "tau_f": 29.08398524,
    "tau_r": 464.5912674,
    "tau_d": 5.411203675,
    "Uinc": 0.167122777,
    "gbarS": 0.999041918,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_aac",
    "tau_f": 29.08398524,
    "tau_r": 464.5912674,
    "tau_d": 5.411203675,
    "Uinc": 0.167122777,
    "gbarS": 0.999041918,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_aac",
    "tau_f": 29.08398524,
    "tau_r": 464.5912674,
    "tau_d": 5.411203675,
    "Uinc": 0.167122777,
    "gbarS": 0.999041918,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_aac",
    "tau_f": 29.08398524,
    "tau_r": 464.5912674,
    "tau_d": 5.411203675,
    "Uinc": 0.167122777,
    "gbarS": 0.999041918,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_aac",
    "tau_f": 29.08398524,
    "tau_r": 464.5912674,
    "tau_d": 5.411203675,
    "Uinc": 0.167122777,
    "gbarS": 0.999041918,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_aac",
    "tau_f": 29.08398524,
    "tau_r": 464.5912674,
    "tau_d": 5.411203675,
    "Uinc": 0.167122777,
    "gbarS": 0.999041918,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_aac = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_aac",
    "tau_f": 42.99023833,
    "tau_r": 401.1602956,
    "tau_d": 4.079683594,
    "Uinc": 0.194570293,
    "gbarS": 1.370295781,
    "Erev": 0.0,
}
CA3_pvbas_2_CA3_aac = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_aac",
    "tau_f": 24.87448902,
    "tau_r": 619.6314584,
    "tau_d": 4.864726664,
    "Uinc": 0.222182231,
    "gbarS": 1.847448993,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_aac = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_aac",
    "tau_f": 17.86013123,
    "tau_r": 539.3344072,
    "tau_d": 6.078168225,
    "Uinc": 0.182228434,
    "gbarS": 1.461545183,
    "Erev": -75.0,
}
CA3_olm_2_CA3_aac = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_aac",
    "tau_f": 22.1333446,
    "tau_r": 605.8697535,
    "tau_d": 5.99254613,
    "Uinc": 0.208463581,
    "gbarS": 1.643330395,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_pvbas",
    "tau_f": 43.27421385,
    "tau_r": 518.9344311,
    "tau_d": 3.914660888,
    "Uinc": 0.175572102,
    "gbarS": 1.624518558,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_pvbas",
    "tau_f": 43.27421385,
    "tau_r": 518.9344311,
    "tau_d": 3.914660888,
    "Uinc": 0.175572102,
    "gbarS": 1.624518558,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_pvbas",
    "tau_f": 43.27421385,
    "tau_r": 518.9344311,
    "tau_d": 3.914660888,
    "Uinc": 0.175572102,
    "gbarS": 1.624518558,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_pvbas",
    "tau_f": 43.27421385,
    "tau_r": 518.9344311,
    "tau_d": 3.914660888,
    "Uinc": 0.175572102,
    "gbarS": 1.624518558,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_pvbas",
    "tau_f": 43.27421385,
    "tau_r": 518.9344311,
    "tau_d": 3.914660888,
    "Uinc": 0.175572102,
    "gbarS": 1.624518558,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_pvbas",
    "tau_f": 43.27421385,
    "tau_r": 518.9344311,
    "tau_d": 3.914660888,
    "Uinc": 0.175572102,
    "gbarS": 1.624518558,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_pvbas",
    "tau_f": 23.32103636,
    "tau_r": 525.604511,
    "tau_d": 4.525332112,
    "Uinc": 0.188975506,
    "gbarS": 1.24735956,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_pvbas",
    "tau_f": 23.32103636,
    "tau_r": 525.604511,
    "tau_d": 4.525332112,
    "Uinc": 0.188975506,
    "gbarS": 1.24735956,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_pvbas",
    "tau_f": 23.32103636,
    "tau_r": 525.604511,
    "tau_d": 4.525332112,
    "Uinc": 0.188975506,
    "gbarS": 1.24735956,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_pvbas",
    "tau_f": 23.32103636,
    "tau_r": 525.604511,
    "tau_d": 4.525332112,
    "Uinc": 0.188975506,
    "gbarS": 1.24735956,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_pvbas",
    "tau_f": 23.32103636,
    "tau_r": 525.604511,
    "tau_d": 4.525332112,
    "Uinc": 0.188975506,
    "gbarS": 1.24735956,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_pvbas",
    "tau_f": 23.32103636,
    "tau_r": 525.604511,
    "tau_d": 4.525332112,
    "Uinc": 0.188975506,
    "gbarS": 1.24735956,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_pvbas = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_pvbas",
    "tau_f": 35.90374421,
    "tau_r": 457.467604,
    "tau_d": 3.602130695,
    "Uinc": 0.209590373,
    "gbarS": 1.556070386,
    "Erev": 0.0,
}
CA3_pvbas_2_CA3_pvbas = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_pvbas",
    "tau_f": 12.07865594,
    "tau_r": 621.5074557,
    "tau_d": 3.826382269,
    "Uinc": 0.233832802,
    "gbarS": 3.034613716,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_pvbas = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_pvbas",
    "tau_f": 14.61380978,
    "tau_r": 542.0383477,
    "tau_d": 5.455384839,
    "Uinc": 0.196458328,
    "gbarS": 1.682870865,
    "Erev": -75.0,
}
CA3_olm_2_CA3_pvbas = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_pvbas",
    "tau_f": 17.1681726,
    "tau_r": 620.860479,
    "tau_d": 5.205992402,
    "Uinc": 0.221229248,
    "gbarS": 1.962668098,
    "Erev": -75.0,
}
DG_granule_soma_backgrond_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_backgrond",
    "post_name": "CA3_cckbas",
    "tau_f": 28.48521105,
    "tau_r": 512.1467675,
    "tau_d": 3.332916307,
    "Uinc": 0.230293415,
    "gbarS": 1.548467784,
    "Erev": 0.0,
}
DG_granule_soma_active1_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active1",
    "post_name": "CA3_cckbas",
    "tau_f": 28.48521105,
    "tau_r": 512.1467675,
    "tau_d": 3.332916307,
    "Uinc": 0.230293415,
    "gbarS": 1.548467784,
    "Erev": 0.0,
}
DG_granule_soma_active2_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active2",
    "post_name": "CA3_cckbas",
    "tau_f": 28.48521105,
    "tau_r": 512.1467675,
    "tau_d": 3.332916307,
    "Uinc": 0.230293415,
    "gbarS": 1.548467784,
    "Erev": 0.0,
}
DG_granule_soma_active3_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active3",
    "post_name": "CA3_cckbas",
    "tau_f": 28.48521105,
    "tau_r": 512.1467675,
    "tau_d": 3.332916307,
    "Uinc": 0.230293415,
    "gbarS": 1.548467784,
    "Erev": 0.0,
}
DG_granule_soma_active4_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active4",
    "post_name": "CA3_cckbas",
    "tau_f": 28.48521105,
    "tau_r": 512.1467675,
    "tau_d": 3.332916307,
    "Uinc": 0.230293415,
    "gbarS": 1.548467784,
    "Erev": 0.0,
}
DG_granule_soma_active5_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "DG_granule_soma_active5",
    "post_name": "CA3_cckbas",
    "tau_f": 28.48521105,
    "tau_r": 512.1467675,
    "tau_d": 3.332916307,
    "Uinc": 0.230293415,
    "gbarS": 1.548467784,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_cckbas",
    "tau_f": 21.66927055,
    "tau_r": 438.28249,
    "tau_d": 4.326690337,
    "Uinc": 0.205972377,
    "gbarS": 1.057563277,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_cckbas",
    "tau_f": 21.66927055,
    "tau_r": 438.28249,
    "tau_d": 4.326690337,
    "Uinc": 0.205972377,
    "gbarS": 1.057563277,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_cckbas",
    "tau_f": 21.66927055,
    "tau_r": 438.28249,
    "tau_d": 4.326690337,
    "Uinc": 0.205972377,
    "gbarS": 1.057563277,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_cckbas",
    "tau_f": 21.66927055,
    "tau_r": 438.28249,
    "tau_d": 4.326690337,
    "Uinc": 0.205972377,
    "gbarS": 1.057563277,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_cckbas",
    "tau_f": 21.66927055,
    "tau_r": 438.28249,
    "tau_d": 4.326690337,
    "Uinc": 0.205972377,
    "gbarS": 1.057563277,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_cckbas",
    "tau_f": 21.66927055,
    "tau_r": 438.28249,
    "tau_d": 4.326690337,
    "Uinc": 0.205972377,
    "gbarS": 1.057563277,
    "Erev": 0.0,
}
EC2_stellate_2_CA3_cckbas = {
    "w": 0.5,
    "pre_name": "EC2_stellate",
    "post_name": "CA3_cckbas",
    "tau_f": 29.94815981,
    "tau_r": 375.4614207,
    "tau_d": 3.311660422,
    "Uinc": 0.229470278,
    "gbarS": 1.380385298,
    "Erev": 0.0,
}
CA3_pvbas_2_CA3_cckbas = {
    "w": 0.1,
    "pre_name": "CA3_pvbas",
    "post_name": "CA3_cckbas",
    "tau_f": 16.0867027,
    "tau_r": 623.7190158,
    "tau_d": 4.741937623,
    "Uinc": 0.230855717,
    "gbarS": 1.786402874,
    "Erev": -75.0,
}
CA3_cckbas_2_CA3_cckbas = {
    "w": 0.1,
    "pre_name": "CA3_cckbas",
    "post_name": "CA3_cckbas",
    "tau_f": 19.05459643,
    "tau_r": 425.2172449,
    "tau_d": 4.926899388,
    "Uinc": 0.150252678,
    "gbarS": 1.11823959,
    "Erev": -75.0,
}
CA3_olm_2_CA3_cckbas = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_cckbas",
    "tau_f": 15.94286202,
    "tau_r": 621.5424093,
    "tau_d": 5.083297611,
    "Uinc": 0.228694061,
    "gbarS": 1.652804372,
    "Erev": -75.0,
}
CA3_pyr_soma_backgrond_2_CA3_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA3_olm",
    "tau_f": 31.57501482,
    "tau_r": 415.2956625,
    "tau_d": 5.591393916,
    "Uinc": 0.181122045,
    "gbarS": 0.912258218,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA3_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA3_olm",
    "tau_f": 31.57501482,
    "tau_r": 415.2956625,
    "tau_d": 5.591393916,
    "Uinc": 0.181122045,
    "gbarS": 0.912258218,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA3_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA3_olm",
    "tau_f": 31.57501482,
    "tau_r": 415.2956625,
    "tau_d": 5.591393916,
    "Uinc": 0.181122045,
    "gbarS": 0.912258218,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA3_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA3_olm",
    "tau_f": 31.57501482,
    "tau_r": 415.2956625,
    "tau_d": 5.591393916,
    "Uinc": 0.181122045,
    "gbarS": 0.912258218,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA3_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA3_olm",
    "tau_f": 31.57501482,
    "tau_r": 415.2956625,
    "tau_d": 5.591393916,
    "Uinc": 0.181122045,
    "gbarS": 0.912258218,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA3_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA3_olm",
    "tau_f": 31.57501482,
    "tau_r": 415.2956625,
    "tau_d": 5.591393916,
    "Uinc": 0.181122045,
    "gbarS": 0.912258218,
    "Erev": 0.0,
}
CA3_olm_2_CA3_olm = {
    "w": 0.1,
    "pre_name": "CA3_olm",
    "post_name": "CA3_olm",
    "tau_f": 23.14618786,
    "tau_r": 584.5909438,
    "tau_d": 6.523577623,
    "Uinc": 0.218677888,
    "gbarS": 1.659754127,
    "Erev": -75.0,
}
CA1_pyr_soma_backgrond_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_pyr_soma_backgrond = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_pyr_soma_active1 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_pyr_soma_active2 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_pyr_soma_active3 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_pyr_soma_active4 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_pyr_soma_active5 = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_pyr_dend_backgrond = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pyr_dend_backgrond",
    "tau_f": 21.84321492,
    "tau_r": 626.6211383,
    "tau_d": 6.461721231,
    "Uinc": 0.236507156,
    "gbarS": 1.369309873,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_pyr_dend_active1 = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pyr_dend_active1",
    "tau_f": 21.84321492,
    "tau_r": 626.6211383,
    "tau_d": 6.461721231,
    "Uinc": 0.236507156,
    "gbarS": 1.369309873,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_pyr_dend_active2 = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pyr_dend_active2",
    "tau_f": 21.84321492,
    "tau_r": 626.6211383,
    "tau_d": 6.461721231,
    "Uinc": 0.236507156,
    "gbarS": 1.369309873,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_pyr_dend_active3 = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pyr_dend_active3",
    "tau_f": 21.84321492,
    "tau_r": 626.6211383,
    "tau_d": 6.461721231,
    "Uinc": 0.236507156,
    "gbarS": 1.369309873,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_pyr_dend_active4 = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pyr_dend_active4",
    "tau_f": 21.84321492,
    "tau_r": 626.6211383,
    "tau_d": 6.461721231,
    "Uinc": 0.236507156,
    "gbarS": 1.369309873,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_pyr_dend_active5 = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pyr_dend_active5",
    "tau_f": 21.84321492,
    "tau_r": 626.6211383,
    "tau_d": 6.461721231,
    "Uinc": 0.236507156,
    "gbarS": 1.369309873,
    "Erev": 0.0,
}
CA1_aac_2_CA1_pyr_soma_backgrond = {
    "w": 0.1,
    "pre_name": "CA1_aac",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 8.885170901,
    "tau_r": 700.9008886,
    "tau_d": 6.288868745,
    "Uinc": 0.303356703,
    "gbarS": 3.059027201,
    "Erev": -75.0,
}
CA1_aac_2_CA1_pyr_soma_active1 = {
    "w": 0.1,
    "pre_name": "CA1_aac",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 8.885170901,
    "tau_r": 700.9008886,
    "tau_d": 6.288868745,
    "Uinc": 0.303356703,
    "gbarS": 3.059027201,
    "Erev": -75.0,
}
CA1_aac_2_CA1_pyr_soma_active2 = {
    "w": 0.1,
    "pre_name": "CA1_aac",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 8.885170901,
    "tau_r": 700.9008886,
    "tau_d": 6.288868745,
    "Uinc": 0.303356703,
    "gbarS": 3.059027201,
    "Erev": -75.0,
}
CA1_aac_2_CA1_pyr_soma_active3 = {
    "w": 0.1,
    "pre_name": "CA1_aac",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 8.885170901,
    "tau_r": 700.9008886,
    "tau_d": 6.288868745,
    "Uinc": 0.303356703,
    "gbarS": 3.059027201,
    "Erev": -75.0,
}
CA1_aac_2_CA1_pyr_soma_active4 = {
    "w": 0.1,
    "pre_name": "CA1_aac",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 8.885170901,
    "tau_r": 700.9008886,
    "tau_d": 6.288868745,
    "Uinc": 0.303356703,
    "gbarS": 3.059027201,
    "Erev": -75.0,
}
CA1_aac_2_CA1_pyr_soma_active5 = {
    "w": 0.1,
    "pre_name": "CA1_aac",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 8.885170901,
    "tau_r": 700.9008886,
    "tau_d": 6.288868745,
    "Uinc": 0.303356703,
    "gbarS": 3.059027201,
    "Erev": -75.0,
}
CA1_pvbas_2_CA1_pyr_soma_backgrond = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 11.57699627,
    "tau_r": 637.3779263,
    "tau_d": 4.408643738,
    "Uinc": 0.282768383,
    "gbarS": 6.067811614,
    "Erev": -75.0,
}
CA1_pvbas_2_CA1_pyr_soma_active1 = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 11.57699627,
    "tau_r": 637.3779263,
    "tau_d": 4.408643738,
    "Uinc": 0.282768383,
    "gbarS": 6.067811614,
    "Erev": -75.0,
}
CA1_pvbas_2_CA1_pyr_soma_active2 = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 11.57699627,
    "tau_r": 637.3779263,
    "tau_d": 4.408643738,
    "Uinc": 0.282768383,
    "gbarS": 6.067811614,
    "Erev": -75.0,
}
CA1_pvbas_2_CA1_pyr_soma_active3 = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 11.57699627,
    "tau_r": 637.3779263,
    "tau_d": 4.408643738,
    "Uinc": 0.282768383,
    "gbarS": 6.067811614,
    "Erev": -75.0,
}
CA1_pvbas_2_CA1_pyr_soma_active4 = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 11.57699627,
    "tau_r": 637.3779263,
    "tau_d": 4.408643738,
    "Uinc": 0.282768383,
    "gbarS": 6.067811614,
    "Erev": -75.0,
}
CA1_pvbas_2_CA1_pyr_soma_active5 = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 11.57699627,
    "tau_r": 637.3779263,
    "tau_d": 4.408643738,
    "Uinc": 0.282768383,
    "gbarS": 6.067811614,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_pyr_soma_backgrond = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 55.80256764,
    "tau_r": 659.1560802,
    "tau_d": 8.261691664,
    "Uinc": 0.230934787,
    "gbarS": 1.633849863,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_pyr_soma_active1 = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 55.80256764,
    "tau_r": 659.1560802,
    "tau_d": 8.261691664,
    "Uinc": 0.230934787,
    "gbarS": 1.633849863,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_pyr_soma_active2 = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 55.80256764,
    "tau_r": 659.1560802,
    "tau_d": 8.261691664,
    "Uinc": 0.230934787,
    "gbarS": 1.633849863,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_pyr_soma_active3 = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 55.80256764,
    "tau_r": 659.1560802,
    "tau_d": 8.261691664,
    "Uinc": 0.230934787,
    "gbarS": 1.633849863,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_pyr_soma_active4 = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 55.80256764,
    "tau_r": 659.1560802,
    "tau_d": 8.261691664,
    "Uinc": 0.230934787,
    "gbarS": 1.633849863,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_pyr_soma_active5 = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 55.80256764,
    "tau_r": 659.1560802,
    "tau_d": 8.261691664,
    "Uinc": 0.230934787,
    "gbarS": 1.633849863,
    "Erev": -75.0,
}
CA1_bis_2_CA1_pyr_soma_backgrond = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pyr_soma_backgrond",
    "tau_f": 9.208561312,
    "tau_r": 1164.285493,
    "tau_d": 11.2889288,
    "Uinc": 0.280258327,
    "gbarS": 1.4388733,
    "Erev": -75.0,
}
CA1_bis_2_CA1_pyr_soma_active1 = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pyr_soma_active1",
    "tau_f": 9.208561312,
    "tau_r": 1164.285493,
    "tau_d": 11.2889288,
    "Uinc": 0.280258327,
    "gbarS": 1.4388733,
    "Erev": -75.0,
}
CA1_bis_2_CA1_pyr_soma_active2 = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pyr_soma_active2",
    "tau_f": 9.208561312,
    "tau_r": 1164.285493,
    "tau_d": 11.2889288,
    "Uinc": 0.280258327,
    "gbarS": 1.4388733,
    "Erev": -75.0,
}
CA1_bis_2_CA1_pyr_soma_active3 = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pyr_soma_active3",
    "tau_f": 9.208561312,
    "tau_r": 1164.285493,
    "tau_d": 11.2889288,
    "Uinc": 0.280258327,
    "gbarS": 1.4388733,
    "Erev": -75.0,
}
CA1_bis_2_CA1_pyr_soma_active4 = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pyr_soma_active4",
    "tau_f": 9.208561312,
    "tau_r": 1164.285493,
    "tau_d": 11.2889288,
    "Uinc": 0.280258327,
    "gbarS": 1.4388733,
    "Erev": -75.0,
}
CA1_bis_2_CA1_pyr_soma_active5 = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pyr_soma_active5",
    "tau_f": 9.208561312,
    "tau_r": 1164.285493,
    "tau_d": 11.2889288,
    "Uinc": 0.280258327,
    "gbarS": 1.4388733,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_pyr_dend_backgrond = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pyr_dend_backgrond",
    "tau_f": 11.0166117,
    "tau_r": 994.5394996,
    "tau_d": 10.09350595,
    "Uinc": 0.263139955,
    "gbarS": 1.372446563,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_pyr_dend_active1 = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pyr_dend_active1",
    "tau_f": 11.0166117,
    "tau_r": 994.5394996,
    "tau_d": 10.09350595,
    "Uinc": 0.263139955,
    "gbarS": 1.372446563,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_pyr_dend_active2 = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pyr_dend_active2",
    "tau_f": 11.0166117,
    "tau_r": 994.5394996,
    "tau_d": 10.09350595,
    "Uinc": 0.263139955,
    "gbarS": 1.372446563,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_pyr_dend_active3 = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pyr_dend_active3",
    "tau_f": 11.0166117,
    "tau_r": 994.5394996,
    "tau_d": 10.09350595,
    "Uinc": 0.263139955,
    "gbarS": 1.372446563,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_pyr_dend_active4 = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pyr_dend_active4",
    "tau_f": 11.0166117,
    "tau_r": 994.5394996,
    "tau_d": 10.09350595,
    "Uinc": 0.263139955,
    "gbarS": 1.372446563,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_pyr_dend_active5 = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pyr_dend_active5",
    "tau_f": 11.0166117,
    "tau_r": 994.5394996,
    "tau_d": 10.09350595,
    "Uinc": 0.263139955,
    "gbarS": 1.372446563,
    "Erev": -75.0,
}
CA1_olm_2_CA1_pyr_dend_backgrond = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pyr_dend_backgrond",
    "tau_f": 12.28169848,
    "tau_r": 783.1238783,
    "tau_d": 7.989148919,
    "Uinc": 0.233093825,
    "gbarS": 1.645016607,
    "Erev": -75.0,
}
CA1_olm_2_CA1_pyr_dend_active1 = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pyr_dend_active1",
    "tau_f": 12.28169848,
    "tau_r": 783.1238783,
    "tau_d": 7.989148919,
    "Uinc": 0.233093825,
    "gbarS": 1.645016607,
    "Erev": -75.0,
}
CA1_olm_2_CA1_pyr_dend_active2 = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pyr_dend_active2",
    "tau_f": 12.28169848,
    "tau_r": 783.1238783,
    "tau_d": 7.989148919,
    "Uinc": 0.233093825,
    "gbarS": 1.645016607,
    "Erev": -75.0,
}
CA1_olm_2_CA1_pyr_dend_active3 = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pyr_dend_active3",
    "tau_f": 12.28169848,
    "tau_r": 783.1238783,
    "tau_d": 7.989148919,
    "Uinc": 0.233093825,
    "gbarS": 1.645016607,
    "Erev": -75.0,
}
CA1_olm_2_CA1_pyr_dend_active4 = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pyr_dend_active4",
    "tau_f": 12.28169848,
    "tau_r": 783.1238783,
    "tau_d": 7.989148919,
    "Uinc": 0.233093825,
    "gbarS": 1.645016607,
    "Erev": -75.0,
}
CA1_olm_2_CA1_pyr_dend_active5 = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pyr_dend_active5",
    "tau_f": 12.28169848,
    "tau_r": 783.1238783,
    "tau_d": 7.989148919,
    "Uinc": 0.233093825,
    "gbarS": 1.645016607,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_pyr_dend_backgrond = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pyr_dend_backgrond",
    "tau_f": 12.64055945,
    "tau_r": 756.6409477,
    "tau_d": 9.005120153,
    "Uinc": 0.245917498,
    "gbarS": 1.472888948,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_pyr_dend_active1 = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pyr_dend_active1",
    "tau_f": 12.64055945,
    "tau_r": 756.6409477,
    "tau_d": 9.005120153,
    "Uinc": 0.245917498,
    "gbarS": 1.472888948,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_pyr_dend_active2 = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pyr_dend_active2",
    "tau_f": 12.64055945,
    "tau_r": 756.6409477,
    "tau_d": 9.005120153,
    "Uinc": 0.245917498,
    "gbarS": 1.472888948,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_pyr_dend_active3 = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pyr_dend_active3",
    "tau_f": 12.64055945,
    "tau_r": 756.6409477,
    "tau_d": 9.005120153,
    "Uinc": 0.245917498,
    "gbarS": 1.472888948,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_pyr_dend_active4 = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pyr_dend_active4",
    "tau_f": 12.64055945,
    "tau_r": 756.6409477,
    "tau_d": 9.005120153,
    "Uinc": 0.245917498,
    "gbarS": 1.472888948,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_pyr_dend_active5 = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pyr_dend_active5",
    "tau_f": 12.64055945,
    "tau_r": 756.6409477,
    "tau_d": 9.005120153,
    "Uinc": 0.245917498,
    "gbarS": 1.472888948,
    "Erev": -75.0,
}
CA3_pyr_soma_backgrond_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_aac = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_aac",
    "tau_f": 42.9199623,
    "tau_r": 331.4994604,
    "tau_d": 3.65913222,
    "Uinc": 0.243195341,
    "gbarS": 1.529326081,
    "Erev": 0.0,
}
CA1_pvbas_2_CA1_aac = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_aac",
    "tau_f": 17.45934692,
    "tau_r": 596.691056,
    "tau_d": 4.000930559,
    "Uinc": 0.272333274,
    "gbarS": 3.523878672,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_aac = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_aac",
    "tau_f": 67.94156049,
    "tau_r": 663.3815975,
    "tau_d": 7.436965993,
    "Uinc": 0.223366693,
    "gbarS": 1.337587481,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_aac = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_aac",
    "tau_f": 23.42714963,
    "tau_r": 546.7347205,
    "tau_d": 6.664521618,
    "Uinc": 0.226229064,
    "gbarS": 1.462421379,
    "Erev": -75.0,
}
CA1_olm_2_CA1_aac = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_aac",
    "tau_f": 19.38979865,
    "tau_r": 602.3297343,
    "tau_d": 5.828232848,
    "Uinc": 0.229179593,
    "gbarS": 1.655937714,
    "Erev": -75.0,
}
CA1_bis_2_CA1_aac = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_aac",
    "tau_f": 15.73374895,
    "tau_r": 738.2651761,
    "tau_d": 7.937465661,
    "Uinc": 0.258069644,
    "gbarS": 1.44425622,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_aac = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_aac",
    "tau_f": 18.27596659,
    "tau_r": 679.3194126,
    "tau_d": 6.998383806,
    "Uinc": 0.246925867,
    "gbarS": 1.479657319,
    "Erev": -75.0,
}
CA3_pyr_soma_backgrond_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 0.908653493,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 0.908653493,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 0.908653493,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 0.908653493,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 0.908653493,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 0.908653493,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_pvbas",
    "tau_f": 76.85776536,
    "tau_r": 327.2596661,
    "tau_d": 3.163416515,
    "Uinc": 0.200078943,
    "gbarS": 1.350968596,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_pvbas",
    "tau_f": 76.85776536,
    "tau_r": 327.2596661,
    "tau_d": 3.163416515,
    "Uinc": 0.200078943,
    "gbarS": 1.350968596,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_pvbas",
    "tau_f": 76.85776536,
    "tau_r": 327.2596661,
    "tau_d": 3.163416515,
    "Uinc": 0.200078943,
    "gbarS": 1.350968596,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_pvbas",
    "tau_f": 76.85776536,
    "tau_r": 327.2596661,
    "tau_d": 3.163416515,
    "Uinc": 0.200078943,
    "gbarS": 1.350968596,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_pvbas",
    "tau_f": 76.85776536,
    "tau_r": 327.2596661,
    "tau_d": 3.163416515,
    "Uinc": 0.200078943,
    "gbarS": 1.350968596,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_pvbas",
    "tau_f": 76.85776536,
    "tau_r": 327.2596661,
    "tau_d": 3.163416515,
    "Uinc": 0.200078943,
    "gbarS": 1.350968596,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_pvbas = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pvbas",
    "tau_f": 38.32919213,
    "tau_r": 363.4563494,
    "tau_d": 3.914953021,
    "Uinc": 0.247415928,
    "gbarS": 1.382260541,
    "Erev": 0.0,
}
CA1_pvbas_2_CA1_pvbas = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pvbas",
    "tau_f": 15.09543237,
    "tau_r": 635.5365307,
    "tau_d": 3.831414171,
    "Uinc": 0.273852244,
    "gbarS": 3.315200522,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_pvbas = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pvbas",
    "tau_f": 53.15475426,
    "tau_r": 752.2001856,
    "tau_d": 6.961632328,
    "Uinc": 0.226835913,
    "gbarS": 1.236161794,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_pvbas = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pvbas",
    "tau_f": 20.39924327,
    "tau_r": 598.3218367,
    "tau_d": 6.456458576,
    "Uinc": 0.226229476,
    "gbarS": 1.388199859,
    "Erev": -75.0,
}
CA1_olm_2_CA1_pvbas = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pvbas",
    "tau_f": 16.57863002,
    "tau_r": 650.1346414,
    "tau_d": 5.685709176,
    "Uinc": 0.230148227,
    "gbarS": 1.567269637,
    "Erev": -75.0,
}
CA1_bis_2_CA1_pvbas = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pvbas",
    "tau_f": 12.41977701,
    "tau_r": 776.2305412,
    "tau_d": 7.451818541,
    "Uinc": 0.261813528,
    "gbarS": 1.469428253,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_pvbas = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pvbas",
    "tau_f": 14.29480314,
    "tau_r": 735.7744076,
    "tau_d": 6.516360302,
    "Uinc": 0.251386833,
    "gbarS": 1.509851331,
    "Erev": -75.0,
}
CA3_pyr_soma_backgrond_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_cckbas",
    "tau_f": 61.43867292,
    "tau_r": 330.9105197,
    "tau_d": 4.833858548,
    "Uinc": 0.226501333,
    "gbarS": 1.215139842,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_cckbas",
    "tau_f": 61.43867292,
    "tau_r": 330.9105197,
    "tau_d": 4.833858548,
    "Uinc": 0.226501333,
    "gbarS": 1.215139842,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_cckbas",
    "tau_f": 61.43867292,
    "tau_r": 330.9105197,
    "tau_d": 4.833858548,
    "Uinc": 0.226501333,
    "gbarS": 1.215139842,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_cckbas",
    "tau_f": 61.43867292,
    "tau_r": 330.9105197,
    "tau_d": 4.833858548,
    "Uinc": 0.226501333,
    "gbarS": 1.215139842,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_cckbas",
    "tau_f": 61.43867292,
    "tau_r": 330.9105197,
    "tau_d": 4.833858548,
    "Uinc": 0.226501333,
    "gbarS": 1.215139842,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_cckbas",
    "tau_f": 61.43867292,
    "tau_r": 330.9105197,
    "tau_d": 4.833858548,
    "Uinc": 0.226501333,
    "gbarS": 1.215139842,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_cckbas",
    "tau_f": 200.0945674,
    "tau_r": 170.3265276,
    "tau_d": 2.77089926,
    "Uinc": 0.248751595,
    "gbarS": 1.889612224,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_cckbas",
    "tau_f": 200.0945674,
    "tau_r": 170.3265276,
    "tau_d": 2.77089926,
    "Uinc": 0.248751595,
    "gbarS": 1.889612224,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_cckbas",
    "tau_f": 200.0945674,
    "tau_r": 170.3265276,
    "tau_d": 2.77089926,
    "Uinc": 0.248751595,
    "gbarS": 1.889612224,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_cckbas",
    "tau_f": 200.0945674,
    "tau_r": 170.3265276,
    "tau_d": 2.77089926,
    "Uinc": 0.248751595,
    "gbarS": 1.889612224,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_cckbas",
    "tau_f": 200.0945674,
    "tau_r": 170.3265276,
    "tau_d": 2.77089926,
    "Uinc": 0.248751595,
    "gbarS": 1.889612224,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_cckbas",
    "tau_f": 200.0945674,
    "tau_r": 170.3265276,
    "tau_d": 2.77089926,
    "Uinc": 0.248751595,
    "gbarS": 1.889612224,
    "Erev": 0.0,
}
EC3_pyr_2_CA1_cckbas = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_cckbas",
    "tau_f": 97.27041139,
    "tau_r": 274.8237744,
    "tau_d": 3.484495113,
    "Uinc": 0.254792697,
    "gbarS": 1.903160825,
    "Erev": 0.0,
}
CA1_pvbas_2_CA1_cckbas = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_cckbas",
    "tau_f": 27.30034173,
    "tau_r": 576.2250426,
    "tau_d": 4.229703968,
    "Uinc": 0.262471938,
    "gbarS": 3.102685857,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_cckbas = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_cckbas",
    "tau_f": 89.13915001,
    "tau_r": 638.8350601,
    "tau_d": 6.672410531,
    "Uinc": 0.214495264,
    "gbarS": 1.397935548,
    "Erev": -75.0,
}
CA1_ngf_2_CA1_cckbas = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_cckbas",
    "tau_f": 40.31598397,
    "tau_r": 500.1573243,
    "tau_d": 6.217529468,
    "Uinc": 0.230065706,
    "gbarS": 1.590137208,
    "Erev": -75.0,
}
CA1_olm_2_CA1_cckbas = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_cckbas",
    "tau_f": 36.41141922,
    "tau_r": 527.6239734,
    "tau_d": 5.47406422,
    "Uinc": 0.230329792,
    "gbarS": 1.785302837,
    "Erev": -75.0,
}
CA1_bis_2_CA1_cckbas = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_cckbas",
    "tau_f": 40.08819019,
    "tau_r": 546.2435104,
    "tau_d": 7.996295433,
    "Uinc": 0.255620629,
    "gbarS": 1.578235331,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_cckbas = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_cckbas",
    "tau_f": 34.90925551,
    "tau_r": 569.0414429,
    "tau_d": 6.94357973,
    "Uinc": 0.243993471,
    "gbarS": 1.544074905,
    "Erev": -75.0,
}
EC3_pyr_2_CA1_ngf = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA1_ngf_2_CA1_ngf = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_ngf",
    "tau_f": 25.480563,
    "tau_r": 553.4916051,
    "tau_d": 8.831768275,
    "Uinc": 0.212282632,
    "gbarS": 1.588573475,
    "Erev": -75.0,
}
CA1_olm_2_CA1_ngf = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_ngf",
    "tau_f": 20.57681507,
    "tau_r": 578.1117892,
    "tau_d": 6.800428696,
    "Uinc": 0.209514977,
    "gbarS": 1.726166607,
    "Erev": -75.0,
}
CA3_pyr_soma_backgrond_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_olm",
    "tau_f": 38.22553135,
    "tau_r": 358.2571628,
    "tau_d": 5.430321889,
    "Uinc": 0.102925387,
    "gbarS": 0.866891054,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_olm",
    "tau_f": 38.22553135,
    "tau_r": 358.2571628,
    "tau_d": 5.430321889,
    "Uinc": 0.102925387,
    "gbarS": 0.866891054,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_olm",
    "tau_f": 38.22553135,
    "tau_r": 358.2571628,
    "tau_d": 5.430321889,
    "Uinc": 0.102925387,
    "gbarS": 0.866891054,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_olm",
    "tau_f": 38.22553135,
    "tau_r": 358.2571628,
    "tau_d": 5.430321889,
    "Uinc": 0.102925387,
    "gbarS": 0.866891054,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_olm",
    "tau_f": 38.22553135,
    "tau_r": 358.2571628,
    "tau_d": 5.430321889,
    "Uinc": 0.102925387,
    "gbarS": 0.866891054,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_olm",
    "tau_f": 38.22553135,
    "tau_r": 358.2571628,
    "tau_d": 5.430321889,
    "Uinc": 0.102925387,
    "gbarS": 0.866891054,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 1.699075536,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 1.699075536,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 1.699075536,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 1.699075536,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 1.699075536,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_olm = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 1.699075536,
    "Erev": 0.0,
}
CA1_bis_2_CA1_olm = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_olm",
    "tau_f": 17.81144768,
    "tau_r": 717.0400063,
    "tau_d": 8.372598889,
    "Uinc": 0.16820889,
    "gbarS": 1.22935451,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_olm = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_olm",
    "tau_f": 20.46870934,
    "tau_r": 669.3842837,
    "tau_d": 7.259238763,
    "Uinc": 0.150359351,
    "gbarS": 1.249240474,
    "Erev": -75.0,
}
CA3_pyr_soma_backgrond_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_bis",
    "tau_f": 27.56437073,
    "tau_r": 369.3806703,
    "tau_d": 6.184627383,
    "Uinc": 0.213215335,
    "gbarS": 1.150542157,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_bis",
    "tau_f": 27.56437073,
    "tau_r": 369.3806703,
    "tau_d": 6.184627383,
    "Uinc": 0.213215335,
    "gbarS": 1.150542157,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_bis",
    "tau_f": 27.56437073,
    "tau_r": 369.3806703,
    "tau_d": 6.184627383,
    "Uinc": 0.213215335,
    "gbarS": 1.150542157,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_bis",
    "tau_f": 27.56437073,
    "tau_r": 369.3806703,
    "tau_d": 6.184627383,
    "Uinc": 0.213215335,
    "gbarS": 1.150542157,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_bis",
    "tau_f": 27.56437073,
    "tau_r": 369.3806703,
    "tau_d": 6.184627383,
    "Uinc": 0.213215335,
    "gbarS": 1.150542157,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_bis",
    "tau_f": 27.56437073,
    "tau_r": 369.3806703,
    "tau_d": 6.184627383,
    "Uinc": 0.213215335,
    "gbarS": 1.150542157,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_bis",
    "tau_f": 45.77509046,
    "tau_r": 242.468234,
    "tau_d": 3.394198844,
    "Uinc": 0.225236757,
    "gbarS": 2.155417698,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_bis",
    "tau_f": 45.77509046,
    "tau_r": 242.468234,
    "tau_d": 3.394198844,
    "Uinc": 0.225236757,
    "gbarS": 2.155417698,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_bis",
    "tau_f": 45.77509046,
    "tau_r": 242.468234,
    "tau_d": 3.394198844,
    "Uinc": 0.225236757,
    "gbarS": 2.155417698,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_bis",
    "tau_f": 45.77509046,
    "tau_r": 242.468234,
    "tau_d": 3.394198844,
    "Uinc": 0.225236757,
    "gbarS": 2.155417698,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_bis",
    "tau_f": 45.77509046,
    "tau_r": 242.468234,
    "tau_d": 3.394198844,
    "Uinc": 0.225236757,
    "gbarS": 2.155417698,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_bis = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_bis",
    "tau_f": 45.77509046,
    "tau_r": 242.468234,
    "tau_d": 3.394198844,
    "Uinc": 0.225236757,
    "gbarS": 2.155417698,
    "Erev": 0.0,
}
CA1_pvbas_2_CA1_bis = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_bis",
    "tau_f": 21.4215323,
    "tau_r": 584.4912283,
    "tau_d": 5.061443542,
    "Uinc": 0.270965957,
    "gbarS": 2.88716469,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_bis = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_bis",
    "tau_f": 49.03171673,
    "tau_r": 628.2474546,
    "tau_d": 8.205527136,
    "Uinc": 0.229198624,
    "gbarS": 1.464067105,
    "Erev": -75.0,
}
CA1_bis_2_CA1_bis = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_bis",
    "tau_f": 14.32265778,
    "tau_r": 709.9692541,
    "tau_d": 10.17310097,
    "Uinc": 0.265016793,
    "gbarS": 1.461626916,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_bis = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_bis",
    "tau_f": 16.85933504,
    "tau_r": 640.9715027,
    "tau_d": 9.042053959,
    "Uinc": 0.255722736,
    "gbarS": 1.506680891,
    "Erev": -75.0,
}
CA3_pyr_soma_backgrond_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_ivy",
    "tau_f": 22.00501845,
    "tau_r": 419.0888672,
    "tau_d": 6.514490352,
    "Uinc": 0.211997085,
    "gbarS": 1.139035363,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_ivy",
    "tau_f": 22.00501845,
    "tau_r": 419.0888672,
    "tau_d": 6.514490352,
    "Uinc": 0.211997085,
    "gbarS": 1.139035363,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_ivy",
    "tau_f": 22.00501845,
    "tau_r": 419.0888672,
    "tau_d": 6.514490352,
    "Uinc": 0.211997085,
    "gbarS": 1.139035363,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_ivy",
    "tau_f": 22.00501845,
    "tau_r": 419.0888672,
    "tau_d": 6.514490352,
    "Uinc": 0.211997085,
    "gbarS": 1.139035363,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_ivy",
    "tau_f": 22.00501845,
    "tau_r": 419.0888672,
    "tau_d": 6.514490352,
    "Uinc": 0.211997085,
    "gbarS": 1.139035363,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_ivy",
    "tau_f": 22.00501845,
    "tau_r": 419.0888672,
    "tau_d": 6.514490352,
    "Uinc": 0.211997085,
    "gbarS": 1.139035363,
    "Erev": 0.0,
}
CA1_pyr_soma_backgrond_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_backgrond",
    "post_name": "CA1_ivy",
    "tau_f": 29.98390368,
    "tau_r": 294.5593265,
    "tau_d": 3.90415446,
    "Uinc": 0.223851273,
    "gbarS": 2.125086979,
    "Erev": 0.0,
}
CA1_pyr_soma_active1_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active1",
    "post_name": "CA1_ivy",
    "tau_f": 29.98390368,
    "tau_r": 294.5593265,
    "tau_d": 3.90415446,
    "Uinc": 0.223851273,
    "gbarS": 2.125086979,
    "Erev": 0.0,
}
CA1_pyr_soma_active2_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active2",
    "post_name": "CA1_ivy",
    "tau_f": 29.98390368,
    "tau_r": 294.5593265,
    "tau_d": 3.90415446,
    "Uinc": 0.223851273,
    "gbarS": 2.125086979,
    "Erev": 0.0,
}
CA1_pyr_soma_active3_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active3",
    "post_name": "CA1_ivy",
    "tau_f": 29.98390368,
    "tau_r": 294.5593265,
    "tau_d": 3.90415446,
    "Uinc": 0.223851273,
    "gbarS": 2.125086979,
    "Erev": 0.0,
}
CA1_pyr_soma_active4_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active4",
    "post_name": "CA1_ivy",
    "tau_f": 29.98390368,
    "tau_r": 294.5593265,
    "tau_d": 3.90415446,
    "Uinc": 0.223851273,
    "gbarS": 2.125086979,
    "Erev": 0.0,
}
CA1_pyr_soma_active5_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA1_pyr_soma_active5",
    "post_name": "CA1_ivy",
    "tau_f": 29.98390368,
    "tau_r": 294.5593265,
    "tau_d": 3.90415446,
    "Uinc": 0.223851273,
    "gbarS": 2.125086979,
    "Erev": 0.0,
}
CA1_pvbas_2_CA1_ivy = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_ivy",
    "tau_f": 17.30237842,
    "tau_r": 598.4298782,
    "tau_d": 5.025261209,
    "Uinc": 0.27646958,
    "gbarS": 3.391835068,
    "Erev": -75.0,
}
CA1_cckbas_2_CA1_ivy = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_ivy",
    "tau_f": 39.16684388,
    "tau_r": 653.4158889,
    "tau_d": 8.3616028,
    "Uinc": 0.231460691,
    "gbarS": 1.58994451,
    "Erev": -75.0,
}
CA1_bis_2_CA1_ivy = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_ivy",
    "tau_f": 11.55699251,
    "tau_r": 760.0916001,
    "tau_d": 10.62000192,
    "Uinc": 0.271264353,
    "gbarS": 1.594908861,
    "Erev": -75.0,
}
CA1_ivy_2_CA1_ivy = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_ivy",
    "tau_f": 13.38354637,
    "tau_r": 688.7459606,
    "tau_d": 9.404598492,
    "Uinc": 0.258486588,
    "gbarS": 1.624924882,
    "Erev": -75.0,
}
EC3_pyr_2_CA1_ivy = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_ivy",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA3_pyr_soma_backgrond_2_CA1_ngf = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_backgrond",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA3_pyr_soma_active1_2_CA1_ngf = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active1",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA3_pyr_soma_active2_2_CA1_ngf = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active2",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA3_pyr_soma_active3_2_CA1_ngf = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active3",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA3_pyr_soma_active4_2_CA1_ngf = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active4",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA3_pyr_soma_active5_2_CA1_ngf = {
    "w": 0.5,
    "pre_name": "CA3_pyr_soma_active5",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA1_ivy_2_CA1_ngf = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_ngf",
    "tau_f": 25.480563,
    "tau_r": 553.4916051,
    "tau_d": 8.831768275,
    "Uinc": 0.212282632,
    "gbarS": 1.588573475,
    "Erev": -75.0,
}

MS_teevra_2_CA3_aac = {
    "w": 0.1,
    "pre_name": "MS_teevra",
    "post_name": "CA3_aac",
    "tau_f": 25.480563,
    "tau_r": 553.4916051,
    "tau_d": 8.831768275,
    "Uinc": 0.212282632,
    "gbarS": 1.588573475,
    "Erev": -75.0,
}

MS_teevra_2_CA3_cckbas = {
    "w": 0.1,
    "pre_name": "MS_teevra",
    "post_name": "CA3_cckbas",
    "tau_f": 25.480563,
    "tau_r": 553.4916051,
    "tau_d": 8.831768275,
    "Uinc": 0.212282632,
    "gbarS": 1.588573475,
    "Erev": -75.0,
}


################# end block of synapses params #########################
########################################################################

##########################################
##### block of generators params #########
msteevra_params = {
    "name" : "MS_teevra",
    "R": 0.6,
    "freq": 5,
    "mean_spike_rate": 50,
    "phase": 1.58,
}

ec2_params = {
    "name" : "EC2",
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 0.5,
    "phase": 3.14,
}

ec3_params = {
    "name" : "EC3",
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 0.5,
    "phase": -1.57,
}
##############################################################################
##
DG_granular_cells = [DG_granule_soma_background_params, DG_granule_dend_background_params,]# \
#                     DG_granule_soma_active1_params, DG_granule_dend_active1_params, \
#                     DG_granule_soma_active2_params, DG_granule_dend_active2_params, \
#                     DG_granule_soma_active3_params, DG_granule_dend_active3_params, \
#                     DG_granule_soma_active4_params, DG_granule_dend_active4_params, \
#                     DG_granule_soma_active5_params, DG_granule_dend_active5_params ]


CA3_pyr_cells = [CA3_pyr_soma_background_params, CA3_pyr_dend_background_params,] # \
#                 CA3_pyr_soma_active1_params, CA3_pyr_dend_active1_params, \
#                 CA3_pyr_soma_active2_params, CA3_pyr_dend_active2_params, \
#                 CA3_pyr_soma_active3_params, CA3_pyr_dend_active3_params, \
#                 CA3_pyr_soma_active4_params, CA3_pyr_dend_active4_params, \
#                 CA3_pyr_soma_active5_params, CA3_pyr_dend_active5_params ]

CA1_pyr_cells = [CA1_pyr_soma_background_params, CA1_pyr_dend_background_params,] # \
#                 CA1_pyr_soma_active1_params, CA1_pyr_dend_active1_params, \
#                 CA1_pyr_soma_active2_params, CA1_pyr_dend_active2_params, \
#                 CA1_pyr_soma_active3_params, CA1_pyr_dend_active3_params, \
#                 CA1_pyr_soma_active4_params, CA1_pyr_dend_active4_params, \
#                 CA1_pyr_soma_active5_params, CA1_pyr_dend_active5_params ]


two_comps_cells = DG_granular_cells + CA3_pyr_cells + CA1_pyr_cells


DG_cells = [DG_mossy_params, DG_aac_params, DG_cckbas_params, DG_pvbas_params]
CA3_cells = [CA3_aac_params, CA3_pvbas_params, CA3_cckbas_params, CA3_olm_params]
CA1_cells = [CA1_pvbas_params, CA1_olm_params, CA1_cckbas_params, CA1_bis_params, CA1_aac_params, CA1_ivy_params, CA1_ngf_params]



#[CA1_pyr_2_CA1_pyr, CA3_pyr_2_CA1_pyr, EC3_pyr_2_CA1_pyr, CA1_aac_2_CA1_pyr, CA1_pvbas_2_CA1_pyr, CA1_cckbas_2_CA1_pyr, CA1_bis_2_CA1_pyr, CA1_ivy_2_CA1_pyr, CA1_olm_2_CA1_pyr, CA1_ngf_2_CA1_pyr, CA3_pyr_2_CA1_aac, CA1_pyr_2_CA1_aac, EC3_pyr_2_CA1_aac, CA1_pvbas_2_CA1_aac, CA1_cckbas_2_CA1_aac, CA1_ngf_2_CA1_aac, CA1_olm_2_CA1_aac, CA1_bis_2_CA1_aac, CA1_ivy_2_CA1_aac, CA3_pyr_2_CA1_pvbas, CA1_pyr_2_CA1_pvbas, EC3_pyr_2_CA1_pvbas, CA1_pvbas_2_CA1_pvbas, CA1_cckbas_2_CA1_pvbas, CA1_ngf_2_CA1_pvbas, CA1_olm_2_CA1_pvbas, CA1_bis_2_CA1_pvbas, CA1_ivy_2_CA1_pvbas, CA3_pyr_2_CA1_cckbas, CA1_pyr_2_CA1_cckbas, EC3_pyr_2_CA1_cckbas, CA1_pvbas_2_CA1_cckbas, CA1_cckbas_2_CA1_cckbas, CA1_ngf_2_CA1_cckbas, CA1_olm_2_CA1_cckbas, CA1_bis_2_CA1_cckbas, CA1_ivy_2_CA1_cckbas, EC3_pyr_2_CA1_ngf, CA1_ngf_2_CA1_ngf, CA1_olm_2_CA1_ngf, CA3_pyr_2_CA1_olm, CA1_pyr_2_CA1_olm, CA1_bis_2_CA1_olm, CA1_ivy_2_CA1_olm, CA3_pyr_2_CA1_bis, CA1_pyr_2_CA1_bis, CA1_pvbas_2_CA1_bis, CA1_cckbas_2_CA1_bis, CA1_bis_2_CA1_bis, CA1_ivy_2_CA1_bis, CA3_pyr_2_CA1_ivy, CA1_pyr_2_CA1_ivy, CA1_pvbas_2_CA1_ivy, CA1_cckbas_2_CA1_ivy, CA1_bis_2_CA1_ivy, CA1_ivy_2_CA1_ivy, EC3_pyr_2_CA1_ivy, CA3_pyr_2_CA1_ngf, CA1_ivy_2_CA1_ngf]

params_synapses = [[], []]
for variable in dir():
    if variable.find('_2_') != -1:
        syn_params = globals()[variable]
        if (syn_params['pre_name'].find("active") != -1) or (syn_params['post_name'].find("active") != -1):
            continue

        optim_idx = 0
        if (syn_params['post_name'].find("CA1") != -1) and (syn_params['post_name'].find("pyr") == -1):
            optim_idx = 1

        params_synapses[optim_idx].append(syn_params)

# for syn in params_synapses[0]:
#     print(syn['pre_name'], "->", syn['post_name'])
#print(len(params_synapses[0]))
#print(len(params_synapses[1]))

params_net = {
"params_neurons" : two_comps_cells + DG_cells + CA3_cells + CA1_cells,
"params_generators" : [msteevra_params, ec2_params, ec3_params],
"params_synapses" : params_synapses,
}
