import tensorflow as tf
@tf.function
def func ():
    dx_dt_list = tf.TensorArray(tf.float64, size=0, dynamic_size=True) # = []
    dx_dt_list_idx = 0
    for _ in range(3):
        dxdt = tf.random.normal((4, ), mean=0.0, stddev=1.0, dtype=tf.dtypes.float64)
        dx_dt_list = dx_dt_list.write(dx_dt_list_idx, dxdt)
        dx_dt_list_idx = dx_dt_list_idx + 1
    dx_dt_list = dx_dt_list.stack()
    return dx_dt_list

dx_dt_list = func()
print(dx_dt_list.numpy())

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



