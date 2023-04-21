import neuron_models
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
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target": {},
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
    "Iext": 1.0,
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
    "target" : {},
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
    "target" : {},
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
    "target" : {},
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
    "target" : {},
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
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target": {},
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
    "target" : {},
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
    "target" : {},
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
    "target" : {},
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
    "target" : {},
}
###################################################################
### CA1 neurons
CA1_pyr_soma_params = {
    "name": "CA1_pyr_soma",
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

CA1_pyr_dend_params = {
    "name": "CA1_pyr_dend",
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
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 20.0,
        "phase": 0.0,
    },
}

########################################################################
################# block of synapses params #############################

CA1_pyr2CA1_pyr = {
    "w": 0.5,
    "pre_name": "CA1_pyr",
    "post_name": "CA1_pyr",
    "tau_f": 19.0939326,
    "tau_r": 801.5798994,
    "tau_d": 6.489890385,
    "Uinc": 0.220334906,
    "gbarS": 1.310724564,
    "Erev": 0.0,
}
CA3_pyr2CA1_pyr = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_pyr",
    "tau_f": 18.01005789,
    "tau_r": 724.3667977,
    "tau_d": 7.463702539,
    "Uinc": 0.201847939,
    "gbarS": 1.021220696,
    "Erev": 0.0,
}
EC3_pyr2CA1_pyr = {
    "w": 0.5,
    "pre_name": "EC3_pyr",
    "post_name": "CA1_pyr",
    "tau_f": 21.84321492,
    "tau_r": 626.6211383,
    "tau_d": 6.461721231,
    "Uinc": 0.236507156,
    "gbarS": 1.369309873,
    "Erev": 0.0,
}
CA1_aac2CA1_pyr = {
    "w": 0.1,
    "pre_name": "CA1_aac",
    "post_name": "CA1_pyr",
    "tau_f": 8.885170901,
    "tau_r": 700.9008886,
    "tau_d": 6.288868745,
    "Uinc": 0.303356703,
    "gbarS": 3.059027201,
    "Erev": -75.0,
}
CA1_pvbas2CA1_pyr = {
    "w": 0.1,
    "pre_name": "CA1_pvbas",
    "post_name": "CA1_pyr",
    "tau_f": 11.57699627,
    "tau_r": 637.3779263,
    "tau_d": 4.408643738,
    "Uinc": 0.282768383,
    "gbarS": 6.067811614,
    "Erev": -75.0,
}
CA1_cckbas2CA1_pyr = {
    "w": 0.1,
    "pre_name": "CA1_cckbas",
    "post_name": "CA1_pyr",
    "tau_f": 55.80256764,
    "tau_r": 659.1560802,
    "tau_d": 8.261691664,
    "Uinc": 0.230934787,
    "gbarS": 1.633849863,
    "Erev": -75.0,
}
CA1_bis2CA1_pyr = {
    "w": 0.1,
    "pre_name": "CA1_bis",
    "post_name": "CA1_pyr",
    "tau_f": 9.208561312,
    "tau_r": 1164.285493,
    "tau_d": 11.2889288,
    "Uinc": 0.280258327,
    "gbarS": 1.4388733,
    "Erev": -75.0,
}
CA1_ivy2CA1_pyr = {
    "w": 0.1,
    "pre_name": "CA1_ivy",
    "post_name": "CA1_pyr",
    "tau_f": 11.0166117,
    "tau_r": 994.5394996,
    "tau_d": 10.09350595,
    "Uinc": 0.263139955,
    "gbarS": 1.372446563,
    "Erev": -75.0,
}
CA1_olm2CA1_pyr = {
    "w": 0.1,
    "pre_name": "CA1_olm",
    "post_name": "CA1_pyr",
    "tau_f": 12.28169848,
    "tau_r": 783.1238783,
    "tau_d": 7.989148919,
    "Uinc": 0.233093825,
    "gbarS": 1.645016607,
    "Erev": -75.0,
}
CA1_ngf2CA1_pyr = {
    "w": 0.1,
    "pre_name": "CA1_ngf",
    "post_name": "CA1_pyr",
    "tau_f": 12.64055945,
    "tau_r": 756.6409477,
    "tau_d": 9.005120153,
    "Uinc": 0.245917498,
    "gbarS": 1.472888948,
    "Erev": -75.0,
}
CA3_pyr2CA1_aac = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}
CA1_pyr2CA1_aac = {
    "w": 0.5,
    "pre_name": "CA1_pyr",
    "post_name": "CA1_aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}
EC3_pyr2CA1_aac = {
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
CA1_pvbas2CA1_aac = {
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
CA1_cckbas2CA1_aac = {
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
CA1_ngf2CA1_aac = {
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
CA1_olm2CA1_aac = {
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
CA1_bis2CA1_aac = {
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
CA1_ivy2CA1_aac = {
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
CA3_pyr2CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_pvbas",
    "tau_f": 29.69023481,
    "tau_r": 440.119068,
    "tau_d": 5.394005967,
    "Uinc": 0.198996085,
    "gbarS": 0.908653493,
    "Erev": 0.0,
}
CA1_pyr2CA1_pvbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr",
    "post_name": "CA1_pvbas",
    "tau_f": 76.85776536,
    "tau_r": 327.2596661,
    "tau_d": 3.163416515,
    "Uinc": 0.200078943,
    "gbarS": 1.350968596,
    "Erev": 0.0,
}
EC3_pyr2CA1_pvbas = {
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
CA1_pvbas2CA1_pvbas = {
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
CA1_cckbas2CA1_pvbas = {
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
CA1_ngf2CA1_pvbas = {
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
CA1_olm2CA1_pvbas = {
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
CA1_bis2CA1_pvbas = {
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
CA1_ivy2CA1_pvbas = {
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
CA3_pyr2CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_cckbas",
    "tau_f": 61.43867292,
    "tau_r": 330.9105197,
    "tau_d": 4.833858548,
    "Uinc": 0.226501333,
    "gbarS": 1.215139842,
    "Erev": 0.0,
}
CA1_pyr2CA1_cckbas = {
    "w": 0.5,
    "pre_name": "CA1_pyr",
    "post_name": "CA1_cckbas",
    "tau_f": 200.0945674,
    "tau_r": 170.3265276,
    "tau_d": 2.77089926,
    "Uinc": 0.248751595,
    "gbarS": 1.889612224,
    "Erev": 0.0,
}
EC3_pyr2CA1_cckbas = {
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
CA1_pvbas2CA1_cckbas = {
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
CA1_cckbas2CA1_cckbas = {
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
CA1_ngf2CA1_cckbas = {
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
CA1_olm2CA1_cckbas = {
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
CA1_bis2CA1_cckbas = {
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
CA1_ivy2CA1_cckbas = {
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
EC3_pyr2CA1_ngf = {
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
CA1_ngf2CA1_ngf = {
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
CA1_olm2CA1_ngf = {
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
CA3_pyr2CA1_olm = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_olm",
    "tau_f": 38.22553135,
    "tau_r": 358.2571628,
    "tau_d": 5.430321889,
    "Uinc": 0.102925387,
    "gbarS": 0.866891054,
    "Erev": 0.0,
}
CA1_pyr2CA1_olm = {
    "w": 0.5,
    "pre_name": "CA1_pyr",
    "post_name": "CA1_olm",
    "tau_f": 106.9783405,
    "tau_r": 202.0650489,
    "tau_d": 2.947716244,
    "Uinc": 0.089607609,
    "gbarS": 1.699075536,
    "Erev": 0.0,
}
CA1_bis2CA1_olm = {
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
CA1_ivy2CA1_olm = {
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
CA3_pyr2CA1_bis = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_bis",
    "tau_f": 27.56437073,
    "tau_r": 369.3806703,
    "tau_d": 6.184627383,
    "Uinc": 0.213215335,
    "gbarS": 1.150542157,
    "Erev": 0.0,
}
CA1_pyr2CA1_bis = {
    "w": 0.5,
    "pre_name": "CA1_pyr",
    "post_name": "CA1_bis",
    "tau_f": 45.77509046,
    "tau_r": 242.468234,
    "tau_d": 3.394198844,
    "Uinc": 0.225236757,
    "gbarS": 2.155417698,
    "Erev": 0.0,
}
CA1_pvbas2CA1_bis = {
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
CA1_cckbas2CA1_bis = {
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
CA1_bis2CA1_bis = {
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
CA1_ivy2CA1_bis = {
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
CA3_pyr2CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_ivy",
    "tau_f": 22.00501845,
    "tau_r": 419.0888672,
    "tau_d": 6.514490352,
    "Uinc": 0.211997085,
    "gbarS": 1.139035363,
    "Erev": 0.0,
}
CA1_pyr2CA1_ivy = {
    "w": 0.5,
    "pre_name": "CA1_pyr",
    "post_name": "CA1_ivy",
    "tau_f": 29.98390368,
    "tau_r": 294.5593265,
    "tau_d": 3.90415446,
    "Uinc": 0.223851273,
    "gbarS": 2.125086979,
    "Erev": 0.0,
}
CA1_pvbas2CA1_ivy = {
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
CA1_cckbas2CA1_ivy = {
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
CA1_bis2CA1_ivy = {
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
CA1_ivy2CA1_ivy = {
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
EC3_pyr2CA1_ivy = {
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
CA3_pyr2CA1_ngf = {
    "w": 0.5,
    "pre_name": "CA3_pyr",
    "post_name": "CA1_ngf",
    "tau_f": 50.35427898,
    "tau_r": 345.1417744,
    "tau_d": 4.255231343,
    "Uinc": 0.218766637,
    "gbarS": 1.650136928,
    "Erev": 0.0,
}
CA1_ivy2CA1_ngf = {
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
DG_granular_cells = [DG_granule_soma_background_params, DG_granule_dend_background_params, \
                     DG_granule_soma_active1_params, DG_granule_dend_active1_params, \
                     DG_granule_soma_active2_params, DG_granule_dend_active2_params, \
                     DG_granule_soma_active3_params, DG_granule_dend_active3_params, \
                     DG_granule_soma_active4_params, DG_granule_dend_active4_params, \
                     DG_granule_soma_active5_params, DG_granule_dend_active5_params ]


CA3_pyr_cells = [CA3_pyr_soma_background_params, CA3_pyr_dend_background_params, \
                 CA3_pyr_soma_active1_params, CA3_pyr_dend_active1_params, \
                 CA3_pyr_soma_active2_params, CA3_pyr_dend_active2_params, \
                 CA3_pyr_soma_active3_params, CA3_pyr_dend_active3_params, \
                 CA3_pyr_soma_active4_params, CA3_pyr_dend_active4_params, \
                 CA3_pyr_soma_active5_params, CA3_pyr_dend_active5_params ]

CA1_pyr_cells = [CA1_pyr_soma_background_params, CA1_pyr_dend_background_params, \
                 CA1_pyr_soma_active1_params, CA1_pyr_dend_active1_params, \
                 CA1_pyr_soma_active2_params, CA1_pyr_dend_active2_params, \
                 CA1_pyr_soma_active3_params, CA1_pyr_dend_active3_params, \
                 CA1_pyr_soma_active4_params, CA1_pyr_dend_active4_params, \
                 CA1_pyr_soma_active5_params, CA1_pyr_dend_active5_params ]

# dg_cells = [DG_mossy_params, DG_aac_params, DG_cckbas_params, DG_pvbas_params]
#
#
# params_neurons = [CA3_pyr_params, CA3_aac_params, CA3_pvbas_params, CA3_cckbas_params, CA3_olm_params, CA1_pvbas_params, CA1_olm_params, CA1_cckbas_params, CA1_bis_params, CA1_aac_params, CA1_ivy_params, CA1_ngf_params],
#
# params_net = {
# "params_neurons" : params_neurons,
# "params_generators" : [CA1_pyr_params, EC3_pyr_params, EC2_stellate_params],
# "params_synapses" : [CA1_pyr_2_CA1_pyr, CA3_pyr_2_CA1_pyr, EC3_pyr_2_CA1_pyr, CA1_aac_2_CA1_pyr, CA1_pvbas_2_CA1_pyr, CA1_cckbas_2_CA1_pyr, CA1_bis_2_CA1_pyr, CA1_ivy_2_CA1_pyr, CA1_olm_2_CA1_pyr, CA1_ngf_2_CA1_pyr, CA3_pyr_2_CA1_aac, CA1_pyr_2_CA1_aac, EC3_pyr_2_CA1_aac, CA1_pvbas_2_CA1_aac, CA1_cckbas_2_CA1_aac, CA1_ngf_2_CA1_aac, CA1_olm_2_CA1_aac, CA1_bis_2_CA1_aac, CA1_ivy_2_CA1_aac, CA3_pyr_2_CA1_pvbas, CA1_pyr_2_CA1_pvbas, EC3_pyr_2_CA1_pvbas, CA1_pvbas_2_CA1_pvbas, CA1_cckbas_2_CA1_pvbas, CA1_ngf_2_CA1_pvbas, CA1_olm_2_CA1_pvbas, CA1_bis_2_CA1_pvbas, CA1_ivy_2_CA1_pvbas, CA3_pyr_2_CA1_cckbas, CA1_pyr_2_CA1_cckbas, EC3_pyr_2_CA1_cckbas, CA1_pvbas_2_CA1_cckbas, CA1_cckbas_2_CA1_cckbas, CA1_ngf_2_CA1_cckbas, CA1_olm_2_CA1_cckbas, CA1_bis_2_CA1_cckbas, CA1_ivy_2_CA1_cckbas, EC3_pyr_2_CA1_ngf, CA1_ngf_2_CA1_ngf, CA1_olm_2_CA1_ngf, CA3_pyr_2_CA1_olm, CA1_pyr_2_CA1_olm, CA1_bis_2_CA1_olm, CA1_ivy_2_CA1_olm, CA3_pyr_2_CA1_bis, CA1_pyr_2_CA1_bis, CA1_pvbas_2_CA1_bis, CA1_cckbas_2_CA1_bis, CA1_bis_2_CA1_bis, CA1_ivy_2_CA1_bis, CA3_pyr_2_CA1_ivy, CA1_pyr_2_CA1_ivy, CA1_pvbas_2_CA1_ivy, CA1_cckbas_2_CA1_ivy, CA1_bis_2_CA1_ivy, CA1_ivy_2_CA1_ivy, EC3_pyr_2_CA1_ivy, CA3_pyr_2_CA1_ngf, CA1_ivy_2_CA1_ngf, ],
# }
