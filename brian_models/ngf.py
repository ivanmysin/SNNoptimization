import matplotlib.pyplot as plt
from brian2 import *
# import h5py
defaultclock.dt = 0.1*ms


Cm = 1*uF # /cm**2
gL = 0.18*msiemens
EL = -60*mV
ENa = 55*mV
EK = -80*mV
gNa = 50 * msiemens # 150*msiemens
gK = 8 * mS # 23*msiemens

sigma = 0.2*mV


N = 1

# Interneuron Model without A-current
full_eqs = '''
dV/dt = (INa + IKdr + IL + Iext)/Cm : volt
IL = gL*(EL - V)           : ampere
INa = gNa*m**3*h*(ENa - V) : ampere
IKdr = gK*n**4*(EK - V) : ampere

m = alpha_m/(alpha_m+beta_m) : 1
alpha_m = 1.0 / exprel(-(V+40*mV)/(10*mV))/ms : Hz
beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms : Hz
dh/dt = (alpha_h*(1-h)-beta_h*h) : 1
alpha_h = 0.07*exp(-(V+65*mV)/(20*mV))/ms : Hz
beta_h = 1./(exp(-0.1/mV*(V+35*mV))+1)/ms : Hz
dn/dt = (alpha_n*(1-n)-beta_n*n) : 1
alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz
'''

full_neuron = NeuronGroup(N, full_eqs, method='exponential_euler', namespace={"Iext" : 2*uA})
full_neuron.V = -90*mV
full_neuron.n = 0.09
full_neuron.h = 1.0


reduced_eqs = '''
dV/dt = (IKdr + IL + Iext)/Cm : volt (unless refractory)
IL = gL*(EL - V)           : ampere
IKdr = gK*n**4*(EK - V)    : ampere

dn/dt = (alpha_n*(1-n)-beta_n*n) : 1 (unless refractory)
alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz
dVT/dt = (-62*mV - VT)/(4*ms) : volt
'''

reduced_neuron = NeuronGroup(N, reduced_eqs, threshold='V > VT', \
                    reset='V =-40*mV;n = 0.65;VT=-20*mV', \
                    refractory=2.5*ms, method='exponential_euler', namespace={"Iext" : 2*uA})

reduced_neuron.V = -90*mV
reduced_neuron.VT = -62*mV
reduced_neuron.n = 0.09
#reduced_neuron.Iext = 1.5*uA




M_full_V = StateMonitor(full_neuron, 'V', record=0)
M_full_INa = StateMonitor(full_neuron, 'INa', record=0)
M_full_IK = StateMonitor(full_neuron, 'IKdr', record=0)
M_full_n = StateMonitor(full_neuron, 'n', record=0)

M_reduced = StateMonitor(reduced_neuron, 'V', record=0)
M_reduced_VT = StateMonitor(reduced_neuron, 'VT', record=0)
M_reduced_n = StateMonitor(reduced_neuron, 'n', record=0)

run(200*ms, report='text')

fig, axes = plt.subplots(nrows=3, sharex=True)
axes[0].plot(M_full_V.t/ms, M_full_V[0].V/mV)
axes[0].plot(M_reduced.t/ms, M_reduced[0].V/mV)
axes[0].plot(M_reduced_VT.t/ms, M_reduced_VT[0].VT/mV)

axes[1].plot(M_full_INa.t/ms, M_full_INa[0].INa/uA, label="INa")
axes[1].plot(M_full_IK.t/ms, M_full_IK[0].IKdr/uA, label="IKdr")
axes[1].legend(loc="upper right")

axes[2].plot(M_full_n.t/ms, M_full_n[0].n, label="full")
axes[2].plot(M_reduced_n.t/ms, M_reduced_n[0].n, label="educed")
axes[2].legend(loc="upper right")
plt.show()



