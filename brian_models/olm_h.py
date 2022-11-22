from brian2 import *
# import h5py
defaultclock.dt = 0.1*ms


Cm = 1*uF # /cm**2
Iext = 0.2*uA
gL = 0.3*msiemens
EL = -54.4*mV
ENa = 50*mV
EK = -77*mV
EH = -20*mV

gNa = 120*msiemens
gK = 36*msiemens
gNap = 2.5 * msiemens
gH = 1.5 * msiemens
sigma = 0.2*mV


N = 1


# Interneuron Model with A-current
eqs = '''
dV/dt = (INa + IKdr + IL +  INap + IH + Iext)/Cm : volt
IL = gL*(EL - V)           : ampere
INa = gNa*m**3*h*(ENa - V) : ampere
IKdr = gK*n**4*(EK - V) : ampere
INap = gNap * mnap * (ENa - V) :  ampere
IH = gH * (0.65 * lfo + 0.35*lso) * (EH - V) :  ampere

m = alpha_m/(alpha_m+beta_m) : 1
alpha_m = 1.0 / exprel(-(V+40*mV)/(10*mV))/ms : Hz
beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms : Hz
dh/dt = (alpha_h*(1-h)-beta_h*h) : 1
alpha_h = 0.07*exp(-(V+65*mV)/(20*mV))/ms : Hz
beta_h = 1./(exp(-0.1/mV*(V+35*mV))+1)/ms : Hz
dn/dt = (alpha_n*(1-n)-beta_n*n) : 1
alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz

dmnap/dt = (alpha_mnap*(1-mnap)-beta_mnap*mnap) : 1
alpha_mnap = 1.0 / (0.15 *  exp( -(V + 38*mV)/(6.5*mV)) )/ms : Hz
beta_mnap = 1.0 / (0.15 *  exprel( -(V + 38*mV)/(6.5*mV)))/ms : Hz


dlfo/dt = (lfo_inf - lfo) / tau_lfo : 1
lfo_inf = 1 / (1 + exp( (V + 79.2*mV)/(9.78*mV) ) ) : 1
tau_lfo = 0.51*ms / ( exp( (V + 1.7*mV)/(10*mV)) + exp( -(V + 340*mV)/(52*mV))  ) + 1.0*ms : second

dlso/dt = (lso_inf - lso) / tau_lso : 1
lso_inf = 1 / (1 + exp( (V + 2.83*mV)/(15.9*mV) ) ) : 1
tau_lso = 5.6*ms / ( exp( (V - 1.7*mV)/(14*mV)) + exp( -(V + 260*mV)/(43*mV))  ) : second

'''



neuron = NeuronGroup(N, eqs, method='exponential_euler')
neuron.V = -90*mV
neuron.n = 0.09
neuron.h = 1.0
#neuron.a = 0.0


M = StateMonitor(neuron, 'V', record=0)

run(200*ms, report='text')

plot(M.t/ms, M[0].V/mV)
show()

