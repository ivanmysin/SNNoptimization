import sys
sys.path.append("../")
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cbrd_tfdiffeq
import h5py
from code_generated_params import params_net
import pickle

params_net["params_neurons"] = [params_net["params_neurons"][0], ]
params_net["params_generators"] = [params_net["params_generators"][0], ]
params_net["params_synapses"] = [params_net["params_synapses"][9], ]

params_net["params_synapses"][0]["gbarS"] = 10 # 0.908653493
params_net["params_synapses"][0]["w"] = 2 # 0.908653493


with open('/home/ivan/Data/Opt_res/test_params_net.pickle', 'wb') as file:
    pickle.dump(params_net, file)

t = tf.range(0.0, 800.0, 0.1, dtype=tf.float64)
net = cbrd_tfdiffeq.Network(params_net)
y0 = net.get_y0()

solution = net.run_simulation(t, y0)

hf = h5py.File('/home/ivan/Data/interneurons_theta/com.hdf5', 'w')
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