import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp
import matplotlib.pyplot as plt
import time

from scipy.integrate import solve_ivp

exp = tf.math.exp # np.exp #

# @tf.function
def ode_fn(t, y, Iapp, Cm, ENa, EK, EL, gbarNa, gbarKdr, gL):
    phi = 5
    # y: V, h, n
    V = y[0]
    h = y[1]
    n = y[2]

    alpha_m = -0.1*(V + 35) / ( exp(-0.1*(V + 35)) - 1 )
    beta_m = 4 * exp(-(V + 60) / 18 )
    m = alpha_m / (alpha_m + beta_m)

    alpha_h = 0.07 * exp( -(V + 58)/20  )
    beta_h = 1 / ( exp(-0.1*(V + 28)) + 1 )

    alpha_n = -0.01*(V + 34)/( exp(-0.1*(V + 34)) - 1 )
    beta_n = 0.125 * exp(-(V + 44) / 80)

    gNa = gbarNa * m**3 * h
    gK = gbarKdr * n**4


    dv_dt =  (gNa * (ENa - V) + gK*(EK - V) + gL *(EL - V) + Iapp ) / Cm
    dh_dt = phi * (alpha_h*(1 - h) - beta_h*h)
    dn_dt = phi * (alpha_n*(1 - n) - beta_n*n)

    dy_dt = tf.stack([dv_dt, dh_dt, dn_dt], axis=0 )
    #dy_dt = [dv_dt, dh_dt, dn_dt]

    return dy_dt
###################################################################################
t0 = 0
duartion = 200
dt = 0.1

solution_times = np.arange(t0, duartion, dt)
y_init = tf.constant([-60.0, 0.5, 0.0], dtype=tf.float64)

constants = {
    "Iapp": tf.constant(0.5, dtype=tf.float64),
    "Cm" :  tf.constant(1.0, dtype=tf.float64),
    "ENa" :  tf.constant(50.0, dtype=tf.float64),
    "EK" : tf.constant(-90.0,  dtype=tf.float64),
    "EL" :  tf.constant(-65.0, dtype=tf.float64),
    "gbarNa" :   tf.constant(35.0, dtype=tf.float64),
    "gbarKdr" : tf.constant(9.0,  dtype=tf.float64),
    "gL" : tf.constant(0.1, dtype=tf.float64),
}

solver = tfp.math.ode.DormandPrince()  # rtol=0.001, atol=1e-03, first_step_size=0.1, safety_factor=0.9
results = solver.solve(ode_fn, t0, y_init, solution_times=solution_times, constants=constants)

plt.plot(solution_times, results.states[:, 0])
plt.show()

# for key, val in constants.items():
#     constants[key] = val.numpy()
# args = (constants["Iapp"], constants["Cm"], constants["ENa"], constants["EK"], constants["EL"], constants["gbarNa"], constants["gbarKdr"], constants["gL"]  )
#
#
# res = solve_ivp(ode_fn, [0, duartion], y_init.numpy(), t_eval=solution_times, args=args)
#
#
# plt.plot(res["t"], res["y"][0, :])
# plt.show()