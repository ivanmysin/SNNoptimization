import sys
sys.path.append("../")
import matplotlib.pyplot as plt
import networkx as nx
from code_generated_params import params_net
G = nx.DiGraph()
plotting_param = {
    "neuron_colors" : {
        "ca1pyr" : (1.0, 0.0, 0.0), # red
        "pvbas": (0.0, 0.0, 1.0), # blue
        "olm": (0.0, 0.0, 0.5), #
        "cckbas": (0.0, 1.0, 0.0), # green
        "ivy": (0.0, 0.5, 0.5), #
        "ngf": (0.5, 0.5, 0.5), #
        "bis": (0.1, 0.0, 0.5), #
        "aac": (1.0, 0.0, 0.5), #
        "sca": (0.0, 1.0, 0.5), #

        "ca3pyr": (0.5, 0.5, 0.0), #
        "ec3": (0.5, 1.0, 0.0), #
        "lec": (0.9, 0.7, 0.0), #
        "msteevracells": (0.0, 0.8, 0.5), #
        "mskomalicells": (0.0, 0.5, 0.9), #
        "msach": (0.8, 0.2, 0.0), #
    },
}

colors = []

for neuron in params_net["params_neurons"]:
    G.add_node(neuron["name"])
    colors.append(plotting_param["neuron_colors"][neuron["name"]])

for neuron in params_net["params_generators"]:
    G.add_node(neuron["name"], node_color=plotting_param["neuron_colors"][neuron["name"]])
    colors.append(plotting_param["neuron_colors"][neuron["name"]])

for syn in params_net["params_synapses"]:
    G.add_edge(syn['pre_name'], syn['post_name'])


pos = nx.circular_layout(G)
fig, axes = plt.subplots(figsize=(10, 10))
nx.draw(G, pos, node_size=10000, node_color=colors, edge_color='b', with_labels=True, font_size=28, font_color='w')
# node_opts = {"node_size": 500, "node_color": "w", "edgecolors": "k", "linewidths": 2.0}
# nx.draw_networkx_nodes(G, **node_opts)
#nx.draw_networkx_labels(G, font_size=14)
fig.savefig('/home/ivan/ConnGraph.png')
plt.show()