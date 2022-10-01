import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
import matplotlib.pyplot as plt
import time

dt = 0.1
t0, t1 = 0., 15.
solution_times = np.arange(0, t1, dt)  # np.linspace(t0, t1, 100)
y_init = tf.constant([-1.7, 0.], dtype=tf.float64)
Iext_target = tf.constant(0.5, dtype=tf.float64)

a = tf.constant(0.7, dtype=tf.float64)
b = tf.constant(0.8, dtype=tf.float64)
tau_u = tf.constant(12.5, dtype=tf.float64)

@tf.function
def ode_fn(t, y, Iext, a, b, tau_u):

    dv_dt = y[0] - (y[0]**3) / 3 - y[1] + Iext
    du_dt = (y[0] + a - b * y[1]) / tau_u

    return tf.stack([dv_dt, du_dt], axis=0)

results = tfp.math.ode.DormandPrince().solve(ode_fn, t0, y_init,
                                     solution_times=solution_times,
                                     constants={'Iext': Iext_target,
                                                'a' : a,
                                                'b' : b,
                                                'tau_u' : tau_u})
Vtarget = np.asarray(results.states[:, 0])

Vtarget = tf.convert_to_tensor(Vtarget, dtype=tf.float64)

print("Hello")

Iext = tf.constant(0.4, dtype=tf.float64)
with tf.GradientTape(persistent=False) as tape:
  tape.watch(Iext)

  solver = tfp.math.ode.DormandPrince(rtol=0.001, atol=1e-03, first_step_size=0.1, safety_factor=0.9)
  results = solver.solve(ode_fn, t0, y_init,
                                     solution_times=solution_times,
                                     constants={'Iext': Iext,
                                                'a' : a,
                                                'b' : b,
                                                'tau_u' : tau_u})
  print("Hello")
  Loss = 0.5*dt*tf.math.squared_difference(results.states[:, 0], Vtarget, name='Loss')
  print("start timer")
  timer = time.time()
  grad = tape.gradient(Loss, Iext)  # Fine.
  print("Grad computation ", time.time() - timer)
  print(grad)

plt.plot(solution_times, Vtarget )
plt.plot(solution_times, results.states[:, 0] )
plt.show()