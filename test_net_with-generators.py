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


solution = odeint(net, y0, t, method="euler")

hf = h5py.File('/home/ivan/Data/interneurons_theta/solution_Target.hdf5', 'w')
solution_dset = hf.create_dataset('solution', data=solution.numpy() )

fig, axes = plt.subplots(nrows=4, sharex=True)
axes[0].plot(t, solution[:, 0], label="ca3pyr2pvbas")
axes[0].plot(t, solution[:, 2], label="olm2pvbas")
axes[0].legend(loc="upper left")
axes[1].plot(t, solution[:, 3])
axes[1].plot(t, solution[:, 5])
axes[2].plot(t, solution[:, 9])
axes[3].plot(t, solution[:, 809])
plt.show()
