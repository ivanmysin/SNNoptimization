from brian2 import *
# import h5py
defaultclock.dt = 0.1*ms


Cm = 1*uF # /cm**2
#ext = 0.2*uA
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



neuron = NeuronGroup(N, eqs, method='exponential_euler', namespace={"Iext" : -0.1*uA})
neuron.V = -90*mV
neuron.n = 0.09
neuron.h = 1.0
neuron.lso = 0.2

reduced_eqs = '''
dV/dt = (IKdr + IL +  INap + IH + Iext)/Cm : volt (unless refractory)
IL = gL*(EL - V)           : ampere

IKdr = gK*n**4*(EK - V) : ampere
INap = gNap * mnap * (ENa - V) :  ampere
IH = gH * (0.65 * lfo + 0.35*lso) * (EH - V) :  ampere

dn/dt = (alpha_n*(1-n)-beta_n*n) : 1  (unless refractory)
alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz

dmnap/dt = (alpha_mnap*(1-mnap)-beta_mnap*mnap) : 1 (unless refractory)
alpha_mnap = 1.0 / (0.15 *  exp( -(V + 38*mV)/(6.5*mV)) )/ms : Hz
beta_mnap = 1.0 / (0.15 *  exprel( -(V + 38*mV)/(6.5*mV)))/ms : Hz


dlfo/dt = (lfo_inf - lfo) / tau_lfo : 1 (unless refractory)
lfo_inf = 1 / (1 + exp( (V + 79.2*mV)/(9.78*mV) ) ) : 1
tau_lfo = 0.51*ms / ( exp( (V + 1.7*mV)/(10*mV)) + exp( -(V + 340*mV)/(52*mV))  ) + 1.0*ms : second

dlso/dt = (lso_inf - lso) / tau_lso : 1 (unless refractory)
lso_inf = 1 / (1 + exp( (V + 2.83*mV)/(15.9*mV) ) ) : 1
tau_lso = 5.6*ms / ( exp( (V - 1.7*mV)/(14*mV)) + exp( -(V + 260*mV)/(43*mV))  ) : second

dVT/dt = (-55*mV - VT)/(4*ms) : volt
'''



reduced_neuron = NeuronGroup(N, reduced_eqs, threshold='V > VT', \
                    reset='V =-40*mV;n = 0.8; VT=-20*mV; lso=lso-0.015; lfo = lfo-0.011; mnap=0.95', \
                    refractory=2.0*ms, method='exponential_euler', namespace={"Iext" : -0.1*uA})

reduced_neuron.V = -90*mV
reduced_neuron.VT = -55*mV
reduced_neuron.n = 0.09
reduced_neuron.lso = 0.2


M_full_V = StateMonitor(neuron, 'V', record=0)
M_full_INa = StateMonitor(neuron, 'INa', record=0)
M_full_IK = StateMonitor(neuron, 'IKdr', record=0)
M_full_n = StateMonitor(neuron, 'n', record=0)
M_full_lso = StateMonitor(neuron, 'lso', record=0)
M_full_lfo = StateMonitor(neuron, 'lfo', record=0)
M_full_mnap = StateMonitor(neuron, 'mnap', record=0)

M_reduced = StateMonitor(reduced_neuron, 'V', record=0)
M_reduced_VT = StateMonitor(reduced_neuron, 'VT', record=0)
M_reduced_n = StateMonitor(reduced_neuron, 'n', record=0)
M_reduced_lso = StateMonitor(reduced_neuron, 'lso', record=0)
M_reduced_lfo = StateMonitor(reduced_neuron, 'lfo', record=0)
M_reduced_mnap = StateMonitor(reduced_neuron, 'mnap', record=0)

run(200*ms, report='text')

fig, axes = plt.subplots(nrows=6, sharex=True)
axes[0].plot(M_full_V.t/ms, M_full_V[0].V/mV)
axes[0].plot(M_reduced.t/ms, M_reduced[0].V/mV)
axes[0].plot(M_reduced_VT.t/ms, M_reduced_VT[0].VT/mV)

axes[1].plot(M_full_INa.t/ms, M_full_INa[0].INa/uA, label="INa")
axes[1].plot(M_full_IK.t/ms, M_full_IK[0].IKdr/uA, label="IKdr")
axes[1].legend(loc="upper right")

axes[2].plot(M_full_n.t/ms, M_full_n[0].n**4, label="full")
axes[2].plot(M_reduced_n.t/ms, M_reduced_n[0].n**4, label="educed")
axes[2].legend(loc="upper right")

axes[3].plot(M_full_lso.t/ms, M_full_lso[0].lso, label="full")
axes[3].plot(M_reduced_lso.t/ms, M_reduced_lso[0].lso, label="reduced")
axes[3].legend(loc="upper right")

axes[4].plot(M_full_lfo.t/ms, M_full_lfo[0].lfo, label="full")
axes[4].plot(M_reduced_lfo.t/ms, M_reduced_lfo[0].lfo, label="reduced")
axes[4].legend(loc="upper right")


axes[5].plot(M_full_mnap.t/ms, M_full_mnap[0].mnap, label="full")
axes[5].plot(M_reduced_mnap.t/ms, M_reduced_mnap[0].mnap, label="reduced")
axes[5].legend(loc="upper right")

plt.show()
