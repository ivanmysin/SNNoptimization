import numpy as np
import tensorflow as tf
from tfdiffeq import odeint
import cbrd_tfdiffeq as ctfeq
import matplotlib.pyplot as plt


params1 = {
    "R" : 0.3,
    "freq" : 5,
    "mean_spike_rate" : 18,
    "phase" : 0,
}

params2 = {
    "R" : 0.3,
    "freq" : 5,
    "mean_spike_rate" : 10,
    "phase" : np.pi,
}

genrator = ctfeq.VonMissesGenerators( [params1, params2] )

t = tf.range(0, 400, 0.1, dtype=tf.float64)
out = []
for idx in range(tf.size(t)):
    out.append( genrator(t[idx]) )
out = tf.stack(out)

plt.plot(t, out[:, 0])
plt.plot(t, out[:, 1])

out_means = tf.reduce_mean(out, axis=0) / 0.1
print(out_means.numpy())
plt.show()