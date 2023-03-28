import numpy as np
import tensorflow as tf
import cbrd_tfdiffeq
import h5py
import pickle

savingpath_template = '/home/ivan/Data/phase_relations/theta_freqs/{omega}.hdf5'

theta_freqs = [12, ] #np.arange(4, 13, 1)

for theta_freq in theta_freqs:

    with open('/home/ivan/Data/Opt_res/LIF_params_net.pickle', 'rb') as file:
        params_net = pickle.load(file)

    for generator_params in params_net["params_generators"]:
        generator_params["freq"] = theta_freq

    t = tf.range(0.0, 1800.0, 0.1, dtype=tf.float64)
    net = cbrd_tfdiffeq.Network(params_net)
    y0 = net.get_y0()

    solution = net.run_simulation(t, y0)

    path = savingpath_template.format(omega=theta_freq)
    hf = h5py.File(path, 'w')
    solution_dset = hf.create_dataset('solution', data=solution.numpy() )
    hf.close()
    print(theta_freq, " is simulated!")