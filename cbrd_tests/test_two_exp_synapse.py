import sys
sys.path.append("../")
import numpy as np
import tensorflow as tf
from tfdiffeq import odeint
import cbrd_tfdiffeq as ctfeq
from synapse_models import TwoExpSynapse
import matplotlib.pyplot as plt

synapse_params = {
    "pconn": 1.0,
    "pre": 0,  # None,
    "post": 1,  # None,
    "tau_rise": 10.0,  # ms
    "tau_decay": 12.0, #  ms   # Synaptic depression rate
    "gbarS": 0.001,
    "Erev": -75.0,
}

W_new = np.array([0.5, 0.5], dtype=np.float64)
dt = 0.1
duration = 250.0
nsteps = int(duration / dt)

synapse = TwoExpSynapse([synapse_params, synapse_params], dt)

SRpres = np.zeros(nsteps, dtype=np.float64)
SRpres[::400] = 1.0
t = tf.linspace(0.0, duration, nsteps)
y_hist = []
y = synapse.get_y0()
for idx in range(nsteps):

    SRpre = tf.Variable( SRpres[idx] )
    dydt = synapse(t[idx], y, SRpre=SRpre)
    y = y + dt * dydt

    y_hist.append(y.numpy())

y_hist = np.asarray(y_hist)

#plt.plot(t, y_hist[:, 0], label="X")
plt.plot(t, y_hist[:, 0], label="Y")
#plt.plot(t, y_hist[:, 4], label="Y")
#plt.plot(t, y_hist[:, 2], label="U")
# plt.plot(t, SRpres, label="SRpres")
plt.legend(loc="upper left")
# plt.show()
# exp = np.exp
# tau_decay = 12
# tau_rise = 2
#
# t = np.linspace(0, 25, 1000)
# exp_part = (exp(-t / tau_decay) - exp(-t / tau_rise))
# gsyns_new = (tau_rise * tau_decay) / (tau_decay - tau_rise) * exp_part
#
# plt.plot(t, gsyns_new)
plt.show()