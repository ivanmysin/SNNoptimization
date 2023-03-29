import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from plotting_params import plotting_colors

import sys
sys.path.append("../")
from code_generated_params import params_net


def plot_connection_graph(ax):
    G = nx.DiGraph()
    colors = []
    for neuron in params_net["params_neurons"]:
        G.add_node(neuron["name"])
        colors.append(plotting_colors["neuron_colors"][neuron["name"]])

    for neuron in params_net["params_generators"]:
        G.add_node(neuron["name"], node_color=plotting_colors["neuron_colors"][neuron["name"]])
        colors.append(plotting_colors["neuron_colors"][neuron["name"]])

    for syn in params_net["params_synapses"]:
        G.add_edge(syn['pre_name'], syn['post_name'], color=plotting_colors["neuron_colors"][syn['pre_name']])

    edge_colors = nx.get_edge_attributes(G,'color').values()
    pos = nx.circular_layout(G)
    nx.draw(G, pos, ax=ax, node_size=5000, node_color=colors, \
            edge_color=edge_colors, with_labels=True, \
            font_size=14, font_color='w', \
            arrowsize=20, connectionstyle='arc3,rad=0.2')
#######################################################################################
fig, axes = plt.subplots(constrained_layout=True, figsize=(10, 10))
plot_connection_graph(axes)

fig.savefig('/home/ivan/Data/phase_relations/figures/Fig_1.png')
plt.show()

