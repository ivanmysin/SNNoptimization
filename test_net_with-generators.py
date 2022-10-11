import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tfdiffeq import odeint, odeint_adjoint
import cbrd_tfdiffeq
import h5py


from net_parameters import params_net

t = tf.range(0.0, 1200.0, 0.1, dtype=tf.float64)

# V = tf.zeros(400, dtype=tf.float64) - 90
# ro = tf.zeros(400, dtype=tf.float64)
# ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[399, ]], [1 / 0.5, ]))
#
# simul_y0 = []
#
# # y0syn = tf.Variable([1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=tf.float64)
# X0 = tf.ones(len(params_net["params_synapses"]), dtype=tf.float64)
# R0_U0 = tf.zeros(2 * len(params_net["params_synapses"]), dtype=tf.float64)
# simul_y0.append(X0)
# simul_y0.append(R0_U0)
#
# for _ in range(len(params_net["params_neurons"])):
#     simul_y0.append(ro)
#     simul_y0.append(V)
#
# y0 = tf.cast(tf.concat(simul_y0, axis=0), dtype=tf.float64)

net = cbrd_tfdiffeq.Network(params_net)
y0 = net.get_y0()
solution = odeint(net, y0, t, method="euler")


fig, axes = plt.subplots(nrows=4, sharex=True)
axes[0].plot(t, solution[:, 0], label="ca3pyr2pvbas")
axes[0].plot(t, solution[:, 2], label="olm2pvbas")
axes[0].legend(loc="upper left")
axes[1].plot(t, solution[:, 3])
axes[1].plot(t, solution[:, 5])
axes[2].plot(t, solution[:, 9])
axes[3].plot(t, solution[:, 809])
plt.show()
