import numpy as np
from scipy.special import i0 as bessel
from copy import deepcopy

RNG = np.random.default_rng()

def r2kappa(R):
    """
    recalulate kappa from R for von Misses function
    """
    if R < 0.53:
        kappa = 2 * R + R**3 + 5/6 * R**5

    elif R >= 0.53 and R < 0.85:
        kappa = -0.4 + 1.39 * R + 0.43 / (1 - R)

    elif R >= 0.85:
        kappa = 1 / (3*R - 4*R**2 + R**3)


    I0 = bessel(kappa)

    return kappa, I0


def get_generator_rates(generator_params):
    rates_template = '{fr} * Hz * exp({kappa} * cos(2*pi*{freq}*Hz*t - {phase}) )'

    kappa, IO = r2kappa(generator_params["R"])
    generator_params["kappa"] = kappa
    generator_params["fr"] = generator_params["mean_spike_rate"] / IO

    rates = rates_template.format(**generator_params)

    return rates

def get_str4Isyn(post_params, params_synapses, NNP, PCONN):
    post_name = post_params["name"]

    Isyn_str = ""

    Isyn_sum = []

    isyn_template = """
    Isyn_{pre_name}2{post_name} = g_syn_{pre_name}2{post_name} * ({Erev}*mV - V) : ampere
    g_syn_{pre_name}2{post_name} = {gbarS}*mS * A_S_{pre_name}2{post_name} : siemens
    dA_S_{pre_name}2{post_name}/dt = -A_S_{pre_name}2{post_name}/tau_d_{pre_name}2{post_name} : 1 
    dU_S_{pre_name}2{post_name}/dt = -U_S_{pre_name}2{post_name}/tau_f_{pre_name}2{post_name} : 1  
    dR_S_{pre_name}2{post_name}/dt = (1 - R_S_{pre_name}2{post_name} - A_S_{pre_name}2{post_name}) / tau_r_{pre_name}2{post_name} : 1  
    
    tau_d_{pre_name}2{post_name} = {tau_d}*ms : second
    tau_r_{pre_name}2{post_name} = {tau_r}*ms : second
    tau_f_{pre_name}2{post_name} = {tau_f}*ms : second
    """

    for conn_param in params_synapses:
        if post_name != conn_param["post_name"]: continue

        # Wconn = conn_param['w'] * conn_param['gbarS'] / NNP / PCONN
        # #gbar_str = "gbarS_{pre_name}2{post_name}".format(**conn_param)
        # conn_param["gbarS"] = Wconn

        isyn = isyn_template.format(**conn_param)
        Isyn_str += isyn

        Isyn_sum.append( "Isyn_{pre_name}2{post_name}".format(**conn_param))

    Isyn_sum = "Isyn = " + " + ".join(Isyn_sum) + ": ampere \n"
    Isyn_str = Isyn_sum + Isyn_str
    return Isyn_str