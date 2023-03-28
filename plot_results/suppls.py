import numpy as np
import pickle
import pandas as pd
path2saving = '/home/ivan/Data/phase_relations/supplement/'
with open('/home/ivan/Data/Opt_res/LIF_params_net.pickle', 'rb') as file:
    params_net = pickle.load(file)

names = [n["name"] for n in params_net["params_generators"]]
neurons_names = [n["name"] for n in params_net["params_neurons"]]
names.extend(neurons_names)

syn_params = params_net["params_synapses"][0].keys()

for syn_param in syn_params:
    table = pd.DataFrame(columns=neurons_names, index=names)

    for syn in params_net["params_synapses"]:
        table[syn['post_name']].loc[syn['pre_name']] = syn[syn_param]
    table = table.replace(np.nan, "-")
    print(table)

    filepath = path2saving + syn_param + '.csv'
    table.to_csv(filepath, index_label="presynaptic", header=False, encoding='utf-8')