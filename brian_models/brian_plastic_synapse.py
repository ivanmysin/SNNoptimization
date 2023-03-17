import numpy as np
import net_lib
from brian2 import *
import matplotlib.pyplot as plt

generator_params = {
    "name" : "ec3",
    "R": 0.2,
    "freq": 6.0,
    "mean_spike_rate": 5.5, # 5,
    "phase": -1.57,
}
duration = 500 * ms
N = 100

poisson_input = PoissonGroup(N, rates=net_lib.get_generator_rates(generator_params))
poisson_SkM = SpikeMonitor(poisson_input)

defaultclock.dt = 0.1*ms
Cm = 1*uF # /cm**2
gL = 0.18 * mS
EL = -60*mV
ENa = 55*mV
EK = -90*mV
gNa = 50 * mS # 50 * msiemens # 150*msiemens
gK = 23 * mS  # 23*msiemens

sigma = 0.3*mV

Esyn = 0*mV

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
#dn/dt = (alpha_n*(1-n)-beta_n*n) : 1
#alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
#beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz
dn/dt = (n_inf - n) / tau_n : 1
tau_n = 0.5*ms + 2.0*ms/(1 + exp(0.045/mV * (V - 50*mV))) : second
n_inf = 1.0 / (1.0 + exp(-0.045 * (V/mV + 10))) : 1

Isyn = gsyn*(Esyn - V)    : ampere
gsyn = A_S * uS : simens


'''

full_neuron = NeuronGroup(1, full_eqs, method='exponential_euler', namespace={"Iext" : 0.5*uA}, threshold='V>-10*mV')
full_neuron.V = -60*mV
full_neuron.n = 0.09
full_neuron.h = 1.0


run(duration)

fig, axes = plt.subplots()

axes.scatter(poisson_SkM.t/ms, poisson_SkM.i)

plt.show()


