# coding=utf-8
def outer_factory():

    def inner_factory(ag__):

        def tf____call__(self, t, y, gsyn=None, Erev=None):
            with ag__.FunctionScope('__call__', 'fscope', ag__.ConversionOptions(recursive=True, user_requested=True, optional_features=(), internal_convert_user_code=True)) as fscope:
                do_return = False
                retval_ = ag__.UndefinedReturnValue()
                ro = ag__.ld(y)[:ag__.ld(self).N]
                V = ag__.ld(y)[ag__.ld(self).N:]

                def get_state():
                    return (dVdt, tau_m)

                def set_state(vars_):
                    nonlocal tau_m, dVdt
                    (dVdt, tau_m) = vars_

                def if_body():
                    nonlocal tau_m, dVdt
                    dVdt = (ag__.ld(self).gl * (ag__.ld(self).El - ag__.ld(V)) + ag__.ld(self).Iext) / ag__.ld(self).C
                    tau_m = ag__.ld(self).C / ag__.ld(self).gl

                def else_body():
                    nonlocal tau_m, dVdt
                    Isyn = ag__.converted_call(ag__.ld(tf).reduce_sum, (ag__.ld(gsyn) * (ag__.ld(Erev) - ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(V),), dict(shape=(1, -1)), fscope)),), dict(axis=0), fscope)
                    dVdt = (ag__.ld(self).gl * (ag__.ld(self).El - ag__.ld(V)) + ag__.ld(self).Iext + ag__.ld(Isyn)) / ag__.ld(self).C
                    tau_m = ag__.ld(self).C / (ag__.ld(self).gl + ag__.converted_call(ag__.ld(tf).reduce_sum, (ag__.ld(gsyn),), None, fscope))
                Isyn = ag__.Undefined('Isyn')
                tau_m = ag__.Undefined('tau_m')
                dVdt = ag__.Undefined('dVdt')
                ag__.if_stmt(ag__.converted_call(ag__.ld(tf).equal, (ag__.converted_call(ag__.ld(tf).size, (ag__.ld(gsyn),), None, fscope), 0), None, fscope), if_body, else_body, get_state, set_state, ('dVdt', 'tau_m'), 2)
                tau_m = ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(tau_m),), dict(shape=(-1,)), fscope)
                dVdt = ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(dVdt),), dict(shape=(-1,)), fscope)
                H = ag__.converted_call(ag__.ld(self).H_function, (ag__.ld(V), ag__.ld(dVdt), ag__.ld(tau_m), ag__.ld(self).Vt, ag__.ld(self).sigma), None, fscope)
                sourse4Pts = ag__.ld(ro) * ag__.ld(H)
                firing = ag__.converted_call(ag__.ld(tf).math.reduce_sum, (ag__.ld(sourse4Pts),), None, fscope)
                sourse4Pts = ag__.converted_call(ag__.ld(tf).tensor_scatter_nd_update, (ag__.ld(sourse4Pts), [[0]], -ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(firing), [1]), None, fscope)), None, fscope)
                dro_dt = ag__.converted_call(ag__.ld(self).update_z, (ag__.ld(ro), ag__.ld(self).dts, ag__.ld(sourse4Pts)), None, fscope)
                dV_dt = ag__.converted_call(ag__.ld(self).update_z, (ag__.ld(V), ag__.ld(self).dts, -ag__.ld(dVdt)), None, fscope)
                dV_dt = ag__.converted_call(ag__.ld(tf).tensor_scatter_nd_update, (ag__.ld(dV_dt), [[0], [ag__.converted_call(ag__.ld(tf).size, (ag__.ld(dV_dt),), None, fscope) - 1]], [0, ag__.ld(dVdt)[-1]]), None, fscope)
                dy_dt = ag__.converted_call(ag__.ld(tf).concat, ([ag__.ld(dro_dt), ag__.ld(dV_dt)],), dict(axis=0), fscope)
                try:
                    do_return = True
                    retval_ = ag__.ld(dy_dt)
                except:
                    do_return = False
                    raise
                return fscope.ret(retval_, do_return)
        return tf____call__
    return inner_factory