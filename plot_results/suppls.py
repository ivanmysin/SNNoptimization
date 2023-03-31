import numpy as np
import pickle
import pandas as pd
path2saving = '/home/ivan/Data/phase_relations/supplement/'
with open('/home/ivan/Data/Opt_res/LIF_params_net.pickle', 'rb') as file:
    params_net = pickle.load(file)

names = [n["name"] for n in params_net["params_generators"]]
neurons_names = [n["name"] for n in params_net["params_neurons"]]
names.extend(neurons_names)

syn_params = list(params_net["params_synapses"][0].keys())
syn_params.remove("pre_name")
syn_params.remove("post_name")

for syn_param in syn_params:
    table = pd.DataFrame(columns=neurons_names, index=names)

    for syn in params_net["params_synapses"]:
        table[syn['post_name']].loc[syn['pre_name']] = syn[syn_param]
    table = table.replace(np.nan, "-")
    print(table)

    filepath = path2saving + syn_param + '.csv'
    table.to_csv(filepath, index_label="presynaptic", header=True, encoding='utf-8')


table = pd.DataFrame(columns=neurons_names, index=["Iext", ])
for neuron in params_net["params_neurons"]:

    table[neuron['name']].loc["Iext"] = neuron['Iext']

print(table)

filepath = path2saving + 'Iext.csv'
table.to_csv(filepath, header=True, encoding='utf-8')

target_params = list(params_net["params_neurons"][0]["target"].keys())
table = pd.DataFrame(columns=target_params, index=names)
for neuron in params_net["params_generators"]:
    for target_param in target_params:
        table[target_param].loc[neuron['name']] = np.around( neuron[target_param], 2)

for neuron in params_net["params_neurons"]:
    for target_param in target_params:
        table[target_param].loc[neuron['name']] = np.around(neuron['target'][target_param], 2)

filepath = '/home/ivan/Data/phase_relations/targets.tex'
table.to_latex(filepath, header=True, encoding='utf-8')
