from brian2 import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
seed(11922)  # to get identical figures for repeated runs
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large',
          }
plt.rcParams.update(params)

TEXTFONTSIZE = 'xx-large'
################################################################################
### General parameters
duration = 1.5*second  # Total simulation time
sim_dt = 0.05*ms        # Integrator/sampling step
N_1 = 200             # Number of excitatory neurons
N_2 = 200              # Number of inhibitory neurons
N = N_1 + N_2
defaultclock.dt = sim_dt
################################################################################
# Model parameters
### Neuron parameters
Cm = 1 * uF  # /cm**2
Iext = -1.0*uA
gL = 0.18 * msiemens
EL = -60 * mV
ENa = 55 * mV
EK = -90 * mV
E_inhsyn = -75*mV
gNa = 50 * mS  # 150*msiemens
gK = 23 * msiemens
gKA = 10 * msiemens
sigma = 0.4 * mV

# tau_e = 5*ms           # Excitatory synaptic time constant
tau_i = 10*ms          # Inhibitory synaptic time constant
tau_r = 5*ms           # Refractory period


### Synapse parameters
w_i = 15.0*uS # 1.0*nS           # Inhibitory synaptic conductance
U_0 = 0.6              # Synaptic release probability at rest
Omega_d = 2.0/second   # Synaptic depression rate
Omega_f = 3.33/second  # Synaptic facilitation rate

################################################################################
# Model definition
################################################################################
# Interneuron Model with A-current
eqs = '''
dV/dt = (INa + IKdr + IL + IA + Iext + Isyn)/Cm + sigma*xi/ms**0.5 : volt
IL = gL*(EL - V)           : ampere
INa = gNa*m**3*h*(ENa - V) : ampere
IKdr = gK*n**4*(EK - V) : ampere
IA = gKA * a * b * (EK - V) :  ampere

m = alpha_m/(alpha_m+beta_m) : 1
alpha_m = 1.0 / exprel(-(V+40*mV)/(10*mV))/ms : Hz
beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms : Hz
dh/dt = (alpha_h*(1-h)-beta_h*h) : 1
alpha_h = 0.07*exp(-(V+65*mV)/(20*mV))/ms : Hz
beta_h = 1./(exp(-0.1/mV*(V+35*mV))+1)/ms : Hz
# dn/dt = (alpha_n*(1-n)-beta_n*n) : 1
# alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
# beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz

dn/dt = (n_inf - n) / tau_n : 1
tau_n = 0.5*ms + 2.0*ms/(1 + exp(0.045/mV * (V - 50*mV))) : second
n_inf = 1.0 / (1.0 + exp(-0.045 * (V/mV + 10))) : 1 

da/dt = (alpha_a*(1-a)-beta_a*a) : 1
alpha_a = 0.2 / exprel( (13.1*mV - V)/(10*mV))/ms : Hz
beta_a = 0.175 / exprel( (V - 40.1*mV)/(10*mV))/ms : Hz


db/dt = (alpha_b*(1-b)-beta_b*b) : 1
alpha_b = 0.0016 * exp( (-13*mV - V) / (18*mV) ) /ms : Hz
beta_b = 0.05 / (1 + exp( (10.1*mV - V)/(5*mV) ) ) /ms : Hz

Isyn = g_i * (E_inhsyn - V) : ampere
dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
'''

neurons = NeuronGroup(N, eqs, method='heun', threshold='V > -5*mV', refractory=tau_r)

neurons.n = 0.09
neurons.h = 1.0
neurons.a = 0.0
neurons.b = 0.9

# Random initial membrane potential values and conductances
neurons.g_i = 'rand()*w_i'

inh1_neurons = neurons[:N_1]
inh2_neurons = neurons[N_1:]

inh1_neurons.V = 'EL + randn()*mV'
inh1_neurons.V = '-90*mV + randn()*mV'

### Synapses
synapses_eqs = '''
# Usage of releasable neurotransmitter per single action potential:
du_S/dt = -Omega_f * u_S     : 1 (event-driven)
# Fraction of synaptic neurotransmitter resources available:
dx_S/dt = Omega_d *(1 - x_S) : 1 (event-driven)
'''

synapses_action = '''
u_S += U_0 * (1 - u_S)
r_S = u_S * x_S
x_S -= r_S
'''

inh_syn1_2 = Synapses(inh1_neurons, inh2_neurons, model=synapses_eqs,
                   on_pre=synapses_action+'g_i_post += w_i*r_S')

inh_syn2_1 = Synapses(inh2_neurons, inh1_neurons, model=synapses_eqs,
                   on_pre=synapses_action+'g_i_post += w_i*r_S')

inh_syn1_2.connect(p=0.5)
inh_syn2_1.connect(p=0.5)
# Start from "resting" condition: all synapses have fully-replenished
# neurotransmitter resources
inh_syn2_1.x_S = 1
inh_syn1_2.x_S = 1

# ##############################################################################
# # Monitors
# ##############################################################################
# Note that we could use a single monitor for all neurons instead, but in this
# way plotting is a bit easier in the end
Sp1M = SpikeMonitor(inh1_neurons)
Sp2M = SpikeMonitor(inh2_neurons)


# ### We record some additional data from a single excitatory neuron
# # Record conductances and membrane potential of neuron ni
state_mon1 = StateMonitor(inh1_neurons, ['V', 'g_i'], record=np.arange(N_1))
state_mon2 = StateMonitor(inh2_neurons, ['V', 'g_i'], record=np.arange(N_2))

# ##############################################################################
# # Simulation run
# ##############################################################################
run(duration, report='text')

mean_con1 = np.mean( (state_mon1.g_i / uS), axis=0)
mean_con2 = np.mean( (state_mon2.g_i / uS), axis=0)

spike_rate_1, bins = np.histogram(Sp1M.t / ms, bins=10*int(duration/ms)+1, density=False, range=[0, duration/ms+1])
dbins = bins[1] - bins[0]
spike_rate_1 = spike_rate_1 / (0.001 * N_1 * dbins)

spike_rate_2, bins = np.histogram(Sp2M.t / ms, bins=10*int(duration/ms)+1, density=False, range=[0, duration/ms+1])
spike_rate_2 = spike_rate_2 / (0.001 * N_2 * dbins)

# fig, axes = plt.subplots(nrows=2, constrained_layout=True, figsize=(15, 10))
# axes[0].plot(state_mon1.V[10]/mV)
# axes[1].plot(state_mon2.V[10]/mV)

plt.show()

gridspec_kw = {
    "width_ratios" : [0.3, 0.5, 0.1],
}

fig, axes = plt.subplots(nrows=6, ncols=3, gridspec_kw=gridspec_kw, constrained_layout=True, figsize=(15, 10))
for ax in axes[:, 2]:
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# axes[0, 1].set_title('Raster plots')
axes[0, 2].text(0, 0.5, 'Raster plots \n of population 1', fontsize=TEXTFONTSIZE )
axes[0, 1].scatter(Sp1M.t / ms, Sp1M.i, s=5, color="green")
axes[0, 1].set_ylabel('Neuron \n index')
axes[1, 2].text(0, 0.5, 'Raster plots \n of population 2', fontsize=TEXTFONTSIZE )
axes[1, 1].scatter(Sp2M.t / ms, Sp2M.i, s=5, color="blue")
axes[1, 1].set_ylabel('Neuron \n index')

#axes[2, 1].set_title('Firing rates')
axes[2, 2].text(0, 0.5, 'Firing rates \n of population 1', fontsize=TEXTFONTSIZE )
axes[2, 1].plot(bins[:-1], spike_rate_1, color="green", linewidth=5)
axes[2, 1].set_ylabel('spikes/sec')
axes[2, 1].set_ylim(0, 400)
axes[3, 2].text(0, 0.5, 'Firing rates \n of population 2', fontsize=TEXTFONTSIZE )
axes[3, 1].plot(bins[:-1], spike_rate_2, color="blue", linewidth=5)
axes[3, 1].set_ylabel('spikes/sec')
axes[3, 1].set_ylim(0, 400)

axes[4, 1].plot(state_mon1.t/ms, mean_con1, linewidth=5, color="green")
axes[4, 1].set_ylim(0, 250)
axes[4, 1].set_ylabel('uS')
#axes[4, 1].set_title('Mean synaptic conductance on population 1')
axes[4, 2].text(0, 0.5, 'Mean synaptic conductance \n on population 1', fontsize=TEXTFONTSIZE )

axes[5, 1].plot(state_mon2.t/ms, mean_con2, linewidth=5, color="blue")
axes[5, 1].set_ylim(0, 250)
axes[5, 1].set_ylabel('uS')
#axes[5, 1].set_title('Mean synaptic conductance on population 2')
axes[5, 2].text(0, 0.5, 'Mean synaptic conductance \n on population 2', fontsize=TEXTFONTSIZE )

axes[-1, 1].set_xlabel('Time (ms)')

for ax in axes[:, 1]:
    ax.set_xlim(200, duration/ms)

gs = axes[0, 0].get_gridspec()
for ax in axes[:, 0]:
    ax.remove()
axbig = fig.add_subplot(gs[:, 0])
axbig.set_xlim(-1, 1)
axbig.set_ylim(-1, 1)

G = nx.DiGraph()
G.add_node("1")
G.add_node("2")
G.add_edge("1", "2")
G.add_edge("2", "1")
pos = {"1": [0, -0.5], "2": [0, 0.5],}
nx.draw(G, ax=axbig, pos=pos, node_size=5000, \
        node_color=['blue', 'green'], edge_color='k',\
        with_labels=True, font_size=14, font_color='w', \
        arrowsize = 20, connectionstyle = 'arc3,rad=0.2')



fig.savefig('/home/ivan/Data/phase_relations/figures/Fig_1.png')
plt.show()
