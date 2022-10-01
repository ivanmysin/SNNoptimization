# coding=utf-8
def outer_factory():

    def inner_factory(ag__):

        def tf__H_function(self, V, dVdt, tau_m, Vt, sigma):
            with ag__.FunctionScope('H_function', 'fscope', ag__.STD) as fscope:
                do_return = False
                retval_ = ag__.UndefinedReturnValue()
                delta_V = ag__.converted_call(ag__.ld(maximum), (ag__.ld(Vt) - ag__.ld(V), -1.0), None, fscope)
                T = ag__.ld(delta_V) / ag__.ld(sigma) / ag__.ld(SQRT_FROM_2)
                A = ag__.converted_call(ag__.ld(exp), (0.0061 - 1.12 * ag__.ld(T) - 0.257 * ag__.ld(T) ** 2 - 0.072 * ag__.ld(T) ** 3 - 0.0117 * ag__.ld(T) ** 4,), None, fscope)
                dT_dt = -1.0 / ag__.ld(sigma) / ag__.ld(SQRT_FROM_2) * ag__.ld(dVdt)
                dT_dt = ag__.converted_call(ag__.ld(minimum), (ag__.ld(dT_dt), 0.0), None, fscope)
                F_T = ag__.ld(SQRT_FROM_2_PI) * ag__.converted_call(ag__.ld(exp), (-ag__.ld(T) ** 2,), None, fscope) / (1.000000001 + ag__.converted_call(ag__.ld(erf), (ag__.ld(T),), None, fscope))
                B = -ag__.ld(SQRT_FROM_2) * ag__.ld(dT_dt) * ag__.ld(F_T) * ag__.ld(tau_m)
                H = (ag__.ld(A) + ag__.ld(B)) / ag__.ld(tau_m)
                H = ag__.converted_call(ag__.ld(maximum), (ag__.ld(H), 0.0), None, fscope)
                try:
                    do_return = True
                    retval_ = ag__.ld(H)
                except:
                    do_return = False
                    raise
                return fscope.ret(retval_, do_return)
        return tf__H_function
    return inner_factory