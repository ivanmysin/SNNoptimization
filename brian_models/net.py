import numpy as np
import sys

sys.path.extend(['/home/ivan/PycharmProjects/SNNoptimization'])
from brian2 import *

defaultclock.dt = 0.1 * ms
import pickle
import net_lib
import h5py
from scipy.signal.windows import parzen


METHOD = 'heun'  # 'exponential_euler'
NNP = 2000
PCONN = 0.5


def get_int_A_group(params_groups, params_net):
    N = NNP
    params = {
        "Iext": params_groups["Iext"] * uA,
        "Cm": params_groups["C"] * uF,  # /cm**2
        "gL": params_groups["gl"] * mS,
        "EL": params_groups["El"] * mV, # -65*mV, #
        "ENa": 55 * mV,
        "EK": params_groups["channels_params"][0]["Erev"] * mV,
        "gNa": 15 * mS, # 50 * mS,
        "gK": params_groups["channels_params"][0]["gmax"] * mS,
        "gKA": params_groups["channels_params"][1]["gmax"] * mS,
        "sigma": 0.3 * mV,
    }

    # Interneuron Model with A-current
    eqs = '''
    dV/dt = (INa + IKdr + IL + IA + Iext + Isyn)/Cm + sigma*xi/ms**0.5 : volt
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
    Isyn_str = net_lib.get_str4Isyn(params_groups, params_net["params_synapses"], NNP, PCONN)

    eqs = eqs.format(isyn_str=Isyn_str)

    neuron = NeuronGroup(N, eqs, method=METHOD, namespace=params, name=params_groups["name"], threshold='V > -10*mV', refractory="15*ms")
    neuron.V = -90 * mV
    for syn in params_net["params_synapses"]:
        rs_val_name = "R_S_{pre_name}2{post_name}".format(pre_name=syn["pre_name"], post_name=syn["post_name"])
        if hasattr(neuron, rs_val_name):
            setattr(neuron, rs_val_name, 1.0)
            #print(getattr(neuron, rs_val_name))

    return neuron


def get_ngf_group(params_groups, params_net):
    N = NNP
    params = {
        "Iext": params_groups["Iext"] * uA,
        "Cm": params_groups["C"] * uF,  # /cm**2
        "gL": params_groups["gl"] * mS,
        "EL": params_groups["El"] * mV, # -65*mV, #
        "ENa": 55 * mV,
        "EK": params_groups["channels_params"][0]["Erev"] * mV,
        "gNa": 50 * mS,
        "gK": params_groups["channels_params"][0]["gmax"] * mS,
        "sigma": 0.3 * mV,
    }

    # Interneuron Model
    eqs = '''
    dV/dt = (INa + IKdr + IL + Iext)/Cm + sigma*xi/ms**0.5 : volt
    IL = gL*(EL - V)           : ampere
    INa = gNa*m**3*h*(ENa - V) : ampere
    IKdr = gK*n**4*(EK - V) : ampere

    m = alpha_m/(alpha_m+beta_m) : 1
    alpha_m = 1.0 / exprel(-(V+40*mV)/(10*mV))/ms : Hz
    beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms : Hz
    dh/dt = (alpha_h*(1-h)-beta_h*h) : 1
    alpha_h = 0.07*exp(-(V+65*mV)/(20*mV))/ms : Hz
    beta_h = 1./(exp(-0.1/mV*(V+35*mV))+1)/ms : Hz
    #dn/dt = (alpha_n*(1-n)-beta_n*n) : 1
    #alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms : Hz
    #beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms : Hz

    dn/dt = (n_inf - n) / tau_n : 1
    tau_n = 0.5*ms + 2.0*ms/(1 + exp(0.045/mV * (V - 50*mV))) : second
    n_inf = 1.0 / (1.0 + exp(-0.045 * (V/mV + 10))) : 1

    {isyn_str}
    '''
    Isyn_str = net_lib.get_str4Isyn(params_groups, params_net["params_synapses"], NNP, PCONN)
    eqs = eqs.format(isyn_str=Isyn_str)

    neuron = NeuronGroup(N, eqs, method=METHOD, namespace=params, name=params_groups["name"], threshold='V > -20*mV', refractory="5*ms")
    neuron.V = -90 * mV
    for syn in params_net["params_synapses"]:
        rs_val_name = "R_S_{pre_name}2{post_name}".format(pre_name=syn["pre_name"], post_name=syn["post_name"])
        if hasattr(neuron, rs_val_name):
            setattr(neuron, rs_val_name, 1.0)
            #print(getattr(neuron, rs_val_name))

    return neuron


def get_olm_group(params_groups, params_net):
    N = NNP
    params = {
        "Iext": params_groups["Iext"] * uA,
        "Cm": params_groups["C"] * uF,  # /cm**2
        "gL": params_groups["gl"] * mS,
        "EL": params_groups["El"] * mV,
        "ENa": 90 * mV,
        "EK": params_groups["channels_params"][0]["Erev"] * mV,
        "EH": params_groups["channels_params"][2]["Erev"] * mV,
        "gNa": 30 * mS,
        "gK": params_groups["channels_params"][0]["gmax"] * mS,
        "gKA": params_groups["channels_params"][1]["gmax"] * mS,
        "gH": params_groups["channels_params"][2]["gmax"] * mS,
        "sigma": 0.3 * mV,
    }

    # OLM Model
    eqs = '''
    dV/dt = (INa + IKdr + IL + IKA + IH + Iext + Isyn)/Cm + sigma*xi/ms**0.5 : volt 

    IL = gL*(EL - V)           : ampere
    INa = gNa*m**3*h*(ENa - V) : ampere
    IKdr = gK*n**4*(EK - V) : ampere
    IKA = gKA * a*b * (EK - V) :  ampere
    IH = gH * rH * (EH - V) :  ampere

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

    drH/dt = (rH_inf - rH) / tau_rH : 1
    rH_inf =  1 / (1 + exp( (V + 84*mV) / (10.2*mV) ) ) : 1
    #tau_rH = 1 / (exp(-14.59 - 0.086*V/mV) + exp(-1.87 + 0.0701*V/mV) ) * ms : second
    tau_rH = 1*ms  /  (exp(-17.9 - 0.116*V/mV) + exp(-1.84 + 0.09*V/mV) ) + 100 * ms : second

    {isyn_str}
    '''
    Isyn_str = net_lib.get_str4Isyn(params_groups, params_net["params_synapses"], NNP, PCONN)
    eqs = eqs.format(isyn_str=Isyn_str)

    #print(eqs)

    neuron = NeuronGroup(N, eqs, method=METHOD, namespace=params, name=params_groups["name"], threshold='V > -10*mV', refractory="5*ms")
    neuron.V = -90 * mV
    neuron.n = 0.09
    neuron.h = 1.0
    for syn in params_net["params_synapses"]:
        rs_val_name = "R_S_{pre_name}2{post_name}".format(pre_name=syn["pre_name"], post_name=syn["post_name"])
        if hasattr(neuron, rs_val_name):
            setattr(neuron, rs_val_name, 1.0)
            #print(getattr(neuron, rs_val_name))

    return neuron


def get_connection_object(pre_pop, post_pop, syn_params):
    # Uinc, tau_r, tau_f, w, gbarS
    #  U_S_{pre_name}2{post_name}_post += W_inp * Uinc * (1 - U_S_{pre_name}2{post_name}_post)
    synapses_action_template = '''
    U_plus = U_S_{pre_name}2{post_name}_post + W_inp * Uinc * (1 - U_S_{pre_name}2{post_name}_post)
    U_S_{pre_name}2{post_name}_post = U_plus
   
    R_S_{pre_name}2{post_name}_post -= W_inp * U_plus * R_S_{pre_name}2{post_name}_post 
    A_S_{pre_name}2{post_name}_post += W_inp * U_plus * R_S_{pre_name}2{post_name}_post
    '''

    #synapses_eqs = synapses_eqs_template.format(**syn_params)
    # synapses_eqs = """
    #                 Uinc : 1
    #                 W_inp : 1
    #                 U_plus : 1
    #                 """
    synapses_action = synapses_action_template.format(**syn_params)

    # print(synapses_eqs)
    # print(synapses_action)
    # print("#############################") model=synapses_eqs,
    W_inp = syn_params["w"] / (NNP * PCONN)

    synobj = Synapses(pre_pop, post_pop,  \
                      on_pre=synapses_action, namespace={"Uinc": syn_params["Uinc"], "W_inp": W_inp})
    synobj.connect(p=PCONN)


    return synobj


def filtrate_params_net(params_net):
    params_net_filtared = {
        "params_neurons": params_net["params_neurons"],
        "params_generators": params_net["params_generators"],
        "params_synapses": [],
    }

    neurons_names = [neuron["name"] for neuron in params_net["params_neurons"]]
    generators_names = [neuron["name"] for neuron in params_net["params_generators"]]

    for synapse in params_net["params_synapses"]:
        if (synapse["pre_name"] in neurons_names) and (synapse["post_name"] in neurons_names):
            params_net_filtared["params_synapses"].append(synapse)

        if (synapse["pre_name"] in generators_names) and (synapse["post_name"] in neurons_names):
            params_net_filtared["params_synapses"].append(synapse)

    return params_net_filtared


###################################################################################################
def get_net_with_params_net(params_net):
    Net = Network()
    SpkMons = []
    for generator_idx, params_generator in enumerate(params_net["params_generators"]):
        #params_generator['freq'] = 6
        rates = net_lib.get_generator_rates(params_generator)
        generator_group = PoissonGroup(NNP, rates=rates, name=params_generator["name"])

        SpkMon = SpikeMonitor(generator_group)
        SpkMons.append(SpkMon)
        Net.add(generator_group, SpkMon)

    for neural_population_idx, params_neurons in enumerate(params_net["params_neurons"]):

        if params_neurons["name"] in ["pvbas", "cckbas", "aac", "ivy", "bis"]:
            neuron_group = get_int_A_group(params_neurons, params_net)
        if params_neurons["name"] in ["ngf", ]:
            neuron_group = get_ngf_group(params_neurons, params_net)

        if params_neurons["name"] in ["olm", ]:
            neuron_group = get_olm_group(params_neurons, params_net)


        SpkMon = SpikeMonitor(neuron_group)
        SpkMons.append(SpkMon)
        Net.add(neuron_group, SpkMon)

        #StMom = StateMonitor(neuron_group, ["A_S_ca3pyr2pvbas", "R_S_ca3pyr2pvbas", "U_S_ca3pyr2pvbas"], record=True)
        #Net.add(StMom)

    for pre_pop in Net.sorted_objects:
        for post_pop in Net.sorted_objects:
            for syn_params in params_net["params_synapses"]:
                if pre_pop.name == syn_params["pre_name"] and post_pop.name == syn_params["post_name"]:
                    #print(pre_pop.name, post_pop.name)
                    synapses = get_connection_object(pre_pop, post_pop, syn_params)
                    Net.add(synapses)

    return Net, SpkMons

def main():
    with open('/home/ivan/Data/Opt_res/params_net.pickle', 'rb') as file:
        params_net = pickle.load(file)
    # params_net = filtrate_params_net(params_net)
    for syn_idx, synapse in enumerate(params_net['params_synapses']):
        synapse["w"] = synapse["w"] / float(defaultclock.dt/ms)  # dt
        #synapse_INDEX = syn_idx

    Net, SpkMons = get_net_with_params_net(params_net)

    Net.run(1800 * ms, report='text')


    # hf = h5py.File('/home/ivan/Data/Opt_res/HH_solution_345!!!.hdf5', 'r')
    # #cbrd_pop_freq = 1000*hf['solution'][:, 3]
    # cbrd_A_S = hf['solution'][:, len(params_net['params_synapses']) + synapse_INDEX]
    # cbrd_U_S = hf['solution'][:, 2*len(params_net['params_synapses']) + synapse_INDEX]
    # cbrd_R_S = hf['solution'][:, synapse_INDEX]
    # hf.close()

    resfile = h5py.File('/home/ivan/Data/interneurons_theta/Monte_Carlo.hdf5', "w")
    fig, axes = plt.subplots(nrows=len(SpkMons), sharex=True)
    for pops_idx, SpkMon in enumerate(SpkMons):
        # print( np.asarray(SpkMon.t).size / 0.2)
        # print(SpkMon.source.name)
        pop_freq, bins = np.histogram(SpkMon.t/ms, range=[0, 1800], bins=18001)
        win = parzen(11)
        win = win / np.sum(win)
        pop_freq = np.convolve(pop_freq, win, mode='same')

        dbins = bins[1] - bins[0]
        pop_freq = pop_freq / NNP / (0.001*dbins)
        axes[pops_idx].plot(bins[:-1], pop_freq)

        # if pops_idx == 0:
        #     t4gen, dt4gen = np.linspace(0, 1.8, 1800, retstep=True)
        #     omega = params_net["params_generators"][0]['freq']
        #     kappa, I0 = net_lib.r2kappa(params_net["params_generators"][0]['R'])
        #     gener = 0.5 / I0 * np.exp(kappa * np.cos(2*np.pi*omega*t4gen - params_net["params_generators"][0]['phase']) ) # * 0.001
        #     axes[pops_idx].plot(1000*t4gen, gener)

        # if pops_idx > 0:
        #     t_4bcrd = np.arange(0, 0.1*cbrd_A_S.size, 0.1)
            # axes[pops_idx].plot(t_4bcrd, cbrd_pop_freq)


        #axes[pops_idx].scatter(SpkMon.t/ms, SpkMon.i)
        axes[pops_idx].set_title(SpkMon.source.name)

        resfile.create_dataset(SpkMon.source.name + "_times", data=SpkMon.t / ms)
        resfile.create_dataset(SpkMon.source.name + "_indexes", data=SpkMon.i)

    # mean_as = StMom.A_S_ca3pyr2pvbas[0, :] # np.mean(StMom.A_S_ca3pyr2pvbas, axis=0) # StMom.A_S_ca3pyr2pvbas[0, :] #
    # axes[pops_idx+1].plot(StMom.t/ms, mean_as)
    # axes[pops_idx+1].plot(t_4bcrd, cbrd_A_S)
    #
    #
    # axes[pops_idx+2].plot(t_4bcrd, cbrd_R_S)
    # axes[pops_idx+2].plot(StMom.t/ms, StMom.R_S_ca3pyr2pvbas[0, :])
    #
    # axes[pops_idx+3].plot(t_4bcrd, cbrd_U_S)
    # axes[pops_idx+3].plot(StMom.t/ms, StMom.U_S_ca3pyr2pvbas[0, :])


    resfile.close()
    #axes.plot(M_full_V.t/ms, M_full_V[0].V/mV)
    plt.show()

########################################################
if __name__ == '__main__':
    main()
