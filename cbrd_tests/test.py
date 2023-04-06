import h5py

path = '/home/ivan/Data/phase_relations/MC_theta_freq/4.hdf5'

file = h5py.File(path, mode='r')
print(file.keys())

pvbas_times = file['pvbas_times'][:]
print(pvbas_times[:5])
file.close()
# import tensorflow as tf
# @tf.function
# def func (a, b):
#     a = tf.reshape(a, (-1, 1))
#     b = tf.reshape(b, (1, -1))
#     prod = a@b
#     c = tf.math.reduce_sum(prod, axis=0)
#     return c
#
#
#
# a = tf.ones([100, 2], dtype=tf.float64)
# b = tf.ones([10, ], dtype=tf.float64)
#
# c = func (a, b)
# print(c.numpy())


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



