# import matplotlib
# matplotlib.use("Qt5Agg")
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

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

def H_function(V, dV_dt, Vt, dt, tau_m, sigma):
    k = tau_m / dt
    g_tot = 1 / tau_m # (Cm = 1) !!!!

    T = sqrt(0.5*(1+k)) * g_tot * (Vt - V) / sigma

    A_inf = exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
    A = A_inf * (1 - (1 + k)**(-0.71 + 0.0825 * (T + 3) ) )

    dT_dt = -g_tot/sigma * sqrt(0.5+0.5*k) * dV_dt

    # dT_dt[dT_dt < 0] = 0
    dT_dt = maximum(0.0, dT_dt)

    F_T = np.sqrt(2.0/np.pi) * exp(-T**2) / (1 + erf(T))

    B = -np.sqrt(2.0) * tau_m * dT_dt * F_T

    H = A + B

    return H
#############################################################################################
def limiter(a, b):
    w = tf.zeros_like(a)

    selected_indx1 = ( (a * b) <= 0 )

    selected_indx2 = (a < 0) & (a * b > 0)

    # x1 = abs(tf.boolean_mask(a, selected_indx2) + tf.boolean_mask(b, selected_indx2) ) * 0.5
    # x2 = 2.0 * minimum( abs(tf.boolean_mask(a, selected_indx2)), abs(tf.boolean_mask(b, selected_indx2)))

    x1 = abs(a + b) * 0.5
    x2 = 2.0 * minimum( abs(a), abs(b) )
    # w[selected_indx2] = -minimum(x1, x2)
    w = tf.where(selected_indx2, -minimum(x1, x2), w)

    # selected_indx3 = np.logical_not(selected_indx1 & selected_indx2)
    selected_indx3 = logical_not( logical_and(selected_indx1, selected_indx2))
    # x1 = abs(a + b) * 0.5
    # x2 = 2.0 * minimum( abs(a), abs(b))
    #
    # w[selected_indx3] = np.minimum(x1, x2)
    w = tf.where(selected_indx3, minimum(x1, x2), w)

    return w

#############################################################################################
def update_z(z, dt, dts, Sourse):


    S = Sourse

    diff_z = z[1:] - z[:-1]  # np.diff(z)


    a = diff_z[1:]
    b = diff_z[:-1]

    wi = limiter(a, b)

    a_ = b[1:]
    b_ = b[:-1]
    wi_1 = limiter(a_, b_)

    wi_1 = tf.concat( [[0, ], wi_1], axis=0 ) # np.append(0, wi_1)

    # dz[1:-1] = -dt/dts * ( diff_z[:-1] + dt / dts * (wi - wi_1)) - dt * S[1:-1]

    dz_1 = -dt / dts * (diff_z[:-1] + dt / dts * (wi - wi_1)) - dt * S[1:-1]


    # dz = tf.tensor_scatter_nd_add(dz, indices=[range(1, diff_z.size)], updates=-dt/dts * ( diff_z[:-1] + dt / dts * (wi - wi_1)) - dt * S[1:-1])

    # dz = tf.zeros_like(z)
    dz_0 = -dt/dts * z[0] - dt * S[0]  # dz[0] = -dt/dts * z[0] - dt * S[0]
    dz_2 = dt/dts * (z[-2] + dt/dts * wi[-1]) - dt * S[-1] # dz[-1] = dt/dts * (z[-2] + dt/dts * wi[-1]) - dt * S[-1]

    dz_0 = tf.reshape(dz_0, [1, ])
    dz_2 = tf.reshape(dz_2, [1, ])

    dz = tf.concat([dz_0, dz_1, dz_2], axis=0)
    return dz
######################################################################################


# np.random.seed(0)
# a = np.random.randn(5)
# b = np.random.randn(5)
#
# a = tf.convert_to_tensor(a, dtype=tf.float64)
# b = tf.convert_to_tensor(b, dtype=tf.float64)
#
# w = limiter(a, b)
# print(w)

Pts = np.zeros(400, dtype=np.float64)
Pts[-1] = 1
V = np.zeros_like(Pts)
#V[-1] = 9

dt = 0.1
dts = 0.5
tau_m = 10.0
Vr=0.0
Vt=10.0
Iext=15.0
sigma=1.5

dV_dt = (-V + Iext) / tau_m

V = tf.Variable(V, dtype=tf.float64)
dV_dt = tf.Variable(dV_dt, dtype=tf.float64)
Vt = tf.constant(Vt, dtype=tf.float64)
Vr = tf.constant(Vr, dtype=tf.float64)
tau_m = tf.constant(tau_m, dtype=tf.float64)
Iext = tf.constant(Iext, dtype=tf.float64)
sigma = tf.constant(sigma, dtype=tf.float64)
dt = tf.constant(dt, dtype=tf.float64)
dts = tf.constant(dts, dtype=tf.float64)

spike_rate = []

with tf.GradientTape(persistent=False) as tape:
    tape.watch(Iext)

    for _ in range(1000):
        dV_dt = (-V + Iext) / tau_m

        H = H_function(V, dV_dt, Vt, dt, tau_m, sigma)
        sourse4Pts = Pts * H

        # sourse4Pts[0] = -tf.math.reduce_sum(sourse4Pts)
        firing = -tf.math.reduce_sum(sourse4Pts)

        sourse4Pts = tf.tensor_scatter_nd_update(sourse4Pts, [[0], ], tf.reshape(firing, [1, ]) )

        dPts = update_z(Pts, dt, dts, sourse4Pts)
        dV = update_z(V, dt, dts, -dV_dt)

        # # print(dPts)
        # spike_rate.append(Pts[0])  # sourse4Pts[0]
        # V_hist.append(V[-1])
        # print(dV)
        # dV[0] = 0
        # dV = tf.where([True, ], [0, ], dV)
        #dV[-1] = dt * dV_dt[-1]
        dV = tf.tensor_scatter_nd_update(dV, [[0], [tf.size(dV)-1]], [0, dt * dV_dt[-1]])

        # Pts += dPts
        Pts = tf.math.add(Pts, dPts)

        # print(V)
        # V += dV
        V = tf.math.add(V, dV)
        # print(dV[-1], V[-1])
        spike_rate.append(-float(firing.numpy()))
        # print("#########################")

    grad = tape.gradient(firing, Iext)

    print(grad)

plt.plot(spike_rate)
# plt.plot(V_hist)
plt.show()

