import tensorflow as tf

a = tf.ones(shape=(5, 7), dtype=tf.float64)
b = tf.zeros(shape=(5, 4), dtype=tf.float64)

c = tf.concat([a, b], axis=1)


print(c.numpy())

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



