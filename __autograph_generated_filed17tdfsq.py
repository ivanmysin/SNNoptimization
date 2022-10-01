# coding=utf-8
def outer_factory():

    def inner_factory(ag__):

        def tf____call__(self, t, y):
            with ag__.FunctionScope('__call__', 'fscope', ag__.ConversionOptions(recursive=True, user_requested=True, optional_features=(), internal_convert_user_code=True)) as fscope:
                do_return = False
                retval_ = ag__.UndefinedReturnValue()
                dy_dt = []
                firings = ag__.converted_call(ag__.ld(tf).reshape, (ag__.converted_call(ag__.ld(tf).gather, (ag__.ld(y), ag__.ld(self).ro_0_indexes), None, fscope),), dict(shape=(-1,)), fscope)

                def get_state():
                    return ()

                def set_state(block_vars):
                    pass

                def loop_body(itr):
                    synapse = itr
                    y4syn = ag__.ld(y)[ag__.ld(synapse).start_idx:ag__.ld(synapse).end_idx]
                    SRpre = ag__.converted_call(ag__.ld(tf).reshape, (ag__.converted_call(ag__.ld(tf).gather, (ag__.ld(firings), ag__.ld(synapse).pre_indxes), None, fscope),), dict(shape=(-1,)), fscope)
                    dsyn_dt = ag__.converted_call(ag__.ld(synapse), (ag__.ld(t), ag__.ld(y4syn)), dict(SRpre=ag__.ld(SRpre)), fscope)
                    dsyn_dt = ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(dsyn_dt),), dict(shape=(-1,)), fscope)
                    ag__.converted_call(ag__.ld(dy_dt).append, (ag__.ld(dsyn_dt),), None, fscope)
                y4syn = ag__.Undefined('y4syn')
                synapse = ag__.Undefined('synapse')
                dsyn_dt = ag__.Undefined('dsyn_dt')
                SRpre = ag__.Undefined('SRpre')
                ag__.for_stmt(ag__.ld(self).synapses, None, loop_body, get_state, set_state, (), {'iterate_names': 'synapse'})

                def get_state_1():
                    return ()

                def set_state_1(block_vars):
                    pass

                def loop_body_1(itr_1):
                    (neuron_idx, neuron) = itr_1
                    y4neuron = ag__.ld(y)[ag__.ld(neuron).start_idx:ag__.ld(neuron).end_idx]
                    synapse = ag__.ld(self).synapses[0]
                    gsyn_idx = ag__.converted_call(ag__.ld(tf).where, (ag__.ld(synapse).post_indxes == ag__.ld(neuron_idx),), None, fscope)
                    gsyn = ag__.ld(synapse).W * ag__.ld(synapse).gbarS * ag__.converted_call(ag__.ld(tf).reshape, (ag__.converted_call(ag__.ld(tf).gather, (ag__.ld(y), ag__.ld(gsyn_idx)), None, fscope),), dict(shape=(-1, 1)), fscope)
                    Erev = ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(synapse).Erev,), dict(shape=(-1, 1)), fscope)
                    dneur_dt = ag__.converted_call(ag__.ld(neuron), (ag__.ld(t), ag__.ld(y4neuron)), dict(gsyn=ag__.ld(gsyn), Erev=ag__.ld(Erev)), fscope)
                    ag__.converted_call(ag__.ld(dy_dt).append, (ag__.ld(dneur_dt),), None, fscope)
                dneur_dt = ag__.Undefined('dneur_dt')
                neuron_idx = ag__.Undefined('neuron_idx')
                y4neuron = ag__.Undefined('y4neuron')
                Erev = ag__.Undefined('Erev')
                gsyn = ag__.Undefined('gsyn')
                neuron = ag__.Undefined('neuron')
                gsyn_idx = ag__.Undefined('gsyn_idx')
                ag__.for_stmt(ag__.converted_call(ag__.ld(enumerate), (ag__.ld(self).neurons,), None, fscope), None, loop_body_1, get_state_1, set_state_1, (), {'iterate_names': '(neuron_idx, neuron)'})
                dy_dt = ag__.converted_call(ag__.ld(tf).concat, (ag__.ld(dy_dt),), dict(axis=0), fscope)
                try:
                    do_return = True
                    retval_ = ag__.ld(dy_dt)
                except:
                    do_return = False
                    raise
                return fscope.ret(retval_, do_return)
        return tf____call__
    return inner_factory