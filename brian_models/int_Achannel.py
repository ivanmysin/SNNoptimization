from brian2 import *
# import h5py
defaultclock.dt = 0.1*ms


Cm = 1*uF # /cm**2
#Iext = 0.5*uA
gL = 0.18*msiemens
EL = -60*mV
ENa = 55*mV
EK = -90*mV
gNa = 50*mS # 150*msiemens
gK = 23*msiemens
gKA = 10 * msiemens
sigma = 0.3*mV


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
'''

neuron = NeuronGroup(N, eqs, method='exponential_euler', namespace={"Iext" : 1.5*uA})
neuron.V = -90*mV
neuron.n = 0.09
neuron.h = 1.0
neuron.a = 0.0
neuron.b = 0.9

reduced_eqs = '''
dV/dt = (IKdr + IL + IA + Iext)/Cm : volt (unless refractory)
IL = gL*(EL - V)           : ampere
IKdr = gK*n**4*(EK - V) : ampere
IA = gKA * a * b * (EK - V) :  ampere

dn/dt = (n_inf - n) / tau_n : 1 (unless refractory)
tau_n = 0.5*ms + 2.0*ms/(1 + exp(0.045/mV * (V - 50*mV))) : second
n_inf = 1.0 / (1.0 + exp(-0.045 * (V/mV + 10))) : 1 

da/dt = (alpha_a*(1-a)-beta_a*a) : 1 (unless refractory)
alpha_a = 0.2 / exprel( (13.1*mV - V)/(10*mV))/ms : Hz
beta_a = 0.175 / exprel( (V - 40.1*mV)/(10*mV))/ms : Hz


db/dt = (alpha_b*(1-b)-beta_b*b) : 1 (unless refractory)
alpha_b = 0.0016 * exp( (-13*mV - V) / (18*mV) ) /ms : Hz
beta_b = 0.05 / (1 + exp( (10.1*mV - V)/(5*mV) ) ) /ms : Hz

dVT/dt = (-60*mV - VT)/(4*ms) : volt
'''

reduced_neuron = NeuronGroup(N, reduced_eqs, threshold='V > VT', \
                    reset='V =-40*mV;n = 0.45; VT=-20*mV; a=0.31;b=b-0.05', \
                    refractory=2.5*ms, method='exponential_euler', namespace={"Iext" : 1.5*uA})

reduced_neuron.V = -90*mV
reduced_neuron.VT = -60*mV
reduced_neuron.n = 0.09
reduced_neuron.b = 0.9





M_full_V = StateMonitor(neuron, 'V', record=0)
M_full_INa = StateMonitor(neuron, 'INa', record=0)
M_full_IK = StateMonitor(neuron, 'IKdr', record=0)
M_full_n = StateMonitor(neuron, 'n', record=0)
M_full_a = StateMonitor(neuron, 'a', record=0)
M_full_b = StateMonitor(neuron, 'b', record=0)

M_reduced = StateMonitor(reduced_neuron, 'V', record=0)
M_reduced_VT = StateMonitor(reduced_neuron, 'VT', record=0)
M_reduced_n = StateMonitor(reduced_neuron, 'n', record=0)
M_reduced_a = StateMonitor(reduced_neuron, 'a', record=0)
M_reduced_b = StateMonitor(reduced_neuron, 'b', record=0)

run(200*ms, report='text')

fig, axes = plt.subplots(nrows=5, sharex=True)
axes[0].plot(M_full_V.t/ms, M_full_V[0].V/mV)
axes[0].plot(M_reduced.t/ms, M_reduced[0].V/mV)
axes[0].plot(M_reduced_VT.t/ms, M_reduced_VT[0].VT/mV)

axes[1].plot(M_full_INa.t/ms, M_full_INa[0].INa/uA, label="INa")
axes[1].plot(M_full_IK.t/ms, M_full_IK[0].IKdr/uA, label="IKdr")
axes[1].legend(loc="upper right")

axes[2].plot(M_full_n.t/ms, M_full_n[0].n**4, label="full")
axes[2].plot(M_reduced_n.t/ms, M_reduced_n[0].n**4, label="educed")
axes[2].legend(loc="upper right")

axes[3].plot(M_full_a.t/ms, M_full_a[0].a, label="full")
axes[3].plot(M_reduced_a.t/ms, M_reduced_a[0].a, label="reduced")
axes[3].legend(loc="upper right")

axes[4].plot(M_full_b.t/ms, M_full_b[0].b, label="full")
axes[4].plot(M_reduced_b.t/ms, M_reduced_b[0].b, label="reduced")
axes[4].legend(loc="upper right")

plt.show()



