import numpy as np
import tensorflow as tf
#from tensorflow.keras.metrics import mean_squared_logarithmic_error
from tensorflow.keras.optimizers import Adam
from tfdiffeq import odeint, odeint_adjoint
import cbrd_tfdiffeq
import h5py

from code_generated_params import params_net

AdamOptimizer = Adam(learning_rate=0.01)

def Loss_func(y_true, y_pred): # = mean_squared_logarithmic_error
    L = tf.reduce_sum( tf.math.square(tf.math.log(y_true + 1.) - tf.math.log(y_pred + 1.)))
    return L


generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])

t = tf.range(0.0, 1200.0, 0.1, dtype=tf.float64)

Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

n_points_of_simulation = int(tf.size(t))
win4_start = 2000
win4grad = 500
n_loops = int((n_points_of_simulation - win4_start) / win4grad)

net = cbrd_tfdiffeq.Network(params_net)
y0_main = net.get_y0()

for number_of_simulation in range(100):

    solution_start = odeint(net, y0_main, t[:win4_start], method="euler")

    hf = h5py.File('/home/ivan/Data/interneurons_theta/solution_' + str(number_of_simulation) + '.hdf5', 'w')
    solution_dset = hf.create_dataset('solution', shape=(n_points_of_simulation, int(tf.size(y0_main))) )
    w_dset = hf.create_dataset('Weights', data = net.synapses[0].W.numpy())
    tau_f_dset = hf.create_dataset('tau_f', data = net.synapses[0].tau_f.numpy())
    tau_r_dset = hf.create_dataset('tau_r', data = net.synapses[0].tau_r.numpy())
    tau_d_dset = hf.create_dataset('tau_d', data = net.synapses[0].tau_d.numpy())
    Uinc_dset = hf.create_dataset('Uinc', data = net.synapses[0].Uinc.numpy())

    solution_dset[:win4_start, :] = solution_start.numpy()

    grad_over_simulation = [0] * len(net.synapses[0].trainable_variables)
    loss_over_simulation = 0

    y0 = solution_start[-1, :]
    for idx in range(n_loops):

        time_start_idx = win4_start + win4grad * idx
        time_end_idx = time_start_idx + win4grad
        t_slice = t[time_start_idx:time_end_idx]
        with tf.GradientTape(watch_accessed_variables=False) as tape:
            tape.watch(net.synapses[0].trainable_variables)

            solution = odeint_adjoint(net, y0, t_slice, method="euler")

            number_nun = tf.reduce_sum( tf.cast(tf.math.is_nan(solution), dtype=tf.int64))
            if number_nun > 0: break # !!!!!!!

            firings = tf.gather( solution, net.ro_0_indexes, axis=1)

            loss = Loss_func(Targets_spikes_rates[time_start_idx:time_end_idx, :], firings )

            grad = tape.gradient(loss, net.synapses[0].trainable_variables)

        

        y0 = solution[-1, :]
        

        for grad_idx in range(len(grad)):
            grad_over_simulation[grad_idx] = grad_over_simulation[grad_idx] + grad[grad_idx]
                
        loss_over_simulation += loss
        

    solution_dset[time_start_idx:time_end_idx, :] = solution.numpy()
    hf.close()
    AdamOptimizer.apply_gradients( zip( grad_over_simulation, net.synapses[0].trainable_variables ))
    print("Прогон № ", (number_of_simulation + 1), ", Loss = ", loss_over_simulation.numpy())

    break  #!!!!!!!!!!!










