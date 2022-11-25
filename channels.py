import tensorflow as tf
import cbrd_tfdiffeq as ctfeq

exp = tf.math.exp

def exprel (x):
    return (exp(x) - 1) / x


class Kdr_channel(ctfeq.BaseChannel):

    # def __init__(self, params, N, dt=0.1):
    #     super(Kdr_channel, self).__init__(params, N, dt)

    def get_x_inf_and_tau_x(self, V):
        alpha_n = 0.1 / exprel(-(V + 55) / 10)
        beta_n = 0.125 * exp(-(V + 65) / 80)

        tau_x = 1 / (alpha_n + beta_n)
        x_inf = alpha_n * tau_x
        return x_inf, tau_x


# import matplotlib.pyplot as plt
#
# V = tf.linspace(-100, 80, 200)
# alpha_n = 0.1 / exprel(-(V + 55) / 10)
# beta_n = 0.125 * exp(-(V + 65) / 80)
#
# tau_x = 1 / (alpha_n + beta_n)
# x_inf = alpha_n * tau_x
#
# x_inf2 = 1.0 / (1.0 + exp(-0.045 * (V + 10)))
#
# plt.plot(V, x_inf**4, label="ngf")
# plt.plot(V, x_inf2**4, label="int")
# #plt.plot(V, tau_x)
# plt.legend(loc = "upper right")
# plt.show()