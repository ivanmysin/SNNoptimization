import tensorflow as tf

x = tf.range(4, dtype=tf.float64)
x = tf.reshape(x, shape=[4, -1])

d = tf.Variable([4,], dtype=tf.float64)
d = tf.reshape(d, shape=[1, 1])
y = tf.math.pow(x, d)

print(x)
print(d)
print(y)

"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
#from tfdiffeq import odeint

V = tf.random.uniform(shape=[10, 8], dtype=tf.float64)
indices = tf.convert_to_tensor([0, 3, 5], dtype=tf.int32)

Vsl = tf.gather(V, indices, axis=1)

print(V.numpy() )

print("#############################################")
print(Vsl.numpy() )
"""



