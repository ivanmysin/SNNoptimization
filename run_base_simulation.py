import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tfdiffeq import odeint, odeint_adjoint
import cbrd_tfdiffeq
import h5py

# from net_parameters import params_net
from code_generated_params import params_net

def Loss_func(y_true, y_pred): # = mean_squared_logarithmic_error
    L = tf.reduce_sum( tf.math.square(tf.math.log(y_true + 1.) - tf.math.log(y_pred + 1.)))
    return L
##########################################################################

path4savingresults_template = '/home/ivan/Data/interneurons_theta/solution_{:s}.hdf5'
AdamOptimizer = Adam(learning_rate=0.05)
t = tf.range(0.0, 1200.0, 0.1, dtype=tf.float64)
generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])
Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

n_points_of_simulation = int(tf.size(t))
win4_start = 2000
win4grad = 500
n_loops = int((n_points_of_simulation - win4_start) / win4grad)

net = cbrd_tfdiffeq.Network(params_net)
y0_main = net.get_y0()

for number_of_simulation in range(100):
    solutions_full = []

    time_start_idx = 0
    time_end_idx = win4_start
    solution = odeint(net, y0_main, t[time_start_idx:time_end_idx], method="euler")
    solutions_full.append(solution)

    grad_over_simulation = [0] * len(net.synapses[0].trainable_variables)
    loss_over_simulation = 0

    y0 = solution[-1, :]
    for idx in range(n_loops):

        time_start_idx = win4grad + win4grad * idx
        time_end_idx = time_start_idx + win4grad
        t_slice = t[time_start_idx:time_end_idx]
        with tf.GradientTape(watch_accessed_variables=False) as tape:

            tape.watch(net.synapses[0].trainable_variables)

            solution = odeint_adjoint(net, y0, t_slice, method="euler")
            solutions_full.append(solution)

            number_nun = tf.reduce_sum( tf.cast(tf.math.is_nan(solution), dtype=tf.int64))
            if number_nun > 0:
                print("Nans values in results!!!!")
                break

            firings = tf.gather( solution, net.ro_0_indexes, axis=1)

            loss = Loss_func(Targets_spikes_rates[time_start_idx:time_end_idx, :], firings )

            grad = tape.gradient(loss, net.synapses[0].trainable_variables)

        path = path4savingresults_template.format(str(number_of_simulation + 1))
        net.save_simulation_data(path, tf.concat(solutions_full, axis=1), Targets_spikes_rates)


        y0 = solution[-1, :]
        

        for grad_idx in range(len(grad)):
            grad_over_simulation[grad_idx] = grad_over_simulation[grad_idx] + grad[grad_idx]
        loss_over_simulation += loss
        



    AdamOptimizer.apply_gradients( zip( grad_over_simulation, net.synapses[0].trainable_variables ))
    print("Прогон № ", (number_of_simulation + 1), ", Loss = ", float(loss_over_simulation) )












