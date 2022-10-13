import pandas as pd
from collections import OrderedDict
filepath = "/home/ivan/Data/hippocampome/mean_connection.txt"
start_code = r"""########################################
##### block of neurons params #########
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
        "mean_spike_rate": 50.0,
        "phase": 1.5707963267948966,
    },
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
    
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 50.0,
        "phase": 3.14,
    },
}

cckbas_params = {
    "name" : "cckbas",
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
    "dts": 0.5,
    
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 50.0,
        "phase": -1.5707963267948966,
    },
}

bis_params = {
    "name" : "bis",
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
    "dts": 0.5,
    
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 50.0,
        "phase": 3.141592653589793,
    },
}

aac_params = {
    "name" : "aac",
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
        "mean_spike_rate": 50.0,
        "phase": 0.0,
    },
}

ivy_params = {
    "name" : "ivy",
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
    "dts": 0.5,
    
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 50.0,
        "phase": -1.5707963267948966,
    },
}

ngf_params = {
    "name" : "ngf",
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
    "dts": 0.5,
    
    "target" : {
        "R": 0.3,
        "freq": 5,
        "mean_spike_rate": 50.0,
        "phase": 0.0,
    },
}

##########################################
##### block of generators params #########
ca3pyr_params = {
    "name" : "ca3pyr",
    "R": 0.3,
    "freq": 5,
    "mean_spike_rate": 5,
    "phase": 1.58,
}

ca1pyr_params = {
    "name" : "ca1pyr",
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 5,
    "phase": 3.14,
}

ec3_params = {
    "name" : "ec3",
    "R": 0.2,
    "freq": 5,
    "mean_spike_rate": 5,
    "phase": -1.57,
}

########################################
##### block of synapses params #########
"""

neurons_names = OrderedDict()
neurons_names["CA1 Basket (-)2232"] = "pvbas"
neurons_names["CA1 O-LM (-)1002"] = "olm"
neurons_names["CA1 Basket CCK+ (-)2232"] = "cckbas"
neurons_names["CA1 Bistratified (-)0333"] = "bis"
neurons_names["CA1 Axo-Axonic (-)2232"] =  "aac"
neurons_names["CA1 Ivy (-)0333"] = "ivy"
neurons_names["CA1 Neurogliaform (-)3000"] = "ngf"

neurons_names["CA3 Pyramidal (+)23223p"] = "ca3pyr"
neurons_names["CA1 Pyramidal (+)2223p"] = "ca1pyr"
neurons_names["EC LIII Pyramidal (+)223111p"] = "ec3"



neurons_names_keys_list = list(neurons_names.keys())

data = pd.read_csv(filepath, delimiter="\t")

code_full = ""
code_template = """{:s}2{:s} = {{
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

indexes_by_condiion = []
for idx in range(len(data)):
    presyncell = data["Presynaptic Neuron"][idx]
    postsyncell = data["Postsynaptic Neuron"][idx]

    # if presyncell.find("CA1 ") != -1 and postsyncell.find("CA1 ") != -1:
    #     print(presyncell, postsyncell)

    if (presyncell in neurons_names.keys()) and (postsyncell in neurons_names.keys() and postsyncell.find("CA1") != -1 and neurons_names[postsyncell] != "ca1pyr"):
        #print(presyncell, postsyncell)
        indexes_by_condiion.append(idx)

        if presyncell.find("(-)") != -1:
            Erev = -75.0
            Weight = 0.1
            gbarS_coeff = 1.0
        else:
            Erev = 0.0
            Weight = 0.5
            gbarS_coeff = 1.0


        code = code_template.format(neurons_names[presyncell], neurons_names[postsyncell], \
                                     Weight = Weight,\
                                     pre = neurons_names[presyncell], \
                                     post = neurons_names[postsyncell], \
                                     tau_f = data["tau_f"][idx], \
                                     tau_r = data["tau_r"][idx], \
                                     tau_d = data["tau_d"][idx], \
                                     Uinc = data["U"][idx],\
                                     gbarS = gbarS_coeff * data["g"][idx],
                                     Erev=Erev)

        code_full += code

        code4synlist += neurons_names[presyncell] + "2" + neurons_names[postsyncell] + ", "

short_names = []
for short_name in neurons_names.values():
    short_names.append(short_name + "_params")

code4neurons = "\"params_neurons\" : [" + ", ".join(short_names[:-3]) + "],\n"
code4generators = "\"params_generators\" : [" + ", ".join(short_names[-3:]) + "],\n"
code4synlist += "],\n"
#print(code4neurons)
#print(code4generators)
code_full += start_code + "params_net = {\n" + code4neurons + code4generators + code4synlist + "}\n"

file4code = open("code_generated_params.py", mode="w")
file4code.write(code_full)
file4code.close()





