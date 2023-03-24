from brian2 import *

defaultclock.dt = 0.1 * ms


params = {
    "Iext": 0.5 * uA,
    "Cm": 1 * uF,  # /cm**2
    "gL": 0.1 * mS,
    "EL": -65*mV, #
    "ENa": 55 * mV,
    "EK": -90 * mV,
    "gNa": 30 * mS,
    "gK": 40 * mS,
    "sigma": 0.3 * mV,
}

# White 1998 Interneuron Model
eqs = '''
   dV/dt = (INa + IKdr + IL + Iext)/Cm + sigma*xi/ms**0.5 : volt
   IL = gL*(EL - V)           : ampere
   INa = gNa*(m**3)*h*(ENa - V) : ampere
   IKdr = gK*(n**4)*(EK - V) : ampere
   IA = gKA * a * b * (EK - V) :  ampere

   m = alpha_m/(alpha_m+beta_m) : 1
   alpha_m = 1.0 / exprel(-(V+40*mV)/(10*mV))/ms : Hz
   beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms : Hz
   dh/dt = (alpha_h*(1-h)-beta_h*h) : 1
   alpha_h = 0.07*exp(-(V+65*mV)/(20*mV))/ms : Hz
   beta_h = 1./(exp(-0.1/mV*(V+35*mV))+1)/ms : Hz


   dn/dt = (n_inf - n) / tau_n : 1
   tau_n = 0.5*ms + 2.0*ms/(1 + exp(0.045/mV * (V - 50*mV))) : second
   n_inf = 1.0 / (1.0 + exp(-0.045 * (V/mV + 10))) : 1

   '''




neuron = NeuronGroup(1, eqs, method=METHOD, namespace=params, name="name", threshold='V > -10*mV',
                     refractory="5*ms")
neuron.V = -90 * mV


