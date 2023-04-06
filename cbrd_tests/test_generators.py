import numpy as np
import tensorflow as tf
import cbrd_tfdiffeq as ctfeq
import matplotlib.pyplot as plt

from code_generated_params import params_net


genrators = ctfeq.VonMissesGenerators( params_net["params_neurons"] )
t = tf.range(0, 1000.0, 0.1, dtype=tf.float64)
outs = genrators( tf.reshape(t, shape=(-1, 1)))

sine = 0.5 * (np.cos(2 * np.pi * 0.001* t * 5) + 1)
# fig, axes = plt.subplots( nrows=len(params_net["params_neurons"]), sharex=True )
# for idx, neuron in enumerate(params_net["params_neurons"]):
#     ax = axes[idx]
#     firings = outs[:, idx]
#     ax.plot(t, firings, label=neuron["name"])
#     sine_ampls = sine * np.max(firings)
#     ax.plot(t, sine_ampls, linestyle="--", label = "cos")
#     ax.legend(loc = "upper right")


fig, ax= plt.subplots()
ax.plot(t, outs[:, 0], linewidth=4, color='green')
sine_ampls = sine * np.max(outs[:, 0])
ax.plot(t, sine_ampls, linestyle="--", linewidth=1, color='black')
plt.show()