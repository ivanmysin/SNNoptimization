import numpy as np
import tensorflow as tf
from tensorflow.keras.optimizers import Adam
import cbrd_tfdiffeq
import synapse_models as SM
from non_plastic_params import params_net
import h5py
from time import time


class Network_non_plastic(cbrd_tfdiffeq.Network):
    def __init__(self, params, dt=0.1):
        super(cbrd_tfdiffeq.Network, self).__init__(name="Network", dtype=tf.float64)

        params_neurons = params["params_neurons"]

        self.synapses = []
        params_synapses = self._set_connections(params_neurons, params["params_generators"], params["params_synapses"])
        Syn = SM.TwoExpSynapse(params_synapses, dt=dt)
        self.synapses.append(Syn)
        # for idx, param_synapse in enumerate(params_synapses):
        #     Syn = PlasticSynapse(param_synapse)
        #     Syn.start_idx = idx * 3 # 3 - число динамических переменных для синапса
        #     Syn.end_idx = Syn.start_idx + 3
        #     self.synapses.append(Syn)

        start_idx4_neurons = self.synapses[-1].end_idx
        self.neurons = []

        ro_0_indexes = []
        start_idx = start_idx4_neurons
        for idx, param_neuron in enumerate(params_neurons):
            Pop = param_neuron["neuron_class"](param_neuron, dt=dt)
            end_idx = Pop.set_indexes(start_idx)
            # start_idx = start_idx4_neurons + idx * Pop.n_dynamic_vars * Pop.N
            # Pop.start_idx = start_idx
            # Pop.end_idx = start_idx + Pop.n_dynamic_vars * Pop.N
            ro_0_indexes.append(start_idx)
            start_idx = end_idx
            self.neurons.append(Pop)

        self.ro_0_indexes = tf.convert_to_tensor(ro_0_indexes, dtype=tf.int32)

        self.generators = []
        generator = cbrd_tfdiffeq.VonMissesGenerators(params["params_generators"])

        self.generators.append(generator)

    def fit(self, t, generators4targets, n_inter=50, path4saving=None, win4_start=2000, win4grad=500):
        n_points_of_simulation = int(tf.size(t))
        n_loops = int((n_points_of_simulation - win4_start) / win4grad)

        y0_main = self.get_y0()
        for number_of_simulation in range(n_inter):
            solutions_full = []

            time_start_idx = 0
            time_end_idx = win4_start

            solution = cbrd_tfdiffeq.odeint(self, y0_main, t[time_start_idx:time_end_idx], method="euler")
            solutions_full.append(solution)

            loss_over_simulation = 0.0
            clear_loss_over_simulation = 0.0

            y0 = solution[-1, :]

            trainable_variables = tuple(neuron.Iext for neuron in self.neurons)
            trainable_variables = trainable_variables + self.synapses[
                0].trainable_variables  # (self.synapses[0].gbarS, ) # !!!!!!!!!!!!!!!!!!

            # trainable_variables = self.synapses[0].trainable_variables
            grad_over_simulation = [0] * len(trainable_variables)

            # print(n_loops)
            targets_firings = generators4targets(tf.reshape(t[time_start_idx:time_end_idx], shape=(-1, 1)))
            targets_firings_list = [targets_firings, ]

            for idx in range(n_loops):

                time_start_idx = win4_start + win4grad * idx - 1
                time_end_idx = time_start_idx + win4grad + 1
                t_slice = t[time_start_idx: time_end_idx]

                targets_firings = generators4targets(tf.reshape(t_slice, shape=(-1, 1)))
                targets_firings_list.append(targets_firings[1:])

                with tf.GradientTape(watch_accessed_variables=False) as tape:

                    tape.watch(trainable_variables)

                    solution = cbrd_tfdiffeq.odeint_adjoint(self, y0, t_slice, method="euler")

                    solutions_full.append(solution[1:])

                    number_nun = tf.reduce_sum(tf.cast(tf.math.is_nan(solution), dtype=tf.int32))
                    if number_nun > 0:
                        print("Nans values in results!!!!")
                        break

                    firings = tf.gather(solution, self.ro_0_indexes, axis=1)

                    clear_loss = self.loss_function(targets_firings, firings)
                    clear_loss_over_simulation += clear_loss
                    loss = clear_loss
                    for val in self.synapses[0].trainable_variables:
                        loss += tf.reduce_sum(-0.001 * tf.math.log(100 * val))

                    grad = tape.gradient(loss, trainable_variables)

                y0 = solution[-1, :]

                for grad_idx in range(len(grad)):
                    grad_over_simulation[grad_idx] = grad_over_simulation[grad_idx] + grad[grad_idx]
                loss_over_simulation += loss

            if not (path4saving is None):
                self.save_simulation_data(path4saving, tf.concat(solutions_full, axis=0),
                                          tf.concat(targets_firings_list, axis=0))

            self.optimizer.apply_gradients(zip(grad_over_simulation, trainable_variables))

        return tf.concat(solutions_full, axis=0), clear_loss_over_simulation, loss_over_simulation

# optimized_results = '/media/LD/Data/SSN_simulated/solution_500.hdf5'
#
# with h5py.File(optimized_results, "r") as h5file:
#     sol_dset = h5file["solution"]
#     for neuron_params in params_net["params_neurons"]:
#         iext_attr_name = neuron_params["name"] + "_Iext"
#         neuron_params["Iext"] = sol_dset.attrs[iext_attr_name]
#
#     w_coeff = 1
#     for syn_idx, synapse_params in enumerate(params_net["params_synapses"]):
#         if synapse_params["pre_name"] in ["ca3pyr", "ca1pyr"]:
#             w_coeff = 10
#         if synapse_params["pre_name"] in ["ec3", ]:
#             w_coeff = 3.33
#
#         gbarS = h5file["SynapticConductance:0"][syn_idx]
#         synapse_params["w"] = w_coeff * h5file["Wplasticsyns:0"][syn_idx]
#
#         synapse_params["tau_f"] = h5file["tau_f:0"][syn_idx]
#         synapse_params["tau_r"] = h5file["tau_r:0"][syn_idx]
#         synapse_params["tau_d"] = h5file["tau_d:0"][syn_idx]
#         synapse_params["Uinc"] = h5file["Uinc:0"][syn_idx]
#         synapse_params["gbarS"] = gbarS
#         w_coeff = 1

for syn_idx, synapse_params in enumerate(params_net["params_synapses"]):
    if synapse_params["pre_name"] in ["ca3pyr", "ca1pyr"]:
        synapse_params['pconn'] = 5
        synapse_params['gbarS'] *= 10
    if synapse_params["pre_name"] in ["ec3", ]:
        synapse_params['pconn'] = 2.5
        synapse_params['gbarS'] *= 10


path4savingresults_template = '/media/LD/Data/SSN_simulated/LIF_nonplastic_synapses/solution_{:03}.hdf5'
#path4savingresults_template = '/home/ivan/Data/interneurons_theta/non_plastic/solution_{:03}.hdf5'

Optimizer = Adam(learning_rate=0.001)  # Adagrad #Adadelta
t = tf.range(0.0, 1800.0, 0.1, dtype=tf.float64)
generators4targets = cbrd_tfdiffeq.VonMissesGenerators(params_net["params_neurons"])
Targets_spikes_rates = generators4targets(tf.reshape(t, shape=(-1, 1)))

net = Network_non_plastic(params_net)
net.set_optimizator(Optimizer)

number_of_simulation_0 = 0
for idx in range(1000):
    timer = time()
    number_of_simulation = number_of_simulation_0 + idx + 1

    path = path4savingresults_template.format(number_of_simulation)
    solution, clearloss, fullloss = net.fit(t, generators4targets, path4saving=path, n_inter=1, win4_start=10000,
                                            win4grad=500)

    net.save_simulation_data(path, solution, Targets_spikes_rates)
    print("Прогон № ", str(number_of_simulation), ", Clear Loss = ", float(clearloss), ", Full Loss = ",
          float(fullloss), ", time = ", str((time() - timer) / 60), " mins")



