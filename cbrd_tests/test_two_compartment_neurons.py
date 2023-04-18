import sys
sys.path.append('../')
import tensorflow as tf
import neuron_models
import matplotlib.pyplot as plt

soma_params = {
    "name": "soma_pyr",
    "neuron_class": neuron_models.Soma,
    "is_sim_rho" : True,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 3.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 0.0,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target": {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 30,  # 20.0,
        "phase": 3.14,
    },
}

dend_params = {
    "name": "dend_pyr",
    "neuron_class": neuron_models.Dendrite,
    "is_sim_rho": False,
    "Vreset": -90.0,
    "Vt": -50.0,
    "gl": 0.1,
    "El": -60.0,
    "C": 1.0,  #
    "sigma": 0.3,
    "ref_dvdt": 0.0,  # AP duration
    "refactory": 3.0,  # refactory for threshold
    "Iext": 2.5,
    "N": 400,
    "dts": 0.5,

    "channels_params": [],
    "target": {
        "R": 0.3,
        "freq": 7.0,
        "mean_spike_rate": 30,  # 20.0,
        "phase": 3.14,
    },
}
dt = 0.1
t = tf.range(0, 500, dt, dtype=tf.float64)
soma = neuron_models.Soma(soma_params, dt)
#soma = neuron_models.LIFCompartment(soma_params, dt)

dend = neuron_models.Dendrite(dend_params, dt)

end_idx = soma.set_indexes(0)
end_idx = dend.set_indexes(end_idx)

soma.add_compartment(dend, tf.constant([3.0, ], dtype=tf.float64))

dend.add_compartment(soma, tf.constant([3.0, ], dtype=tf.float64))
y0 = tf.concat( [soma.get_y0(), dend.get_y0()], axis=0)

solution = [y0, ]
y = y0
for ts in t[1:]:
    argmax_ro_H = None
    dy_dt_soma, argmax_ro_H = soma(ts, y, argmax_ro_H=argmax_ro_H)
    dy_dt_dend, _ = dend(ts, y, argmax_ro_H=argmax_ro_H)

    dy_dt = tf.concat([dy_dt_soma, dy_dt_dend], axis=0)

    y = y + dt * dy_dt
    solution.append(y)
solution = tf.stack(solution)

fig, axes = plt.subplots()
axes.set_title('Firing rate')
axes.plot(t, solution[:, 0])

fig, axes = plt.subplots()
axes.set_title('Vsoma')
axes.plot(t, solution[:, 799])

fig, axes = plt.subplots()
axes.set_title('Vdend')
axes.plot(t, solution[:, 1199])

plt.show()



