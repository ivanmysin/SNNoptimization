import numpy as np
import matplotlib.pyplot as plt

def exprel(x):
    return (exp(x) - 1) / x
exp = np.exp
mymax = np.maximum
mV = 1
ms = 1
V = np.linspace(-100, 80, 500)

# alpha_m = 1.0 / exprel(-(V+40*mV)/(10*mV))/ms
# beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms
alpha_mnap = 1.0 / (0.15 *  exp( -(V + 38*mV)/(6.5*mV)) )/ms
beta_mnap = 1.0 / (0.15 *  exprel( -(V + 38*mV)/(6.5*mV)))/ms

#m = alpha_m/(alpha_m+beta_m)
m = alpha_mnap/(alpha_mnap+beta_mnap)
plt.plot(V, m)

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


