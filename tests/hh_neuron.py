import numpy as np
import matplotlib.pyplot as plt
from brian2 import *

defaultclock.dt = 0.1*ms


def simulate(Iapp=2, Cm=1):
    Cm = Cm*uF # /cm**2

    gL = 0.1*msiemens
    EL = -65*mV
    ENa = 55*mV
    EK = -90*mV
    gbarNa = 35*msiemens
    gbarKdr = 9*msiemens

    Iapp = Iapp * uA

    eqs = '''
    dv/dt = (gNa * (ENa - v) + gK*(EK - v) + gL*(EL - v)+Iapp)/Cm : volt
    gNa = gbarNa*m**3*h : siemens
    gK = gbarKdr*n**4 : siemens
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

    neuron = NeuronGroup(1, eqs, method='exponential_euler')
    neuron.v = -70*mV
    neuron.h = 1
    Mon = StateMonitor(neuron, 'v', record=0)
    Mongna = StateMonitor(neuron, 'gNa', record=0)
    Mongk = StateMonitor(neuron, 'gK', record=0)
    # Mongl = StateMonitor(neuron, 'gL', record=0)

    run(100*ms) # , report='text'

    # plot(Mon.t/ms, Mon[0].v/mV)
    # show()

    t = np.asarray(Mon.t/ms)
    V = np.asarray(Mon[0].v/mV)
    g = np.asarray( ( Mongna[0].gNa + Mongk[0].gK + gL )/ msiemens )



    return t, V, g

###########################################################
def main():
    Iapp_target = 2.0
    Cm = 1
    t, Vtarget, _ = simulate(Iapp=Iapp_target, Cm=Cm)

    Loss = np.zeros(200, dtype=np.float64)
    dL_dp = np.zeros_like(Loss)
    dt = float(defaultclock.dt / ms)
    print("dt = ", dt)
    learning_rate = 0.000001

    Iapp = 1.0
    for ls_idx in range(dL_dp.size):
        t, V, sum_cond = simulate(Iapp, Cm=Cm)
        Loss[ls_idx] = 0.5 * np.sum( (V - Vtarget)**2 )

        lamda_lg = np.zeros_like(t)
        for idx in t.size - np.arange(t.size) - 2:
            lamda_lg[idx] = lamda_lg[idx + 1] - dt * (sum_cond[idx+1]*lamda_lg[idx + 1]/Cm - V[idx+1] + Vtarget[idx+1])

        dL_dp[ls_idx] = np.sum(lamda_lg ) / Cm   # *dt

        if ls_idx == 0:
            step_h = 0.01
            Iapp_1 = Iapp - step_h
            Iapp_2 = Iapp + step_h
            _, V_1, _ = simulate(Iapp_1, Cm=Cm)
            _, V_2, _ = simulate(Iapp_2, Cm=Cm)

            Loss_1 = 0.5 * np.sum( (V_1 - Vtarget)**2 )
            Loss_2 = 0.5 * np.sum( (V_2 - Vtarget)**2 )

            dL_dp_numetric = (Loss_2 - Loss_1) / (2 * step_h)
            print(dL_dp_numetric, dL_dp[ls_idx])


        Iapp = Iapp - learning_rate * dL_dp[ls_idx]

        #break

    print("Optimmized Iapp", Iapp)
    print("Real Iapp", Iapp_target)
    fig, axes = plt.subplots(nrows=3)
    axes[0].plot(t, Vtarget, color='green', linewidth=5)
    axes[0].plot(t, V, color='orange', linewidth=2)

    axes[1].plot(Loss, color='green', linewidth=5)
    axes[2].plot(dL_dp, color='orange', linewidth=2)
    plt.show()
#########################################################################
if __name__ == '__main__':
    main()