# import matplotlib
# matplotlib.use("Qt5Agg")
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import copy

# from scipy.special import erf
# from tensorflow.math import erf, sqrt, exp, maximum, minimum, abs

erf = tf.math.erf
sqrt = tf.math.sqrt
exp = tf.math.exp
maximum = tf.math.maximum
minimum = tf.math.minimum
abs = tf.math.abs
logical_and = tf.math.logical_and
logical_not = tf.math.logical_not

SQRT_FROM_2 = sqrt(2.0)
SQRT_FROM_2_PI = 0.7978845608028654

def H_function(V, dVdt, tau_m, Vt, sigma):
    delta_V = maximum((Vt - V), -1.0) #(Vt - V) #
    #print(delta_V.numpy())
    T = delta_V / sigma / SQRT_FROM_2
    A = exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
    dT_dt = -1.0 / sigma / SQRT_FROM_2 * dVdt
    dT_dt = minimum(0.0, dT_dt)


    F_T = SQRT_FROM_2_PI * exp(-T ** 2) / (1.001 + erf(T))
    B = -SQRT_FROM_2 * dT_dt * F_T * tau_m

    #print(A[-20:].numpy())

    H = (A + B) / tau_m
    return H


V = tf.linspace(-52, -40, 100)
V = tf.cast(V, tf.float32)
dVdt = 0.1*(-60 - V) + 1.8
tau_m = 10
Vt = -50.0
sigma = 0.3

#T = (Vt - V) / sigma / SQRT_FROM_2
delta_V = (Vt - V)
H = H_function(V, dVdt, tau_m, Vt, sigma)
H = H.numpy()
# print(np.sum(H < 0))
# print(H[-20:])
#print(delta_V)

plt.scatter(V.numpy(), H)
plt.show()