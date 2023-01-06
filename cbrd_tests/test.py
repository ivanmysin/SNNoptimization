
import numpy as np
import matplotlib.pyplot as plt
import h5py


# import tensorflow as tf
# erf = tf.math.erf
# bessel_i0 = tf.math.bessel_i0
# sqrt = tf.math.sqrt
# exp = tf.math.exp
# cos = tf.math.cos
# maximum = tf.math.maximum
# minimum = tf.math.minimum
# abs = tf.math.abs
# logical_and = tf.math.logical_and
# logical_not = tf.math.logical_not
# argmax = tf.math.argmax
#
# SQRT_FROM_2 = np.sqrt(2)
# SQRT_FROM_2_PI = 0.7978845608028654
# PI = np.pi
#
# def limiter(a, b):
#     w = tf.zeros_like(a)
#     selected_indx1 = ((a * b) <= 0)
#     selected_indx2 = (a < 0) & (a * b > 0)
#
#     x1 = abs(a + b) * 0.5
#     x2 = 2.0 * minimum(abs(a), abs(b))
#
#     w = tf.where(selected_indx2, -minimum(x1, x2), w)
#
#     selected_indx3 = logical_not(logical_and(selected_indx1, selected_indx2))
#     w = tf.where(selected_indx3, minimum(x1, x2), w)
#
#     return w
# def update_z(z, dts, Sourse, dt):
#     diff_z = z[1:] - z[:-1]
#     a = diff_z[1:]
#     b = diff_z[:-1]
#     wi = limiter(a, b)
#     a_ = b[1:]
#     b_ = b[:-1]
#     wi_1 = limiter(a_, b_)
#     wi_1 = tf.concat([[0, ], wi_1], axis=0)
#
#     dz_1 = -1 / dts * (diff_z[:-1] + 0.5 * (1 - dt / dts) * (wi - wi_1)) - Sourse[1:-1]
#
#     dz_0 = -1 / dts * z[0] - Sourse[0]
#
#     dz_2 = 1 / dts * (z[-2] + 0.5 * (1 - dt / dts) * wi[-1]) - Sourse[-1]
#
#     dz_0 = tf.reshape(dz_0, [1, ])
#     dz_2 = tf.reshape(dz_2, [1, ])
#
#     dz_dt = tf.concat([dz_0, dz_1, dz_2], axis=0)
#     return dz_dt
# ######################################################################
# z = tf.range(1, 11, 1, dtype=tf.float64)
# Sourse = tf.zeros_like(z)
# dts = 0.1
# dt = 0.1
# print(z)
# for idx in range(2):
#     dzdt = update_z(z, dts, Sourse, dt)
#     #dzdt = tf.tensor_scatter_nd_update(dzdt, [[0], [tf.size(dzdt) - 1]], [0, 0])
#     z = z + dt * dzdt
# print(z)

with h5py.File("../com.hdf5", "r") as file:

    b = file["Solution"][:, 1600]

plt.plot(b)
plt.show()



