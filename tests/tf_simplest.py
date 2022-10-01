import tensorflow as tf
import tensorflow_probability as tfp

t_init, t0, t1 = 0., 0.5, 1.
y_init = tf.constant([1., 1.], dtype=tf.float64)
A = tf.constant([[-1., -2.], [-3., -4.]], dtype=tf.float64)

def ode_fn(t, y, A):
  return tf.linalg.matvec(A, y)

with tf.GradientTape() as tape:
  tape.watch(A)
  results = tfp.math.ode.BDF().solve(ode_fn, t_init, y_init,
                                     solution_times=[t0, t1],
                                     constants={'A': A})
grad = tape.gradient(results.states, A)  # Fine.
print(grad)