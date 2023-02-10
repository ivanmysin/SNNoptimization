import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tfdiffeq import odeint, odeint_adjoint
import cbrd_tfdiffeq
import h5py
from code_generated_params import params_net

t = tf.range(0.0, 800.0, 0.1, dtype=tf.float64)
net = cbrd_tfdiffeq.Network(params_net)
y0 = net.get_y0()


solution = odeint(net, y0, t, method="euler")

hf = h5py.File('com.hdf5', 'w')
solution_dset = hf.create_dataset('solution', data=solution.numpy() )
hf.close()


fig, axes = plt.subplots(nrows=4, sharex=True)
axes[0].plot(t, solution[:, 1], label="ca3pyr2pvbas")
# axes[0].plot(t, solution[:, 2], label="olm2pvbas")
# axes[0].legend(loc="upper left")

axes[1].plot(t, solution[:, 3])
# axes[1].plot(t, solution[:, 5])
axes[2].plot(t, solution[:, 802]) # 1602

axes[3].plot( solution[-1, 403:803] ) # 803:1603
plt.show()
