from brian2 import *
# import h5py
defaultclock.dt = 0.01*ms


Cm = 1.3*uF # /cm**2
#ext = 0.2*uA
gL = 0.05*mS
EL = -70*mV #  -54.4*mV
ENa = 90*mV
EK = -100*mV #  -77*mV
EH = -32*mV # -20*mV

gNa = 30*msiemens
gK = 23*msiemens
gKA = 16.0*mS
gH = 8.0 * msiemens
sigma = 0.2*mV


N = 1


# OLM Model
eqs = '''
dV/dt = (INa + IKdr + IL + IKA + IH + Iext)/Cm + sigma*xi/ms**0.5 : volt
IL = gL*(EL - V)           : ampere
INa = gNa*m**3*h*(ENa - V) : ampere
IKdr = gK*n**4*(EK - V) : ampere
IKA = gKA * a*b * (EK - V) :  ampere
IH = gH * r * (EH - V) :  ampere

#dm/dt = (alpha_m*(1-m)-beta_m*m) : 1
m = alpha_m / (alpha_m + beta_m) : 1
alpha_m = 1.0 / exprel(-(V+38*mV)/(10*mV))/ms : Hz
beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms : Hz
dh/dt = (alpha_h*(1-h)-beta_h*h) : 1
alpha_h = 0.07*exp(-(V+63*mV)/(20*mV))/ms : Hz
beta_h = 1./(exp(-0.1/mV*(V+33*mV))+1)/ms : Hz
dn/dt = (alpha_n*(1-n)-beta_n*n) : 1
alpha_n = 0.018/mV * (V - 25*mV) / (1 - exp( (V - 25*mV)/(-25*mV)) )/ms : Hz
beta_n = 0.0036*((V-35*mV)/mV) / (exp( (V-35*mV)/(12*mV) ) - 1) /ms : Hz

da/dt = (a_inf - a) / tau_a : 1
a_inf = 1 / (1 + exp( (V + 14*mV)/(-16*mV) ) ) : 1
tau_a = 5*ms : second

db/dt = (b_inf - b) / tau_b : 1
b_inf = 1 / (1 + exp( (V + 71*mV)/(7.3*mV) ) ) : 1
tau_b = 1 / (0.000009/(exp((V - 26*mV)/(18.5*mV)) + 0.014/(0.2 + exp((V+70*mV)/(-11*mV)))))*ms : second
dr/dt = (r_inf - r) / tau_r : 1
r_inf =  1 / (1 + exp( (V + 84*mV) / (10.2*mV) ) ) : 1
tau_r = 1 / (exp(-14.59 - 0.086*V/mV) + exp(-1.87 + 0.0701*V/mV) ) * ms: second
'''



neuron = NeuronGroup(N, eqs, method='heun', namespace={"Iext" : -0.5*uA})
neuron.V = -90*mV
neuron.n = 0.09
neuron.h = 1.0


reduced_eqs = '''
dV/dt = (IKdr + IL + IKA + IH + Iext)/Cm : volt (unless refractory)
IL = gL*(EL - V)           : ampere
IKdr = gK*n**4*(EK - V) : ampere
IKA = gKA * a*b * (EK - V) :  ampere
IH = gH * r * (EH - V) :  ampere

dn/dt = (alpha_n*(1-n)-beta_n*n) : 1 (unless refractory)
alpha_n = 0.018/mV * (V - 25*mV) / (1 - exp( (V - 25*mV)/(-25*mV)) )/ms : Hz
beta_n = 0.0036*((V-35*mV)/mV) / (exp( (V-35*mV)/(12*mV) ) - 1) /ms : Hz

da/dt = (a_inf - a) / tau_a : 1 (unless refractory)
a_inf = 1 / (1 + exp( (V + 14*mV)/(-16*mV) ) ) : 1
tau_a = 5*ms : second

db/dt = (b_inf - b) / tau_b : 1 (unless refractory)
b_inf = 1 / (1 + exp( (V + 71*mV)/(7.3*mV) ) ) : 1
tau_b = 1 / (0.000009/(exp((V - 26*mV)/(18.5*mV)) + 0.014/(0.2 + exp((V+70*mV)/(-11*mV)))))*ms : second
dr/dt = (r_inf - r) / tau_r : 1 (unless refractory)
r_inf =  1 / (1 + exp( (V + 84*mV) / (10.2*mV) ) ) : 1
tau_r = 1 / (exp(-14.59 - 0.086*V/mV) + exp(-1.87 + 0.0701*V/mV) ) * ms: second
dVT/dt = (-61*mV - VT)/(4*ms) : volt
'''



reduced_neuron = NeuronGroup(N, reduced_eqs, threshold='V > VT', \
                    reset='V =-40*mV;n = 0.67; VT=-20*mV; a = 0.25; b = b + 0.0; r=0.0001', \
                    refractory=2.0*ms, method='exponential_euler', namespace={"Iext" : -0.5*uA})

reduced_neuron.V = -90*mV
reduced_neuron.VT = -61*mV
reduced_neuron.n = 0.09



M_full_V = StateMonitor(neuron, 'V', record=0)
M_full_INa = StateMonitor(neuron, 'INa', record=0)
M_full_IK = StateMonitor(neuron, 'IKdr', record=0)
M_full_n = StateMonitor(neuron, 'n', record=0)
M_full_a = StateMonitor(neuron, 'a', record=0)
M_full_b = StateMonitor(neuron, 'b', record=0)
M_full_r = StateMonitor(neuron, 'r', record=0)

M_reduced = StateMonitor(reduced_neuron, 'V', record=0)
M_reduced_VT = StateMonitor(reduced_neuron, 'VT', record=0)
M_reduced_n = StateMonitor(reduced_neuron, 'n', record=0)
M_reduced_a = StateMonitor(reduced_neuron, 'a', record=0)
M_reduced_b = StateMonitor(reduced_neuron, 'b', record=0)
M_reduced_r = StateMonitor(reduced_neuron, 'r', record=0)

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

axes[3].plot(M_full_a.t/ms, M_full_a[0].a, label="full")
axes[3].plot(M_reduced_a.t/ms, M_reduced_a[0].a, label="reduced")
axes[3].legend(loc="upper right")

axes[4].plot(M_full_b.t/ms, M_full_b[0].b, label="full")
axes[4].plot(M_reduced_b.t/ms, M_reduced_b[0].b, label="reduced")
axes[4].legend(loc="upper right")


axes[5].plot(M_full_r.t/ms, M_full_r[0].r, label="full")
axes[5].plot(M_reduced_r.t/ms, M_reduced_r[0].r, label="reduced")
axes[5].legend(loc="upper right")

plt.show()
