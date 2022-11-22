from brian2 import *
# import h5py
defaultclock.dt = 0.1*ms


Cm = 1*uF # /cm**2
Iext = 1.2*uA
gL = 0.18*msiemens
EL = -60*mV
ENa = 55*mV
EK = -90*mV
gNa = 150*msiemens
gK = 23*msiemens
gKA = 10 * msiemens
sigma = 0.2*mV


N = 1


# Interneuron Model with A-current
eqs = '''
dV/dt = (INa + IKdr + IL + IA + Iext)/Cm : volt
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
dn/dt = (alpha_n*(1-n)-beta_n*n) : 1
alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz

da/dt = (alpha_a*(1-a)-beta_a*a) : 1
alpha_a = 0.2 / exprel( (13.1*mV - V)/(10*mV))/ms : Hz
beta_a = 0.175 / exprel( (V - 40.1*mV)/(10*mV))/ms : Hz


db/dt = (alpha_b*(1-b)-beta_b*b) : 1
alpha_b = 0.0016 * exp( (-13*mV - V) / (18*mV) ) /ms : Hz
beta_b = 0.05 / (1 + exp( (10.1*mV - V)/(5*mV) ) ) /ms : Hz
'''

neuron = NeuronGroup(N, eqs, method='exponential_euler')
neuron.V = -90*mV
neuron.n = 0.09
neuron.h = 1.0
neuron.a = 0.0
neuron.b = 0.0

M = StateMonitor(neuron, 'V', record=0)

run(200*ms, report='text')

plot(M.t/ms, M[0].V/mV)
show()

