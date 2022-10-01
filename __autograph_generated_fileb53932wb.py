# coding=utf-8
def outer_factory():

    def inner_factory(ag__):

        def tf__update_z(self, z, dts, Sourse):
            with ag__.FunctionScope('update_z', 'fscope', ag__.STD) as fscope:
                do_return = False
                retval_ = ag__.UndefinedReturnValue()
                diff_z = ag__.ld(z)[1:] - ag__.ld(z)[:-1]
                a = ag__.ld(diff_z)[1:]
                b = ag__.ld(diff_z)[:-1]
                wi = ag__.converted_call(ag__.ld(self).limiter, (ag__.ld(a), ag__.ld(b)), None, fscope)
                a_ = ag__.ld(b)[1:]
                b_ = ag__.ld(b)[:-1]
                wi_1 = ag__.converted_call(ag__.ld(self).limiter, (ag__.ld(a_), ag__.ld(b_)), None, fscope)
                wi_1 = ag__.converted_call(ag__.ld(tf).concat, ([[0], ag__.ld(wi_1)],), dict(axis=0), fscope)
                dz_1 = -1 / ag__.ld(dts) * (ag__.ld(diff_z)[:-1] + 0.5 * (1 - 0.1 / ag__.ld(dts)) * (ag__.ld(wi) - ag__.ld(wi_1))) - ag__.ld(Sourse)[1:-1]
                dz_0 = -1 / ag__.ld(dts) * ag__.ld(z)[0] - ag__.ld(Sourse)[0]
                dz_2 = 1 / ag__.ld(dts) * (ag__.ld(z)[-2] + 0.5 * (1 - 0.1 / ag__.ld(dts)) * ag__.ld(wi)[-1]) - ag__.ld(Sourse)[-1]
                dz_0 = ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(dz_0), [1]), None, fscope)
                dz_2 = ag__.converted_call(ag__.ld(tf).reshape, (ag__.ld(dz_2), [1]), None, fscope)
                dz_dt = ag__.converted_call(ag__.ld(tf).concat, ([ag__.ld(dz_0), ag__.ld(dz_1), ag__.ld(dz_2)],), dict(axis=0), fscope)
                try:
                    do_return = True
                    retval_ = ag__.ld(dz_dt)
                except:
                    do_return = False
                    raise
                return fscope.ret(retval_, do_return)
        return tf__update_z
    return inner_factory