import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tfdiffeq import odeint, odeint_adjoint
import cbrd_tfdiffeq
import h5py
from net_parameters import params_net

t = tf.range(0.0, 1200.0, 0.1, dtype=tf.float64)
net = cbrd_tfdiffeq.Network(params_net)
y0 = net.get_y0()


solution_1 = odeint(net, y0, t[:2000], method="euler")

y0_ = solution_1[-1, :]
solution_2 = odeint(net, y0_, t[2000:], method="euler")

t = t[2000:]
solution = solution_2   #tf.stack(solution_1, solution_2)

fig, axes = plt.subplots(nrows=4, sharex=True)
axes[0].plot(t, solution[:, 0], label="ca3pyr2pvbas")
axes[0].plot(t, solution[:, 2], label="olm2pvbas")
axes[0].legend(loc="upper left")
axes[1].plot(t, solution[:, 3])
axes[1].plot(t, solution[:, 5])
axes[2].plot(t, solution[:, 9])
axes[3].plot(t, solution[:, 809])
plt.show()
