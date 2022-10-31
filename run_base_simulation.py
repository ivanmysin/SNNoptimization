import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam, Adadelta, Adagrad
import cbrd_tfdiffeq
from code_generated_params import params_net



path4savingresults_template = '/home/ivan/Data/interneurons_theta/solution_{:03}.hdf5'
Optimizer = Adagrad(learning_rate=0.01)
t = tf.range(0.0, 1800.0, 0.1, dtype=tf.float64)
generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])
Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

net = cbrd_tfdiffeq.Network(params_net)
net.set_optimizator(Optimizer)
#net.load_trained_variables('/home/ivan/Data/interneurons_theta/solution_000.hdf5')

number_of_simulation_0 = 0
for idx in range(200):
    number_of_simulation = number_of_simulation_0 + idx + 1
    
    path = path4savingresults_template.format(number_of_simulation)
    solution, loss = net.fit(t, Targets_spikes_rates, path4saving=path, n_inter=1, win4_start = 10000, win4grad = 500)

    #net.save_simulation_data(path, solution, Targets_spikes_rates)
    print("Прогон № ", str(number_of_simulation), ", Loss = ", float(loss))





