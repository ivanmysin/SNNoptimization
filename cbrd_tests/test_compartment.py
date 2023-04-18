import sys
sys.path.append('../')
import tensorflow as tf
import neuron_models
import matplotlib.pyplot as plt
import cbrd_tfdiffeq

ca3pvbas_params = {
    "name": "ca3pvbas",
    "neuron_class":  neuron_models.LIFCompartment, # cbrd_tfdiffeq.HH_Neuron,
    "is_sim_rho": True,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 1.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],

    "target": {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 24,  # 20.0,
        "phase": 1.5707963267948966,
    },
}

dt = 0.1
neuron = neuron_models.LIFCompartment(ca3pvbas_params, dt)
#neuron = cbrd_tfdiffeq.HH_Neuron(ca3pvbas_params, dt)

y0 = neuron.get_y0()
t = tf.range(0, 1000, dt, dtype=tf.float64)
solution = [y0, ]
y = y0
for ts in t[1:]:

    dy_dt, _ = neuron(ts, y)

    y = y + dt * dy_dt
    solution.append(y)
solution = tf.stack(solution)

fig, axes = plt.subplots()
axes.set_title('Firing rate')
axes.plot(t, solution[:, 0])

plt.show()



