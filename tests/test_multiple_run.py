import numpy as np
import tensorflow as tf
from tfdiffeq import odeint
import matplotlib.pyplot as plt

class ODEFunc(tf.keras.Model):

    def __init__(self, Iext, **kwargs):
        super(ODEFunc, self).__init__(**kwargs)
        self.Iext = tf.constant(Iext, dtype=tf.float64)
        self.a = tf.constant(0.7, dtype=tf.float64)
        self.b = tf.constant(0.8, dtype=tf.float64)
        self.tau_u = tf.constant(12.5, dtype=tf.float64)

    def __call__(self, t, y):
        dv_dt = y[0] - (y[0] ** 3) / 3 - y[1] + self.Iext
        du_dt = (y[0] + self.a - self.b * y[1]) / self.tau_u
        return tf.stack([dv_dt, du_dt], axis=0)

model = ODEFunc(0.5)
y0 = tf.constant([-1.7, 0.], dtype=tf.float64)
t = tf.range(0.0, 1000.0, 0.1, dtype=tf.float64)

sol_1 = odeint(model, y0, t, method="euler")

win = 100
n_iter = int(tf.size(t) / win)
sol_2 = []
for idx in range(n_iter):

    if idx == 0:
        winstart = idx * win
        winend = winstart + win
    else:
        winstart = idx * win - 1
        winend = winstart + win + 1

    tslice = t[winstart:winend]
    sol_tmp = odeint(model, y0, tslice, method="euler")
    y0 = sol_tmp[-1, :]

    if idx == 0:
        sol_2.append(sol_tmp)
    else:
        sol_2.append(sol_tmp[1:])
    #print(idx, tslice[0], tslice[-1])

sol_2  = tf.concat(sol_2, axis=0)




fig, axes = plt.subplots(nrows=2)
axes[0].plot(t, sol_1[:, 0], linewidth=2, color='green')
axes[0].plot(t, sol_2[:, 0], linewidth=1, color='red')

axes[1].plot(t, sol_1[:, 1], linewidth=2, color='green')
axes[1].plot(t, sol_2[:, 1], linewidth=1, color='red')


plt.show()