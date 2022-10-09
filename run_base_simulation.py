import numpy as np
import tensorflow as tf
from tensorflow.keras.metrics import mean_squared_logarithmic_error
from tensorflow.keras.optimizers import Adam
from tfdiffeq import odeint, odeint_adjoint
import cbrd_tfdiffeq
import h5py

from code_generated_params import params_net

AdamOptimizer = Adam(learning_rate=0.01)

Loss_func = mean_squared_logarithmic_error



generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])

t = tf.range(0.0, 1200.0, 0.1, dtype=tf.float64)

Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

n_points_of_simulation = int(tf.size(t))
win4_start = 2000
win4grad = 500
n_loops = int((n_points_of_simulation - win4_start) / win4grad)

V = tf.zeros(400, dtype=tf.float64) - 90
ro = tf.zeros(400, dtype=tf.float64)
ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[399, ]], [1 / 0.5, ]))

simul_y0 = []

# y0syn = tf.Variable([1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], dtype=tf.float64)
X0 = tf.ones(len(params_net["params_synapses"]), dtype=tf.float64)
R0_U0 = tf.zeros(2 * len(params_net["params_synapses"]), dtype=tf.float64)
simul_y0.append(X0)
simul_y0.append(R0_U0)

for _ in range(len(params_net["params_neurons"])):
    simul_y0.append(ro)
    simul_y0.append(V)

y0_main = tf.cast(tf.concat(simul_y0, axis=0), dtype=tf.float64)

net = cbrd_tfdiffeq.Network(params_net)

for number_of_simulation in range(100):

    solution_start = odeint(net, y0_main, t[:win4_start], method="euler")

    hf = h5py.File('/home/ivan/Data/interneurons_theta/solution_' + str(number_of_simulation) + '.hdf5', 'w')
    solution_dset = hf.create_dataset('solution', shape=(n_points_of_simulation, int(tf.size(y0))) )
    w_dset = hf.create_dataset('Weights', data = net.synapses[0].W.numpy())
    tau_f_dset = hf.create_dataset('tau_f', data = net.synapses[0].tau_f.numpy())
    tau_r_dset = hf.create_dataset('tau_r', data = net.synapses[0].tau_r.numpy())
    tau_d_dset = hf.create_dataset('tau_d', data = net.synapses[0].tau_d.numpy())
    Uinc_dset = hf.create_dataset('Uinc', data = net.synapses[0].Uinc.numpy())

    solution_dset[:win4_start, :] = solution_start.numpy()

    grad_over_simulation = 0
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

            loss_over_simulation += loss


        y0 = solution[-1, :]
        grad_over_simulation = grad_over_simulation + grad

    solution_dset[time_start_idx:time_end_idx, :] = solution.numpy()
    hf.close()
    AdamOptimizer.apply_gradients( zip( [grad_over_simulation, ], [net.synapses[0].trainable_variables, ] ))
    print("Прогон модели № ", (number_of_simulation + 1), ", Loss = ", loss_over_simulation)
#print(grad_over_simulation)









