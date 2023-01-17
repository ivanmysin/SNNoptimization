

def get_str4Isyn(post_name, params_synapses):
    Isyn_str = ""

    Isyn_sum = []

    isyn_template = """
    Isyn_{pre_name}2{post_name} = g_{pre_name}2{post_name}*({Erev}*mV - V) : ampere
    dg_{pre_name}2{post_name}/dt = -g_{pre_name}2{post_name}/tau_d_{pre_name}2{post_name} : siemens
    tau_d_{pre_name}2{post_name} = {tau_d}*ms : second
    """

    for conn_param in params_synapses:
        if post_name != conn_param["post_name"]: continue

        isyn = isyn_template.format(**conn_param)
        Isyn_str += isyn

        Isyn_sum.append( "Isyn_{pre_name}2{post_name}".format(**conn_param))

    Isyn_sum = "Isyn = " + " + ".join(Isyn_sum) + ": ampere \n"
    Isyn_str = Isyn_sum + Isyn_str
    return Isyn_str