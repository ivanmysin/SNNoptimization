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


def get_int_group(params_groups, params_net):
    N = NNP
    params = {
        "Iext": params_groups["Iext"] * uA,
        "Cm": params_groups["C"] * uF,  # /cm**2
        "gL": params_groups["gl"] * mS,
        "EL": params_groups["El"] * mV,  # -65*mV, #
        "sigma": 0.3 * mV,
        "Vreset": params_groups["Vreset"] * mV,
        "VT": params_groups["Vt"] * mV,
        "refactory" : params_groups["refactory"] * ms,
    }

    # Simplest Interneuron Model
    eqs = '''
    dV/dt = (IL + Iext + Isyn)/Cm + sigma*xi/ms**0.5 : volt  (unless refractory)
    IL = gL*(EL - V)           : ampere
    {isyn_str}
    '''
    Isyn_str = net_lib.get_str4Isyn(params_groups, params_net["params_synapses"], NNP, PCONN)

    eqs = eqs.format(isyn_str=Isyn_str)
    neuron = NeuronGroup(N, eqs, method=METHOD, namespace=params, name=params_groups["name"], threshold='V > VT',
                         refractory=params["refactory"], reset="V = Vreset" )
    neuron.V = -90 * mV


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

    # synapses_eqs = synapses_eqs_template.format(**syn_params)
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

    synobj = Synapses(pre_pop, post_pop, \
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
        # params_generator['freq'] = 6
        rates = net_lib.get_generator_rates(params_generator)
        generator_group = PoissonGroup(NNP, rates=rates, name=params_generator["name"])

        SpkMon = SpikeMonitor(generator_group)
        SpkMons.append(SpkMon)
        Net.add(generator_group, SpkMon)

    for neural_population_idx, params_neurons in enumerate(params_net["params_neurons"]):
        neuron_group = get_int_group(params_neurons, params_net)

        SpkMon = SpikeMonitor(neuron_group)
        SpkMons.append(SpkMon)
        Net.add(neuron_group, SpkMon)


        # StMom = StateMonitor(neuron_group, ["A_S_ca3pyr2pvbas", "R_S_ca3pyr2pvbas", "U_S_ca3pyr2pvbas"], record=True)
        # Net.add(StMom)

    for pre_pop in Net.sorted_objects:
        for post_pop in Net.sorted_objects:
            for syn_params in params_net["params_synapses"]:
                if pre_pop.name == syn_params["pre_name"] and post_pop.name == syn_params["post_name"]:
                    # print(pre_pop.name, post_pop.name)
                    synapses = get_connection_object(pre_pop, post_pop, syn_params)
                    Net.add(synapses)

    return Net, SpkMons


def main():
    with open('/home/ivan/Data/Opt_res/LIF_params_net.pickle', 'rb') as file:
        params_net = pickle.load(file)
    # params_net = filtrate_params_net(params_net)
    for syn_idx, synapse in enumerate(params_net['params_synapses']):
        synapse["w"] = synapse["w"] / float(defaultclock.dt / ms)  # dt

    Net, SpkMons = get_net_with_params_net(params_net)

    Net.run(1800 * ms, report='text')

    # hf = h5py.File('/home/ivan/Data/Opt_res/HH_solution_345!!!.hdf5', 'r')
    # #cbrd_pop_freq = 1000*hf['solution'][:, 3]
    # cbrd_A_S = hf['solution'][:, len(params_net['params_synapses']) + synapse_INDEX]
    # cbrd_U_S = hf['solution'][:, 2*len(params_net['params_synapses']) + synapse_INDEX]
    # cbrd_R_S = hf['solution'][:, synapse_INDEX]
    # hf.close()

    resfile = h5py.File('/home/ivan/Data/interneurons_theta/LIF_Monte_Carlo.hdf5', "w")
    fig, axes = plt.subplots(nrows=len(SpkMons), sharex=True)
    for pops_idx, SpkMon in enumerate(SpkMons):
        # print( np.asarray(SpkMon.t).size / 0.2)
        # print(SpkMon.source.name)
        pop_freq, bins = np.histogram(SpkMon.t / ms, range=[0, 1800], bins=18001)
        win = parzen(11)
        win = win / np.sum(win)
        pop_freq = np.convolve(pop_freq, win, mode='same')

        dbins = bins[1] - bins[0]
        pop_freq = pop_freq / NNP / (0.001 * dbins)
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

        # axes[pops_idx].scatter(SpkMon.t/ms, SpkMon.i)
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
    # axes.plot(M_full_V.t/ms, M_full_V[0].V/mV)
    plt.show()


########################################################
if __name__ == '__main__':
    main()
