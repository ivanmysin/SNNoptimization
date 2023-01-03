import tensorflow as tf
import cbrd_tfdiffeq as ctfeq

exp = tf.math.exp

def exprel (x):
    return (exp(x) - 1) / x


class Kdr_channelOLM(ctfeq.BaseChannel):

    def __init__(self, params, N, dt=0.1):
        super(Kdr_channelOLM, self).__init__(params, N, dt)

    def get_x_inf_and_tau_x(self, V):
        alpha_n = 0.1 / exprel(-(V + 55) / 10)
        beta_n = 0.125 * exp(-(V + 65) / 80)

        tau_x = 1 / (alpha_n + beta_n)
        x_inf = alpha_n * tau_x
        return x_inf, tau_x

#############################################################################
class KA_channel(ctfeq.BaseChannel):

    def __init__(self, params, N, dt=0.1):
        super(KA_channel, self).__init__(params, N, dt=dt)

        self.list4vars_update = [self.__get_a_inf_and_tau_a, self.__get_b_inf_and_tau_b]

    def get_x_inf_and_tau_x(self, V):
        x_inf = []
        tau_x = []
        for func in self.list4vars_update:
            x_inf_, tau_x_ = func(V)
            x_inf.append(x_inf_)
            tau_x.append(tau_x_)
        x_inf = tf.stack(x_inf)
        tau_x = tf.stack(tau_x)

        return x_inf, tau_x

    def __get_a_inf_and_tau_a(self, V):
        alpha_a = 0.2 / exprel( (13.1 - V) / 10)
        beta_a = 0.175 / exprel( (V - 40.1) / 10)
        tau_a = 1 / (alpha_a + beta_a)
        a_inf = alpha_a * tau_a
        return a_inf, tau_a


    def __get_b_inf_and_tau_b(self, V):
        alpha_b = 0.0016 * exp( (-13 - V) / 18)
        beta_b = 0.05 / (1 + exp((10.1 - V) / 5))

        tau_b = 1 / (alpha_b + beta_b)
        b_inf = alpha_b * tau_b
        return b_inf, tau_b

    def reset(self, dxdt, x4reset):
        dxdt = tf.reshape(dxdt, shape=(self.n_gate_vars, self.N))

        xr = tf.zeros((self.n_gate_vars, self.ref_dvdt_idx), dtype=tf.float64)
        dxdt = tf.concat([xr, dxdt[:, self.ref_dvdt_idx:]], axis=1)
        dxdt = tf.reshape(dxdt, shape=(tf.size(dxdt)))

        dxdt_reset = tf.zeros(self.n_gate_vars, dtype=tf.float64)
        xres = (x4reset[1] + self.x_reset[1]) / self.dt
        dxdt_reset = tf.tensor_scatter_nd_update(dxdt_reset, [[1]], [xres, ])
        return dxdt, dxdt_reset

    def get_y0(self, V):
        x_inf, _ = self.get_x_inf_and_tau_x(V)
        xr1 = tf.zeros((1, self.ref_dvdt_idx), dtype=tf.float64) + self.x_reset[0]
        xr2 = tf.zeros((1, self.ref_dvdt_idx), dtype=tf.float64) + 1.0 #!!!! x_inf[1, 0]
        xr = tf.concat([xr1, xr2], axis=0)
        x_inf = tf.concat([xr, x_inf[:, self.ref_dvdt_idx:]], axis=1)
        x_inf = tf.reshape(x_inf, shape=(tf.size(x_inf)))

        return x_inf

#####################################################################################
class PersistentPotassiumChannel(ctfeq.BaseChannel):
    def __init__(self, params, N, dt=0.1):
        super(PersistentPotassiumChannel, self).__init__(params, N, dt=dt)

        self.list4vars_update = [self.__get_mnap_inf_and_tau_mnap, ]

    def __get_mnap_inf_and_tau_mnap(self, V):
        alpha_mnap = 1.0 / (0.15 * exp(-(V + 38) / 6.5))
        beta_mnap = 1.0 / (0.15 * exprel(-(V + 38) / 6.5 ))

        tau_mnap = 1 / (alpha_mnap + beta_mnap)
        mnap_inf = alpha_mnap * tau_mnap

        return mnap_inf, tau_mnap

    def get_x_inf_and_tau_x(self, V):
        x_inf = []
        tau_x = []
        for func in self.list4vars_update:
            x_inf_, tau_x_ = func(V)
            x_inf.append(x_inf_)
            tau_x.append(tau_x_)
        x_inf = tf.stack(x_inf)
        tau_x = tf.stack(tau_x)

        return x_inf, tau_x


class H_Channel4OLM(ctfeq.BaseChannel):

    def __init__(self, params, N, dt=0.1):
        super(H_Channel4OLM, self).__init__(params, N, dt=dt)

        self.list4vars_update = [self.__get_lso_inf_and_tau_lso, self.__get_lfo_inf_and_tau_lfo,]

    def __get_lso_inf_and_tau_lso(self, V):
        lso_inf = 1 / (1 + exp( (V + 2.83) / 15.9 ))
        tau_lso = 5.6  / (exp( (V - 1.7) / 14 ) + exp(-(V + 260) / 43) )
        return lso_inf, tau_lso

    def __get_lfo_inf_and_tau_lfo(self, V):
        lfo_inf = 1 / (1 + exp( (V + 79.2) / 9.78 ))
        tau_lfo = 0.51 / (exp( (V + 1.7) / 10) + exp(-(V + 340) / 52 )) + 1.0
        return lfo_inf, tau_lfo
    def get_x_inf_and_tau_x(self, V):
        x_inf = []
        tau_x = []
        for func in self.list4vars_update:
            x_inf_, tau_x_ = func(V)
            x_inf.append(x_inf_)
            tau_x.append(tau_x_)
        x_inf = tf.stack(x_inf)
        tau_x = tf.stack(tau_x)

        return x_inf, tau_x

    def get_gch_and_Ich(self, y):
        V = y[self.start_V_idx : self.end_V_idx]
        x = y[self.start_x_idx : self.end_x_idx]
        x = tf.reshape(x, shape=(self.n_gate_vars, self.N) )
        # x = tf.math.pow(x, self.degrees)
        # 0.35*lso + 0.65*lfo
        g = self.gmax * (0.35*x[0, :] + 0.65 * x[1, :])
        I = g * (self.Erev - V)
        return g, I
    def reset(self, dxdt, x4reset):
        dxdt = tf.reshape(dxdt, shape=(self.n_gate_vars, self.N))

        xr = tf.zeros((self.n_gate_vars, self.ref_dvdt_idx), dtype=tf.float64)
        dxdt = tf.concat([xr, dxdt[:, self.ref_dvdt_idx:]], axis=1)
        dxdt = tf.reshape(dxdt, shape=(tf.size(dxdt)))

        # dxdt_reset = tf.zeros(self.n_gate_vars, dtype=tf.float64)
        # xres =
        dxdt_reset = (x4reset + self.x_reset) / self.dt
        return dxdt, dxdt_reset

    def get_y0(self, V):
        x_inf, _ = self.get_x_inf_and_tau_x(V)
        xr1 = tf.zeros((1, self.ref_dvdt_idx), dtype=tf.float64) + 0.2 # lso
        xr2 = tf.zeros((1, self.ref_dvdt_idx), dtype=tf.float64) + 0.01 # lfo
        xr = tf.concat([xr1, xr2], axis=0)
        x_inf = tf.concat([xr, x_inf[:, self.ref_dvdt_idx:]], axis=1)
        x_inf = tf.reshape(x_inf, shape=(tf.size(x_inf)))

        return x_inf



######################################################################################
class Kdr_channelPyrChizhovGraham(ctfeq.BaseChannel):
    def __init__(self, params, N, dt=0.1):
        super(Kdr_channelPyrChizhovGraham, self).__init__(params, N, dt=dt)

        self.list4vars_update = [self.get_a_inf_and_tau_a, self.get_b_inf_and_tau_b]

    def get_x_inf_and_tau_x(self, V):
        x_inf = []
        tau_x = []
        for func in self.list4vars_update:
            x_inf_, tau_x_ = func(V)
            x_inf.append(x_inf_)
            tau_x.append(tau_x_)
        x_inf = tf.stack(x_inf)
        tau_x = tf.stack(tau_x)

        return x_inf, tau_x

    def get_a_inf_and_tau_a(self, V):
        alpha_a = 0.17 * exp( (V + 5) * 0.09)
        beta_a =  0.17 * exp(-(V + 5) * 0.022)
        tau_a = 1 / (alpha_a + beta_a) + 0.8
        a_inf = alpha_a / (alpha_a + beta_a)
        return a_inf, tau_a


    def get_b_inf_and_tau_b(self, V):
        tau_b = tf.zeros_like(V) + 300
        b_inf = 1 / (1 + exp( (V + 68) * 0.038) )
        return b_inf, tau_b

    # def reset(self, dxdt, x4reset):
    #     xr = tf.zeros((self.n_gate_vars, self.ref_dvdt_idx), dtype=tf.float64)
    #     dxdt = tf.concat([xr, dxdt[:, self.ref_dvdt_idx:]], axis=1)
    #     dxdt = tf.reshape(dxdt, shape=(tf.size(dxdt)))
    #     return dxdt
    #
    # def get_y0(self, V):
    #     x_inf, _ = self.get_x_inf_and_tau_x(V)
    #     #x_inf = tf.tensor_scatter_nd_update(x_inf, [[0, 0], [1, 0]], self.x_reset)
    #
    #     xr = tf.zeros((self.ref_dvdt_idx, self.n_gate_vars), dtype=tf.float64) + tf.reshape(self.x_reset, shape=(1, self.n_gate_vars))
    #     xr = tf.transpose(xr)
    #
    #     x_inf = tf.concat([xr, x_inf[:, self.ref_dvdt_idx:]], axis=1)
    #     x_inf = tf.reshape(x_inf, shape=(tf.size(x_inf)))
    #
    #
    #     return x_inf




# import matplotlib.pyplot as plt
# V = tf.linspace(-100, 80, 200)
#
# ka_channel = {
#     "channel_class" : KA_channel,
#
#     "gmax" : 0.0, #10.0,
#     "Erev" : -90.0,
#
#     "degrees" : [1, 1],
#     "x_reset" : [0.31, -0.05],
# }
# ch = KA_channel(ka_channel, 400, 0.1)
# x_inf, tau_x = ch.get_x_inf_and_tau_x(V)
#
# x_inf = tf.reshape(x_inf, shape=(2, -1))
#
# plt.plot(V, x_inf[0, :], label="a")
# plt.plot(V, x_inf[1, :], label="b")
# # plt.plot(V, x_inf2**4, label="int")
# # #plt.plot(V, tau_x)
# # plt.legend(loc = "upper right")
# plt.show()