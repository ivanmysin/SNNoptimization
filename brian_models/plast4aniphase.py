from brian2 import *
import sympy
import numpy as np
import matplotlib.pyplot as plt
seed(11922)  # to get identical figures for repeated runs
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
plt.rcParams.update(params)

################################################################################
# Model parameters
################################################################################
### General parameters
duration = 1.0*second  # Total simulation time
sim_dt = 0.1*ms        # Integrator/sampling step
N_e = 200             # Number of excitatory neurons
N_i = 200              # Number of inhibitory neurons

### Neuron parameters
E_l = -60*mV           # Leak reversal potential
g_l = 9.99*nS          # Leak conductance
E_e = 0*mV             # Excitatory synaptic reversal potential
E_i = -80*mV           # Inhibitory synaptic reversal potential
C_m = 198*pF           # Membrane capacitance
tau_e = 5*ms           # Excitatory synaptic time constant
tau_i = 10*ms          # Inhibitory synaptic time constant
tau_r = 5*ms           # Refractory period
I_ex = 150*pA          # External current
V_th = -50*mV          # Firing threshold
V_r = E_l              # Reset potential

### Synapse parameters
w_e = 0.05*nS          # Excitatory synaptic conductance
w_i = 1.0*nS # 1.0*nS           # Inhibitory synaptic conductance
U_0 = 0.6              # Synaptic release probability at rest
Omega_d = 2.0/second   # Synaptic depression rate
Omega_f = 3.33/second  # Synaptic facilitation rate

################################################################################
# Model definition
################################################################################
# Set the integration time (in this case not strictly necessary, since we are
# using the default value)
defaultclock.dt = sim_dt

### Neurons
neuron_eqs = '''
dv/dt = (g_l*(E_l-v) + g_e*(E_e-v) + g_i*(E_i-v) +
         I_ex)/C_m    : volt (unless refractory)
dg_e/dt = -g_e/tau_e  : siemens  # post-synaptic exc. conductance
dg_i/dt = -g_i/tau_i  : siemens  # post-synaptic inh. conductance
'''
neurons = NeuronGroup(N_e + N_i, model=neuron_eqs,
                      threshold='v>V_th', reset='v=V_r',
                      refractory='tau_r', method='euler')
# Random initial membrane potential values and conductances
neurons.v = 'E_l + randn()*(V_th-E_l)'
neurons.g_e = 'rand()*w_e'
neurons.g_i = 'rand()*w_i'
exc_neurons = neurons[:N_e]
inh_neurons = neurons[N_e:]

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

exc_syn = Synapses(exc_neurons, inh_neurons, model=synapses_eqs,
                   on_pre=synapses_action+'g_i_post += w_i*r_S')

inh_syn = Synapses(inh_neurons, exc_neurons, model=synapses_eqs,
                   on_pre=synapses_action+'g_i_post += w_i*r_S')

exc_syn.connect(p=0.5)
inh_syn.connect(p=0.5)
# Start from "resting" condition: all synapses have fully-replenished
# neurotransmitter resources
exc_syn.x_S = 1
inh_syn.x_S = 1

# ##############################################################################
# # Monitors
# ##############################################################################
# Note that we could use a single monitor for all neurons instead, but in this
# way plotting is a bit easier in the end
#exc_mon = SpikeMonitor(exc_neurons)
#inh_mon = SpikeMonitor(inh_neurons)
SpM = SpikeMonitor(neurons)


# ### We record some additional data from a single excitatory neuron
# ni = 50
# # Record conductances and membrane potential of neuron ni
state_mon1 = StateMonitor(exc_neurons, ['v', 'g_i'], record=np.arange(200))
state_mon2 = StateMonitor(inh_neurons, ['v', 'g_i'], record=np.arange(200))
# # We make sure to monitor synaptic variables after synapse are updated in order
# # to use simple recurrence relations to reconstruct them. Record all synapses
# # originating from neuron ni
# synapse_mon = StateMonitor(exc_syn, ['u_S', 'x_S'],
#                            record=exc_syn[ni, :], when='after_synapses')



# ##############################################################################
# # Simulation run
# ##############################################################################
run(duration, report='text')

mean_con1 = np.sum( (state_mon1.g_i / mS), axis=0)
mean_con2 = np.sum( (state_mon2.g_i / mS), axis=0)

fig, axes = plt.subplots(nrows=3, figsize=(15, 8), sharex=True)
axes[0].scatter(SpM.t / ms, SpM.i, s=5, color="green")
axes[0].set_ylabel('Neuron index')

axes[1].plot(state_mon1.t/ms, mean_con1, linewidth=5, color="blue")
axes[1].set_ylabel('Mean synaptic \n conductance, mS')
axes[2].plot(state_mon2.t/ms, mean_con2, linewidth=5, color="blue")
axes[2].set_ylabel('Mean synaptic \n conductance, mS')
axes[2].set_xlabel('Time (ms)')

fig.savefig('/home/ivan/Документы/Тезисы/Fig_2Pop.png')
show()
