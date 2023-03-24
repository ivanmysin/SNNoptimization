import numpy as np
import net_lib
from brian2 import *
import matplotlib.pyplot as plt
from plastic_synapse_ode import Synapse
from scipy.signal.windows import parzen
defaultclock.dt = 0.05*ms

generator_params = {
    "name" : "ec3",
    "R": 0.6,
    "freq": 6.0,
    "mean_spike_rate": 15.5, # 5,
    "phase": -1.57,
}

ec32ngf = {
    "W": 1.0,
    "pre_name": "ca3pyr",
    "post_name": "aac",
    "tau_f": 31.42111393,
    "tau_r": 388.4010873,
    "tau_d": 5.516572108,
    "Uinc": 0.203836307,
    "gbarS": 0.991873144,
    "Erev": 0.0,
}

duration = 500 * ms
N = 10000

poisson_input = PoissonGroup(N, rates=net_lib.get_generator_rates(generator_params))
poisson_SkM = SpikeMonitor(poisson_input)


Cm = 1*uF # /cm**2
gL = 0.18 * mS
EL = -70*mV
ENa = 55*mV
EK = -90*mV
gNa = 50 * mS # 50 * msiemens # 150*msiemens
gK = 23 * mS  # 23*msiemens

sigma = 0.3*mV

Esyn = 0*mV

tau_f = ec32ngf["tau_f"]*ms
tau_r = ec32ngf["tau_r"]*ms
tau_d = ec32ngf["tau_d"]*ms

# Interneuron Model without A-current
full_eqs = '''
dV/dt = (INa + IKdr + IL + Iext + Isyn)/Cm : volt
IL = gL*(EL - V)           : ampere
INa = gNa*m**3*h*(ENa - V) : ampere
IKdr = gK*n**4*(EK - V) : ampere
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

Isyn = gsyn*(Esyn - V)    : ampere
gsyn = A_S * 1 * mS : siemens

dU_S/dt = -U_S/tau_f : 1
dR_S/dt = (1 - R_S - A_S) / tau_r : 1
dA_S/dt = -A_S/tau_d : 1
'''

full_neuron = NeuronGroup(1, full_eqs, method='rk4', namespace={"Iext" : 0.0*uA}, threshold='V>-10*mV')
full_neuron.V = -60*mV
full_neuron.n = 0.09
full_neuron.h = 1.0
full_neuron.R_S = 1.0
full_neuron.A_S = 0.0
full_neuron.U_S = 0.0

neuron_mon = StateMonitor(full_neuron, variables=["A_S", "U_S", "R_S", "V"], record=0)

on_pre = """
U_S_post += 0.0001*Uinc*(1 - U_S)
R_S_post -= 0.0001*U_S_post*R_S_post 
A_S_post += 0.0001*U_S_post*R_S_post 
"""
synapse = Synapses(poisson_input, full_neuron, on_pre=on_pre, namespace=ec32ngf)
synapse.connect()

run(duration)


################################
synapse = Synapse(ec32ngf)
y0 = np.asarray([1.0, 0.0, 0.0])
t = np.arange(0, 500.05, 0.05)

# #SRpre = np.zeros_like(t)
# #SRpre[ (poisson_SkM.t/ms / t[1]).astype(np.int32) ] = 1

SRpre, bins = np.histogram(poisson_SkM.t/ms, bins=t)
SRpre = SRpre / N # (0.001 * 0.05) /
SRpre = np.append(SRpre, 0)

kappa, IO = net_lib.r2kappa(generator_params["R"])
gen_input = generator_params["mean_spike_rate"] / IO * np.exp(kappa * np.cos(2*np.pi*0.001*generator_params["freq"]*bins - generator_params["phase"]))
gen_input = gen_input * 0.001 * (bins[1] - bins[0])

win = parzen(101)
win = win / np.sum(win)
SRpre = np.convolve(SRpre, win, mode='same')

solution = synapse.integrate(t, y0, SRpre)


fig, axes = plt.subplots(nrows=5)

#axes.scatter(poisson_SkM.t/ms, poisson_SkM.i)
axes[0].plot(neuron_mon.t/ms, neuron_mon.V[0]/mV)

axes[1].plot(t, solution[:, 1], linewidth=5)
axes[1].plot(neuron_mon.t/ms, neuron_mon.A_S[0], linewidth=2)

axes[2].plot(t, solution[:, 0], linewidth=5)
axes[2].plot(neuron_mon.t/ms, neuron_mon.R_S[0], linewidth=2)

axes[3].plot(t, solution[:, 2], linewidth=5)
axes[3].plot(neuron_mon.t/ms, neuron_mon.U_S[0], linewidth=2)

axes[4].plot(bins, SRpre, linewidth=5)
axes[4].plot(bins, gen_input, linewidth=2)


plt.show()


