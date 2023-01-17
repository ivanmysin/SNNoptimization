from brian2 import *
from code_generated_params import params_net
import net_lib
METHOD = 'exponential_euler'

def get_int_A_group(params_groups):
    N = 1
    params = {
        "Iext": params_groups["Iext"] * uA,
        "Cm" : params_groups["C"] * uF,  # /cm**2
        "gL" : params_groups["gl"] * mS,
        "EL" : params_groups["El"] * mV,
        "ENa" : 55 * mV,
        "EK" : params_groups["channels_params"][0]["Erev"] * mV,
        "gNa" : 50 * mS,
        "gK" : params_groups["channels_params"][0]["gmax"] * mS,
        "gKA" : params_groups["channels_params"][1]["gmax"] * mS,
        "sigma" : 0.3 * mV,
    }


    # Interneuron Model with A-current
    eqs = '''
    dV/dt = (INa + IKdr + IL + IA + Iext + Isyn)/Cm : volt
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

    {isyn_str}
    '''
    Isyn_str = net_lib.get_str4Isyn(params_groups["name"], params_net["params_synapses"])
    eqs = eqs.format(isyn_str = Isyn_str)


    neuron = NeuronGroup(N, eqs, method=METHOD, namespace=params, name=params_groups["name"], threshold='V > -20*mV')
    neuron.V = -90 * mV

    return neuron

def get_connection_object(pre_pop, post_pop, syn_params):
    # U_0, tau_r, tau_f, w, gbarS
    synapses_eqs_template = '''
    # Usage of releasable neurotransmitter per single action potential:
    du_S/dt = - u_S / tau_f    : 1 (event-driven)
    # Fraction of synaptic neurotransmitter resources available:
    dx_S/dt = (1 - x_S) / tau_r : 1 (event-driven)
    tau_r = {tau_r}*ms : second
    tau_f = {tau_f}*ms : second
    '''

    synapses_action_template = '''
    u_S += U_0 * (1 - u_S)
    r_S = u_S * x_S
    x_S -= r_S
    g_{pre_name}2{post_name}_post += gbarS*r_S
    '''
    synapses_eqs = synapses_eqs_template.format(**syn_params)
    synapses_action = synapses_action_template.format(**syn_params)

    # print(synapses_eqs)
    # print(synapses_action)
    # print("#############################")

    synobj = Synapses(pre_pop, post_pop,  model=synapses_eqs,
                       on_pre=synapses_action, namespace={"U_0": syn_params["Uinc"], "gbarS":syn_params["gbarS"]*mS})
    synobj.connect(p=syn_params["w"]) #set w !!!!
    synobj.x_S = 1


    return synobj



Net = Network()
for neural_population_idx, params_neurons in enumerate(params_net["params_neurons"]):
    if params_neurons["name"] in ["pvbas", "cckbas", "aac", "ivy", "bis"]:
        neuron_group = get_int_A_group(params_neurons)
        M_full_V = StateMonitor(neuron_group, 'V', record=0)
    Net.add(neuron_group, M_full_V)


for pre_pop in Net.sorted_objects:
    for post_pop in Net.sorted_objects:
        for syn_params in params_net["params_synapses"]:
            if pre_pop.name == syn_params["pre_name"] and post_pop.name == syn_params["post_name"]:
                print(pre_pop.name, post_pop.name)
                synapses = get_connection_object(pre_pop, post_pop, syn_params)
                Net.add(synapses)





Net.run(200*ms, report='text')

fig, axes = plt.subplots(nrows=1, sharex=True)

axes.plot(M_full_V.t/ms, M_full_V[0].V/mV)
plt.show()


#print(pvbas_params)
