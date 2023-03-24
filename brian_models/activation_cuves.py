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
#tau_r =  1 /  (exp(-17.9 - 0.116*V/mV) + exp(-1.84 + 0.09*V/mV) ) + 100
#tau_r = 1 / (exp(-14.59 - 0.086*V/mV) + exp(-1.87 + 0.0701*V/mV) )

alpha_m = 1.0 / exprel(-(V + 40 * mV) / (10 * mV)) / ms
beta_m = 4 * exp(-(V + 65 * mV) / (18 * mV)) / ms
m1 = alpha_m / (alpha_m + beta_m)

alpha_m = 0.1/mV*10*mV/exprel(-(V+35*mV)/(10*mV))/ms
beta_m = 4*exp(-(V+60*mV)/(18*mV))/ms
m2 = alpha_m/(alpha_m+beta_m)

m3 = 1 / (1 + np.exp( -0.08*(V + 26)) )

alpha_h = 0.07 * exp(-(V + 65 * mV) / (20 * mV)) / ms
beta_h = 1. / (exp(-0.1 / mV * (V + 35 * mV)) + 1) / ms
h = alpha_h/(alpha_h+beta_h)
#n = alpha_n/(alpha_n+beta_n)
#m = alpha_m/(alpha_mnap+beta_mnap)
plt.plot(V, m1)
plt.plot(V, h)
# plt.plot(V, m2)
# plt.plot(V, m3)
# plt.plot(V, h)
#plt.plot(V, tau_r)

# alpha_n = 0.1 / exprel(-(V+55*mV)/(10*mV))/ms
# beta_n = 0.125*exp(-(V+65*mV)/(80*mV))/ms
#
# n = alpha_n / (alpha_n + beta_n)
#
# n_a = 1.0 / (1.0 + exp(-0.045 * (V + 10)))
#
# plt.plot(V, n**4)
# plt.plot(V, n_a**4)

plt.ylim(0, 1)
plt.show()


