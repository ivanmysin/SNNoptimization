from brian2 import *
import matplotlib.pyplot as plt
defaultclock.dt = 0.05 * ms

METHOD = 'heun'

params = {
    "Iext": 0.0 * uA,
    "Cm": 1 * uF,  # /cm**2
    "gL": 0.18 * mS,
    "EL": -65*mV, #
    "ENa": 45 * mV,
    "EK": -90 * mV,
    "gNa": 30 * mS,
    "gK": 40 * mS,
    "sigma": 0.3 * mV,
}

# White 1998 Interneuron Model
eqs = '''
    dV/dt = (INa + IKdr + IL + Iext)/Cm + sigma*xi/ms**0.5 : volt
    IL = gL*(EL - V)           : ampere
    INa = gNa*(m_inf**3)*h*(ENa - V) : ampere
    IKdr = gK*(n**4)*(EK - V) : ampere
    m_inf = 1 / (1 + exp( -0.08*(V/mV + 26)) ) : 1
    dh/dt = (h_inf - h) / tau_h : 1
    h_inf = 1.0 / (1.0 + exp(0.13/mV * (V + 38*mV))) : 1
    tau_h = 0.6*ms / (1.0 + exp(-0.12/mV*(V + 67*mV)))   : second
    dn/dt = (n_inf - n) / tau_n : 1
    tau_n = 0.5*ms + 2.0*ms/(1 + exp(0.045/mV * (V - 50*mV))) : second
    n_inf = 1.0 / (1.0 + exp(-0.045 * (V/mV + 10))) : 1
    '''


neuron = NeuronGroup(1, eqs, method=METHOD, namespace=params, name="int", threshold='V > -10*mV', refractory="5*ms")
neuron.V = -90 * mV

VmSt = StateMonitor(neuron, "V", record=True)

run(1000*ms)

plt.plot(VmSt.t/ms, VmSt.V[0]/mV)
plt.show()

