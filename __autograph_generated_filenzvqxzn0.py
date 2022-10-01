# coding=utf-8
def outer_factory():

    def inner_factory(ag__):

        def tf____call__(self, t, y, SRpre=None):
            with ag__.FunctionScope('__call__', 'fscope', ag__.STD) as fscope:
                do_return = False
                retval_ = ag__.UndefinedReturnValue()
                X = ag__.ld(y)[0::3]
                Y = ag__.ld(y)[1::3]
                U = ag__.ld(y)[2::3]
                y_ = ag__.ld(Y) * ag__.converted_call(ag__.ld(exp), (-ag__.ld(self).dt / ag__.ld(self).tau_d,), None, fscope)
                x_ = 1 + (ag__.ld(X) - 1 + ag__.ld(self).tau1r * ag__.ld(Y)) * ag__.converted_call(ag__.ld(exp), (-ag__.ld(self).dt / ag__.ld(self).tau_r,), None, fscope) - ag__.ld(self).tau1r * ag__.ld(Y)
                u_ = ag__.ld(U) * ag__.converted_call(ag__.ld(exp), (-ag__.ld(self).dt / ag__.ld(self).tau_f,), None, fscope)
                u0 = ag__.ld(u_) + ag__.ld(self).Uinc * (1 - ag__.ld(u_)) * ag__.ld(SRpre)
                y0 = ag__.ld(y_) + ag__.ld(u0) * ag__.ld(x_) * ag__.ld(SRpre)
                x0 = ag__.ld(x_) - ag__.ld(u0) * ag__.ld(x_) * ag__.ld(SRpre)
                dXdt = (ag__.ld(x0) - ag__.ld(X)) / ag__.ld(self).dt
                dYdt = (ag__.ld(y0) - ag__.ld(Y)) / ag__.ld(self).dt
                dUdt = (ag__.ld(u0) - ag__.ld(U)) / ag__.ld(self).dt
                dy_dt = ag__.converted_call(ag__.ld(tf).stack, ([ag__.ld(dXdt), ag__.ld(dYdt), ag__.ld(dUdt)],), None, fscope)
                try:
                    do_return = True
                    retval_ = ag__.ld(dy_dt)
                except:
                    do_return = False
                    raise
                return fscope.ret(retval_, do_return)
        return tf____call__
    return inner_factory