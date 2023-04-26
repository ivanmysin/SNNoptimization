import numpy as np
import tensorflow as tf
import cbrd_tfdiffeq

erf = tf.math.erf
bessel_i0 = tf.math.bessel_i0
sqrt = tf.math.sqrt
exp = tf.math.exp
cos = tf.math.cos
maximum = tf.math.maximum
minimum = tf.math.minimum
abs = tf.math.abs
logical_and = tf.math.logical_and
logical_not = tf.math.logical_not
argmax = tf.math.argmax

SQRT_FROM_2 = np.sqrt(2)
SQRT_FROM_2_PI = 0.7978845608028654
PI = np.pi

class Networkmcomps(cbrd_tfdiffeq.Network):
    def __init__(self, params, dt=0.1):
        super(cbrd_tfdiffeq.Network, self).__init__(name="Network", dtype=tf.float64)

        params_neurons = params["params_neurons"]

        self.synapses = []
        for param_synapse in params["params_synapses"]:
            params_synapses = self._set_connections(params_neurons, params["params_generators"], param_synapse)
            Syn = cbrd_tfdiffeq.PlasticSynapse(params_synapses, dt=dt)
            self.synapses.append(Syn)

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
            #if param_neuron["is_sim_rho"]:
            ro_0_indexes.append(start_idx)

            start_idx = end_idx
            self.neurons.append(Pop)

        self.ro_0_indexes = tf.convert_to_tensor(ro_0_indexes, dtype=tf.int32)

        self.generators = []
        generator = cbrd_tfdiffeq.VonMissesGenerators(params["params_generators"])

        self.generators.append(generator)
        self.n_mulcoms = 0

    def set_compartmets(self, ntwocomps, strength):
        self.n_mulcoms = int(ntwocomps//2)
        for neuron_idx in range(0, ntwocomps, 2):
            self.neurons[neuron_idx].add_compartment(self.neurons[neuron_idx + 1], strength[neuron_idx])
            self.neurons[neuron_idx+1].add_compartment(self.neurons[neuron_idx], strength[neuron_idx+1])


    @tf.function(input_signature=[tf.TensorSpec(shape=(), dtype=tf.float64), tf.TensorSpec(shape=(None,), dtype=tf.float64)])
    def __call__(self, t, y):
        t = tf.cast(t, dtype=tf.float64)
        dy_dt = []
        neurons_firings = tf.reshape(tf.gather(y, self.ro_0_indexes), shape=(-1,))

        all_firings = [neurons_firings, ]
        for generator in self.generators:
            artifitial_firing = generator(t)
            # firings = tf.concat(firings, artifitial_firing, axis=0)
            all_firings.append(artifitial_firing)

        firings = tf.concat(all_firings, axis=0)

        for synapse in self.synapses:
            y4syn = y[synapse.start_idx:synapse.end_idx]
            SRpre = tf.reshape(tf.gather(firings, synapse.pre_indxes), shape=(-1,))
            dsyn_dt = synapse(t, y4syn, SRpre=SRpre)
            dy_dt.append(dsyn_dt)

        argmax_rho_H = -1
        for neuron_idx, neuron in enumerate(self.neurons):
            Vpost = y[neuron.V_start_idx:neuron.V_end_idx]

            Isyn_full = tf.zeros(neuron.N, dtype=tf.float64)
            gsyn_full = tf.zeros(neuron.N, dtype=tf.float64)
            for synapse in self.synapses:
                gsyn, Isyn = synapse.get_G_Isyn(y, Vpost, neuron_idx)
                gsyn_full = gsyn_full + tf.reduce_sum(gsyn, axis=0)
                Isyn_full = Isyn_full + tf.reduce_sum(Isyn, axis=0)


            dneur_dt, argmax_rho_H_ = neuron(t, y, argmax_rho_H, gsyn=gsyn_full, Isyn=Isyn_full)  # for LIF y4neuron

            if argmax_rho_H_ !=  None:
                argmax_rho_H = argmax_rho_H_

            dy_dt.append(dneur_dt)

        dy_dt = tf.concat(dy_dt, axis=0)
        return dy_dt

    def loss_function(self, y_true, y_pred): # = mean_squared_logarithmic_error
        L = tf.reduce_sum( tf.math.square(tf.math.log(y_true + 1.) - tf.math.log(y_pred + 1.)))
        return L

    def __get_target_firing(self, targets_firings):
        optim_firing_indexes = []
        targets_firings_ = []
        for tar_fir_idx, tar_fir in enumerate(targets_firings):
            if not tar_fir is None:
                optim_firing_indexes.append(tar_fir_idx)
                targets_firings_.append(tar_fir)

        targets_firings = tf.stack(targets_firings_)
        optim_firing_indexes = tf.gather(self.ro_0_indexes, optim_firing_indexes)
        return targets_firings, optim_firing_indexes


    def __get_lfps(self, solution, optim_lfp_indexes):
        lfps = []
        for idx in optim_lfp_indexes:
            Vsoma = solution[:, self.neurons[idx].V_start_idx:self.neurons[idx].V_end_idx]
            Vdend = solution[:, self.neurons[idx+1].V_start_idx:self.neurons[idx+1].V_end_idx]
            rho = solution[:, self.neurons[idx].ro_start_idx:self.neurons[idx].ro_end_idx]
            lfp = tf.reduce_sum(rho*(Vdend-Vsoma), axis=1)
            lfps.append(lfp)
        lfps = tf.stack(lfps)
        return lfps
    
    def __get_targets_lfps(self, targets_lfp):
        targets_lfps_ = []
        optim_lfp_indexes = []

        for idx, tar_lfp in zip(range(0, 2*self.n_mulcoms, 2), targets_lfp):
            if tar_lfp is None: continue
            targets_lfps_.append(tar_lfp)
            optim_lfp_indexes.append(idx)
        targets_lfps = tf.stack(targets_lfps_)
        optim_lfp_indexes = tf.constant(optim_lfp_indexes, dtype=tf.int32)
        return targets_lfps, optim_lfp_indexes
    
    
    def fit(self, t, targets_firings, targets_lfp, n_inter=50, path4saving=None, win4_start=2000, win4grad=500):
        n_points_of_simulation = int(tf.size(t))
        n_loops = int((n_points_of_simulation - win4_start) / win4grad)

        targets_firings, optim_firing_indexes = self.__get_target_firing(targets_firings)
        targets_lfps, optim_lfp_indexes = self.__get_targets_lfps(targets_lfp)

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
            trainable_variables = trainable_variables + self.synapses[0].trainable_variables  # (self.synapses[0].gbarS, ) # !!!!!!!!!!!!!!!!!!

            # trainable_variables = self.synapses[0].trainable_variables
            grad_over_simulation = [0] * len(trainable_variables)

            # print(n_loops)
            #targets_firings = generators4targets(tf.reshape(t[time_start_idx:time_end_idx], shape=(-1, 1)))
            #targets_firings_list = [targets_firings, ]

            for idx in range(n_loops):

                time_start_idx = win4_start + win4grad * idx - 1
                time_end_idx = time_start_idx + win4grad + 1
                t_slice = t[time_start_idx: time_end_idx]


                #generators4targets(tf.reshape(t_slice, shape=(-1, 1)))
                #targets_firings_list.append(targets_firings[1:])

                with tf.GradientTape(watch_accessed_variables=False) as tape:

                    tape.watch(trainable_variables)

                    solution = cbrd_tfdiffeq.odeint_adjoint(self, y0, t_slice, method="euler")

                    solutions_full.append(solution[1:])

                    number_nun = tf.reduce_sum(tf.cast(tf.math.is_nan(solution), dtype=tf.int32))
                    if number_nun > 0:
                        print("Nans values in results!!!!")
                        break

                    #firings = tf.gather(solution, self.ro_0_indexes, axis=1)
                    firings = tf.gather(solution, optim_firing_indexes, axis=1)
                    #lfps = self.__get_lfps(solution, optim_lfp_indexes)

                    clear_loss = self.loss_function( tf.transpose(targets_firings[:, time_start_idx: time_end_idx]), firings )

                    #clear_loss = clear_loss +  tf.reduce_sum((lfps - targets_lfps[:, time_start_idx: time_end_idx])**2)


                    clear_loss_over_simulation += clear_loss


                    loss = clear_loss
                    for val in self.synapses[0].trainable_variables:
                        # loss += tf.reduce_sum(10e6 * tf.nn.relu(0.005 - val))
                        loss += tf.reduce_sum(-0.001 * tf.math.log(100 * val))

                    loss += tf.reduce_sum(-0.001 * tf.math.log(100 * (1.0 - self.synapses[0].Uinc)))
                    # loss += tf.reduce_sum(-0.001 * tf.math.log(100 * (1.0 - self.synapses[0].W) ))

                    # for neuron in self.neurons:
                    #     loss += tf.reduce_sum(-0.1 * tf.math.log(1.5 - neuron.Iext))

                    grad = tape.gradient(loss, trainable_variables)

                y0 = solution[-1, :]

                for grad_idx in range(len(grad)):
                    grad_over_simulation[grad_idx] = grad_over_simulation[grad_idx] + grad[grad_idx]
                loss_over_simulation += loss

            if not (path4saving is None):
                self.save_simulation_data(path4saving, tf.concat(solutions_full, axis=0), targets_firings)

            self.optimizer.apply_gradients(zip(grad_over_simulation, trainable_variables))

        return tf.concat(solutions_full, axis=0), clear_loss_over_simulation, loss_over_simulation
