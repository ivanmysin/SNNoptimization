import numpy as np
import matplotlib.pyplot as plt

def exprel(x):
    return (exp(x) - 1) / x
exp = np.exp
mymax = np.maximum
mV = 1
ms = 1
V = np.linspace(-100, 80, 500)

alpha_m = 1.0 / exprel(-(V+40*mV)/(10*mV))/ms
beta_m = 4*exp(-(V+65*mV)/(18*mV))/ms
m = alpha_m/(alpha_m+beta_m)

plt.plot(V, m**3)
plt.show()


