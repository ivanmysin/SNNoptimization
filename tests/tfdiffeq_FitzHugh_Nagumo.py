import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tfdiffeq import odeint

def forward(Iext, dt, N, a, b, tau_u):
    v = -1.7
    u = 0
    V = np.zeros(N, dtype=np.float64)
    U = np.zeros_like(V)
    for idx in range(N):
        V[idx] = v
        U[idx] = u
        v = v + dt * (v - (v**3)/3 - u + Iext)
        u = u + dt * (v + a - b*u) / tau_u
    V[-1] = v
    U[-1] = u

    return V, U


class ODEFunc(tf.keras.Model):

    def __init__(self, Iext, **kwargs):
        super(ODEFunc, self).__init__(**kwargs)
        self.Iext = Iext
        self.a = tf.constant(0.7, dtype=tf.float64)
        self.b = tf.constant(0.8, dtype=tf.float64)
        self.tau_u = tf.constant(12.5, dtype=tf.float64)

    @tf.function
    def __call__(self, t, y):
        dv_dt = y[0] - (y[0] ** 3) / 3 - y[1] + self.Iext
        du_dt = (y[0] + self.a - self.b * y[1]) / self.tau_u

        return tf.stack([dv_dt, du_dt], axis=0)

dt = 0.01
t0, t1 = 0., 15.
solution_times = tf.convert_to_tensor(np.arange(0, t1, dt), dtype=tf.float64)  # np.linspace(t0, t1, 100)
y_init = tf.constant([-1.7, 0.], dtype=tf.float64)
Iext_target = tf.constant(0.5, dtype=tf.float64)
Iext_start = tf.Variable(0.4, dtype=tf.float64)
Vtarget, U = forward(0.5, dt, np.arange(0, t1, dt).size, 0.7, 0.8, 12.5)

lr = 1e-3
optimizer = tf.keras.optimizers.Adam(lr)
ode_fn = ODEFunc(Iext_start)

for itr in range(1, 10):
    with tf.GradientTape() as tape:
        tape.watch(ode_fn.Iext)
        pred_y = odeint(ode_fn, y_init, solution_times)
        loss = 0.5*dt*tf.math.squared_difference(pred_y[:, 0], Vtarget, name='Loss')
        grad = tape.gradient(loss, ode_fn.Iext)
        # print(loss, grad)
        grad_vars = zip([grad, ],  [ode_fn.Iext, ])
        optimizer.apply_gradients(grad_vars)

print(ode_fn.Iext)



plt.plot(solution_times, pred_y[:, 0])
plt.plot(solution_times, Vtarget)
plt.show()