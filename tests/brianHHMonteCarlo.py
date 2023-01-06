from brian2 import *
import h5py
defaultclock.dt = 0.1*ms

Cm = 1*uF # /cm**2
Iapp = 1.8*uA
gL = 0.1*msiemens
EL = -60*mV
#ENa = 55*mV
EK = -90*mV
#gNa = 35*msiemens
gK = 40*msiemens
sigma = 0.2*mV
tau = 0.1 * ms

N = 4000

# sqrt(2*sigma**2/tau)

eqs = '''
dV/dt = (gK*(n**4)*(EK - V) + gL*(EL - V) + Iapp )/Cm  + sigma*xi/ms**0.5 : volt (unless refractory)


dn/dt = (n_inf - n) / tau_n : 1 (unless refractory)
n_inf = 1.0 / (1.0 + exp(-0.045 * (V + 10*mV) /mV) ) : 1
tau_n = 0.5*ms + 2.0*ms/(1 + exp(0.045 * (V - 50*mV)/mV)) : second


# VT = -50*mV : volt
dVT/dt = (-50*mV - VT)/(5*ms) : volt
'''


neuron = NeuronGroup(N, eqs, threshold='V > VT', \
                     reset='V =-40*mV;n = 0.45;VT=-30*mV', refractory=1.5*ms, method='heun') # , method='exponential_euler'
neuron.V = -90*mV


neuron.VT = -50*mV
neuron.n = 0.09
M = StateMonitor(neuron, 'V', record=0)

spikemon = SpikeMonitor(neuron)
run(200*ms, report='text')

spike_rate, bins = np.histogram(spikemon.t/ms, 2001, density=False, range=[0, 200])
spike_rate = spike_rate / (1000*N*defaultclock.dt)

#plot(M.t/ms, M[0].V/mV)



with h5py.File("../com.hdf5", "r") as file:
    #cbrd_V = file["Vm"][:]
    cbrd_spike_rate = file["SpikeRate"][:]

plot(M.t/ms, cbrd_spike_rate, color='green', linewidth=4)

plot(bins[:-1], spike_rate, color='red', linewidth=1)

show()

"""
# Wang-Buzsaki Model
eqs = '''
dv/dt = (-gNa*m**3*h*(v-ENa)-gK*n**4*(v-EK)-gL*(v-EL)+Iapp)/Cm : volt
m = alpha_m/(alpha_m+beta_m) : 1
alpha_m = 0.1/mV*10*mV/exprel(-(v+35*mV)/(10*mV))/ms : Hz
beta_m = 4*exp(-(v+60*mV)/(18*mV))/ms : Hz
dh/dt = 5*(alpha_h*(1-h)-beta_h*h) : 1
alpha_h = 0.07*exp(-(v+58*mV)/(20*mV))/ms : Hz
beta_h = 1./(exp(-0.1/mV*(v+28*mV))+1)/ms : Hz
dn/dt = 5*(alpha_n*(1-n)-beta_n*n) : 1
alpha_n = 0.01/mV*10*mV/exprel(-(v+34*mV)/(10*mV))/ms : Hz
beta_n = 0.125*exp(-(v+44*mV)/(80*mV))/ms : Hz
'''
"""