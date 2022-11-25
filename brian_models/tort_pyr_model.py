# import numpy as np
# import matplotlib.pyplot as plt
#
# exp = np.exp
# mymax = np.maximum
# mV = 1
# ms = 1
# V_bd = np.linspace(-100, 80, 500)
#
# alpha_m_bd = 0.4 * (V_bd/mV + 30) / (1 - exp( - (V_bd/mV + 30) / 7.2 ) ) / ms
# beta_m_bd = 0.124 * (V_bd/mV + 30) / (exp((V_bd/mV + 30) / 7.2 ) - 1 ) / ms
# m_inf_bd = alpha_m_bd/(alpha_m_bd + beta_m_bd)
# tau_m_eq_bd = mymax(0.2*ms, 0.5/(alpha_m_bd + beta_m_bd))
#
# alpha_h_bd = (0.03 * (V_bd/mV + 45) / (1 - exp( - (V_bd/mV + 45) / 1.5 ) ) ) / ms
# beta_h_bd = (0.01 * (V_bd/mV + 45) / (exp((V_bd/mV + 45) / 1.5 ) - 1 )) / ms
# h_inf_bd = 1 / (1 + exp( (V_bd/mV + 50) / 4 ) )
# tau_h_eq_bd = mymax(0.5*ms, 0.5/(alpha_h_bd + beta_h_bd) )
#
#
#
# alpha_n_bd = exp(-0.11 * (V_bd/mV - 13))/ms
# beta_n_bd = exp(-0.08 * (V_bd/mV - 13))/ms
# n_inf_bd = 1 / (1 + alpha_n_bd*ms)
#
# tau_n_eq_bd = mymax(2*ms, 50*ms * beta_n_bd / (1/ms + alpha_n_bd) )
#
# fig, axes = plt.subplots(ncols=2)
# axes[0].plot(V_bd, m_inf_bd**3, label="m")
# axes[0].plot(V_bd, h_inf_bd, label="h")
# axes[0].plot(V_bd, n_inf_bd, label="n")
# axes[0].legend(loc="upper right")
#
# axes[1].plot(V_bd, tau_m_eq_bd, label="tau_m")
# axes[1].plot(V_bd, tau_h_eq_bd, label="tau_h")
# axes[1].plot(V_bd, tau_n_eq_bd, label="tau_n")
# axes[1].legend(loc="upper right")
# plt.show()




from brian2 import *


@implementation('numpy', discard_units=True)
@check_units(th=ms, val=ms, result=ms)
def mymax(th, val):
    return maximum(th, val)

defaultclock.dt = 0.1*ms

Cm = 1*uF # /cm**2
I_app = 1.5*uA

g_l_bd = 0.03 * mS
g_h_bd = 1.0 * mS
g_A_bd = 48 * mS
g_Na_bd = 32 * mS
g_K_bd = 10 * mS

E_K = -90 * mV
E_Na = 55 * mV
E_h = -30 * mV
E_A = -90 * mV
E_l = -70 * mV

B_bd = 4.0
C_bd = 4.0
E_bd = 11.0
D_bd = 1.5
F_bd = 0.825
V_50_bd = -82.0

eqs_Tort = '''
dV_bd/dt = (- (I_Na_bd + I_Ka_bd + I_leak_bd + I_h_bd + I_A_bd) + I_app) / Cm : volt

I_Na_bd = g_Na_bd * m_eq_bd**3 * h_eq_bd * i_eq_bd * (V_bd - E_Na) : ampere
I_Ka_bd =  g_K_bd * n_eq_bd**4 * (V_bd - E_K)  : ampere
I_leak_bd =  g_l_bd * (V_bd - E_l) : ampere
I_h_bd =  g_h_bd * r_eq_bd * (V_bd - E_h)  : ampere
I_A_bd =  g_A_bd * a_eq_bd * b_eq_bd * (V_bd - E_A) : ampere

dm_eq_bd/dt = (m_inf_bd - m_eq_bd) / (tau_m_eq_bd) : 1
dh_eq_bd/dt = (h_inf_bd - h_eq_bd) / (tau_h_eq_bd) : 1
di_eq_bd/dt = (i_inf_bd - i_eq_bd) / (tau_i_eq_bd) : 1
dn_eq_bd/dt = (n_inf_bd - n_eq_bd) / (tau_n_eq_bd) : 1
dr_eq_bd/dt = (r_inf_bd - r_eq_bd) / (tau_r_eq_bd) : 1
da_eq_bd/dt = (a_inf_bd - a_eq_bd) / (tau_a_eq_bd) : 1
db_eq_bd/dt = (b_inf_bd - b_eq_bd) / (tau_b_eq_bd) : 1

m_inf_bd = alpha_m_bd/(alpha_m_bd + beta_m_bd) : 1
tau_m_eq_bd = mymax(0.2*ms, 0.5/(alpha_m_bd + beta_m_bd)) : second

alpha_m_bd = 0.4 * (V_bd/mV + 30) / (1 - exp( - (V_bd/mV + 30) / 7.2 ) ) / ms : Hz
beta_m_bd = 0.124 * (V_bd/mV + 30) / (exp((V_bd/mV + 30) / 7.2 ) - 1 ) / ms : Hz

h_inf_bd = 1 / (1 + exp( (V_bd/mV + 50) / 4 ) ) : 1
tau_h_eq_bd = mymax(0.5*ms, 0.5/(alpha_h_bd + beta_h_bd) ) : second

alpha_h_bd = (0.03 * (V_bd/mV + 45) / (1 - exp( - (V_bd/mV + 45) / 1.5 ) ) ) / ms : Hz
beta_h_bd = (0.01 * (V_bd/mV + 45) / (exp((V_bd/mV + 45) / 1.5 ) - 1 )) / ms : Hz

i_inf_bd = (1 + B_bd * exp((V_bd/mV + 60) / 2)) / (1 + exp( (V_bd/mV + 60) / 2 ) ) : 1
tau_i_eq_bd = mymax(10*ms, 30000*ms * beta_i_bd / (1/ms + alpha_i_bd) ) : second

alpha_i_bd = exp(0.45 * (V_bd/mV + 66)) /ms : Hz
beta_i_bd = exp(0.09 * (V_bd/mV + 66)) /ms : Hz

n_inf_bd = 1 / (1 + alpha_n_bd*ms) : 1
tau_n_eq_bd = mymax(2*ms, 50*ms * beta_n_bd / (1/ms + alpha_n_bd) ) : second
alpha_n_bd = exp(-0.11 * (V_bd/mV - 13))/ms : Hz
beta_n_bd = exp(-0.08 * (V_bd/mV - 13))/ms : Hz

r_inf_bd = 1 / (1 + exp((V_bd/mV - V_50_bd) / 10.5)) : 1
tau_r_eq_bd = 1 / (exp(-14.59 - 0.086 * V_bd/mV) + exp(-1.87 + 0.0701 * V_bd/mV)) *ms : second

a_inf_bd = 1/(1.0 + alpha_a_bd*ms) : 1
tau_a_eq_bd = mymax(0.1*ms, C_bd*ms * beta_a_bd /(1/ms + alpha_a_bd) ) : second

alpha_a_bd = exp( -0.038 * (D_bd + long_ratio_bd) * (V_bd/mV - E_bd)) / ms : Hz
beta_a_bd = exp( -0.038 * (F_bd + long_ratio_bd) * (V_bd/mV - E_bd)) / ms: Hz
long_ratio_bd = 1 / (1 + exp(V_bd/mV + 40) / 5) : 1

b_inf_bd = 1 / (1 + exp(0.11 * (V_bd/mV  + 56))) : 1
tau_b_eq_bd = mymax(2*ms, 0.26 * (V_bd/mV + 50) * ms ) : second
'''

neuron = NeuronGroup(1, eqs_Tort, method='exponential_euler')
neuron.V_bd = -90*mV
# neuron.n = 0.09
neuron.h_eq_bd = 1.0


M = StateMonitor(neuron, 'V_bd', record=0)

run(200*ms, report='text')

plot(M.t/ms, M[0].V_bd/mV)
show()




