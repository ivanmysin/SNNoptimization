import numpy as np
import matplotlib.pyplot as plt

def exprel(x):
    return (exp(x) - 1) / x
exp = np.exp
mymax = np.maximum
mV = 1
ms = 1
V = np.linspace(-100, 100, 500)

#tau_r =  1 / (exp(-14.59 - 0.086*V/mV) + exp(-1.87 + 0.0701*V/mV) )
tau_r =  1 /  (exp(-17.9 - 0.116*V/mV) + exp(-1.84 + 0.09*V/mV) ) + 100



# m = alpha_m/(alpha_m+beta_m)
# h = alpha_h/(alpha_h+beta_h)
#n = alpha_n/(alpha_n+beta_n)
#m = alpha_m/(alpha_mnap+beta_mnap)
# plt.plot(V, m)
# plt.plot(V, h)
plt.plot(V, tau_r)

# alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms
# beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms
#
# n = alpha_n / (alpha_n + beta_n)
#
# n_a = 1.0 / (1.0 + exp(-0.045 * (V + 10)))
#
# plt.plot(V, n**4)
# plt.plot(V, n_a**4)
plt.show()


