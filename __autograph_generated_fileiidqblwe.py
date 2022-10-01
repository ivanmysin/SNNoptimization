# coding=utf-8
def outer_factory():

    def inner_factory(ag__):

        def tf__limiter(self, a, b):
            with ag__.FunctionScope('limiter', 'fscope', ag__.STD) as fscope:
                do_return = False
                retval_ = ag__.UndefinedReturnValue()
                w = ag__.converted_call(ag__.ld(tf).zeros_like, (ag__.ld(a),), None, fscope)
                selected_indx1 = ag__.ld(a) * ag__.ld(b) <= 0
                selected_indx2 = (ag__.ld(a) < 0) & (ag__.ld(a) * ag__.ld(b) > 0)
                x1 = ag__.converted_call(ag__.ld(abs), (ag__.ld(a) + ag__.ld(b),), None, fscope) * 0.5
                x2 = 2.0 * ag__.converted_call(ag__.ld(minimum), (ag__.converted_call(ag__.ld(abs), (ag__.ld(a),), None, fscope), ag__.converted_call(ag__.ld(abs), (ag__.ld(b),), None, fscope)), None, fscope)
                w = ag__.converted_call(ag__.ld(tf).where, (ag__.ld(selected_indx2), -ag__.converted_call(ag__.ld(minimum), (ag__.ld(x1), ag__.ld(x2)), None, fscope), ag__.ld(w)), None, fscope)
                selected_indx3 = ag__.converted_call(ag__.ld(logical_not), (ag__.converted_call(ag__.ld(logical_and), (ag__.ld(selected_indx1), ag__.ld(selected_indx2)), None, fscope),), None, fscope)
                w = ag__.converted_call(ag__.ld(tf).where, (ag__.ld(selected_indx3), ag__.converted_call(ag__.ld(minimum), (ag__.ld(x1), ag__.ld(x2)), None, fscope), ag__.ld(w)), None, fscope)
                try:
                    do_return = True
                    retval_ = ag__.ld(w)
                except:
                    do_return = False
                    raise
                return fscope.ret(retval_, do_return)
        return tf__limiter
    return inner_factory