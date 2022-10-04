
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
#from tfdiffeq import odeint


#
# print(Isyn)

# V = tf.random.uniform(shape=[10, ], dtype=tf.float64)
# #indices = tf.convert_to_tensor([0, 3, 5], dtype=tf.int32)
# indices = tf.where(V > 0.5) # tf.convert_to_tensor([0, 3, 5], dtype=tf.int32)
# Vsl = tf.gather(V, indices)

# print(V)
# print(Vsl)
# a = 0.0
# V = tf.transpose(a)
#
# print(V)

t = 0.1*tf.range(0.0, 500.0, dtype=tf.float64)

print(t.numpy())


