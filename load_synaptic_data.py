import pandas as pd
from collections import OrderedDict
filepath = "mean_connection.txt"
start_code = r"""########################################
import neuron_models
##### block of neurons params #########
## DG neurons
DG_granule_soma_params = {
    "name": "DG_granule_soma",
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

DG_granule_dend_params = {
    "name": "DG_granule_dend",
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
#########################333
# CA3 neurons
CA3_pyr_soma_params = {
    "name": "CA3_pyr_soma",
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

CA3_pyr_dend_params = {
    "name": "CA3_pyr_dend",
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

##########################################
##### block of generators params #########
msteevra_params = {
    "name" : "msteevra_params",
    "R": 0.6,
    "freq": 5,
    "mean_spike_rate": 50,
    "phase": 1.58,
}

ec2_params = {
    "name" : "ec2",
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 0.5,
    "phase": 3.14,
}

ec3_params = {
    "name" : "ec3",
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 0.5,
    "phase": -1.57,
}

########################################
##### block of synapses params #########
"""

neurons_names = OrderedDict()
neurons_names["DG Granule (+)2201p"] = "DG_granule"
neurons_names["DG Mossy (+)0103"] = "DG_mossy"
neurons_names["DG Axo-Axonic (-)2233"] = "DG_aac"
neurons_names["DG Basket CCK+ (-)2232"] = "DG_cckbas"
neurons_names["DG Basket (-)2232"] = "DG_pvbas"

neurons_names["CA3 Pyramidal (+)23223p"] = "CA3_pyr"
neurons_names["CA3 Axo-Axonic (-)22232"] = "CA3_aac"
neurons_names["CA3 Basket (-)22232"] = "CA3_pvbas"
neurons_names["CA3 Basket CCK+ (-)22232"] = "CA3_cckbas"
neurons_names["CA3 O-LM (-)11003"] = "CA3_olm"


neurons_names["CA1 Basket (-)2232"] = "CA1_pvbas"
neurons_names["CA1 O-LM (-)1002"] = "CA1_olm"
neurons_names["CA1 Basket CCK+ (-)2232"] = "CA1_cckbas"
neurons_names["CA1 Bistratified (-)0333"] = "CA1_bis"
neurons_names["CA1 Axo-Axonic (-)2232"] =  "CA1_aac"
neurons_names["CA1 Ivy (-)0333"] = "CA1_ivy"
neurons_names["CA1 Neurogliaform (-)3000"] = "CA1_ngf"


neurons_names["CA1 Pyramidal (+)2223p"] = "CA1_pyr"
neurons_names["EC LIII Pyramidal (+)223111p"] = "EC3_pyr"
neurons_names["MEC LII Stellate (+)331111p"] = "EC2_stellate"



neurons_names_keys_list = list(neurons_names.keys())

data = pd.read_csv(filepath, delimiter="\t")


code_full = ""
code_template = """{:s}_2_{:s} = {{
    \"w\": {Weight},
    \"pre_name\": \"{pre}\",
    \"post_name\": \"{post}\",
    \"tau_f\": {tau_f},
    \"tau_r\": {tau_r},
    \"tau_d\": {tau_d},
    \"Uinc\": {Uinc},
    \"gbarS\": {gbarS},
    \"Erev\": {Erev},
}}
"""
code4synlist = "\"params_synapses\" : ["

two_comps = ['DG_granule', 'CA3_pyr', 'CA1_pyr']
two_comps_names = ['backgrond', 'active1','active2','active3','active4','active5',]
dend_target = ['EC3_pyr', 'EC2_stellate', 'CA1_ivy', 'CA1_ngf', 'CA1_olm', 'CA3_olm']

indexes_by_condiion = []
for idx in range(len(data)):
    presyncell = data["Presynaptic Neuron"][idx]
    postsyncell = data["Postsynaptic Neuron"][idx]

    try:
        if neurons_names[postsyncell] in ['EC3_pyr', 'EC2_stellate']:
            continue
    except KeyError:
        continue

    if (presyncell in neurons_names.keys()) and (postsyncell in neurons_names.keys()):
        if neurons_names[presyncell] in two_comps:
            pre_names = []
            for two_comps_name in two_comps_names:
                pre_names.append( neurons_names[presyncell] + "_soma_" + two_comps_name)
        else:
            pre_names = [neurons_names[presyncell], ]

        if neurons_names[postsyncell] in two_comps:
            post_names = []
            for two_comps_name in two_comps_names:
                if pre_names[0] in dend_target:
                    post_names.append(neurons_names[postsyncell] + "_dend_" + two_comps_name)
                else:
                    post_names.append( neurons_names[postsyncell] + "_soma_" + two_comps_name)
        else:
            post_names = [neurons_names[postsyncell], ]

        for pre_name in pre_names:
            for post_name in post_names:


                indexes_by_condiion.append(idx)

                if presyncell.find("(-)") != -1:
                    Erev = -75.0
                    Weight = 0.1
                    gbarS_coeff = 1.0
                else:
                    Erev = 0.0
                    Weight = 0.5
                    gbarS_coeff = 1.0


                code = code_template.format(pre_name, post_name, \
                                             Weight = Weight,\
                                             pre = pre_name, \
                                             post = post_name, \
                                             tau_f = data["tau_f"][idx], \
                                             tau_r = data["tau_r"][idx], \
                                             tau_d = data["tau_d"][idx], \
                                             Uinc = data["U"][idx],\
                                             gbarS = gbarS_coeff * data["g"][idx],
                                             Erev=Erev)

                code_full += code

                #code4synlist += pre_name + "_2_" + post_name + ", "

short_names = []
for short_name in neurons_names.values():
    short_names.append(short_name + "_params")

code4neurons = "\"params_neurons\" : [" + ", ".join(short_names[:-3]) + "],\n"
code4generators = "\"params_generators\" : [" + ", ".join(short_names[-3:]) + "],\n"
code4synlist += "],\n"
#print(code4neurons)
#print(code4generators)
code_full += start_code + "params_net = {\n" + code4neurons + code4generators + code4synlist + "}\n"

file4code = open("/home/ivan/Data/hippocampome/full_hippocampus_code_generated_params.txt", mode="w")
file4code.write(code_full)
file4code.close()





