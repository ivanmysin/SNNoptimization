import numpy as np
import tensorflow as tf
from tfdiffeq import odeint
import cbrd_tfdiffeq as ctfeq
import matplotlib.pyplot as plt

synapse_params = {
    "w": 1.0,
    "pre": 0,  # None,
    "post": 1,  # None,
    "tau_f": 12.0,  # ms
    "tau_r": 1912.0, #  ms   # Synaptic depression rate
    "tau_d": 23.08,  #
    "Uinc": 0.153,
    "gbarS": 0.001,
    "Erev": -75.0,
}


synapse = ctfeq.PlasticSynapse([synapse_params, ])
y = tf.Variable([1.0, 0.0, 0.0], dtype=tf.float64)

dt = 0.1
duration = 200.0
nsteps = int(duration / dt)

SRpres = np.zeros(nsteps, dtype=np.float64)
SRpres[::200] = 1.0
t = tf.linspace(0.0, duration, nsteps)
y_hist = []
for idx in range(nsteps):
    #inpt = tf.where( tf.random.uniform(shape=(1, ), maxval=1.0, dtype=tf.float64) > 0.99, 1, 0)

    # inpt = tf.where( (idx%200 == 0), 1.0, 0.0)
    #
    # inpt = tf.reshape(inpt, shape=(1, ))
    # SRpre = tf.cast(inpt, tf.float64) #/ dt
    SRpre = tf.Variable( SRpres[idx] )
    dydt = synapse(t[idx], y, SRpre=SRpre)

    y.assign_add(dt * tf.reshape(dydt, shape=(3, )))
    y_hist.append(y.numpy())

y_hist = np.asarray(y_hist)

#plt.plot(t, y_hist[:, 0], label="X")
plt.plot(t, y_hist[:, 1], label="Y")
#plt.plot(t, y_hist[:, 2], label="U")
# plt.plot(t, SRpres, label="SRpres")
plt.legend(loc="upper left")
plt.show()