import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tfdiffeq import odeint
# from hh_neuron import simulate
exp = tf.math.exp
sqrt = tf.math.sqrt
erf = tf.math.erf

heaviside = tf.experimental.numpy.heaviside

SQRT_2 = np.sqrt(2)

class ODEFunc(tf.keras.Model):

    def __init__(self, args, **kwargs):
        super(ODEFunc, self).__init__(**kwargs)

        for key, val in args.items():
            setattr(self, key, val)

        self.V_Threshold = tf.constant(-55.0 , dtype=tf.float64)# mV
        self.sigma_V = tf.constant( 0.1 , dtype=tf.float64)

        self.prob = tf.Variable(0, dtype=tf.float64)


    def getAB(self, V, tau_m, dv_dt):

        T = (self.V_Threshold - V) / ( SQRT_2 * self.sigma_V)
        A = exp(0.0061 - 1.12*T - 0.257 * T**2 - 0.072 * T**3 - 0.117 * T**4 ) / tau_m

        dT_dt = dv_dt / ( SQRT_2 * self.sigma_V)
        B = -2 * np.sqrt( 1 / np.pi) * heaviside(dT_dt, 0) * exp(-T**2) / (1.000000001  + erf(T))
        H = A + B
        return B

    def get_gtot_and_dv_dt(self, y):
        V = y[:, 0]
        h = y[:, 1]
        n = y[:, 2]

        m = self.get_m(V)
        gNa = self.gbarNa * m ** 3 * h
        gK = self.gbarKdr * n ** 4
        gtot = gNa + gK + self.gL

        dv_dt = (gNa * (self.ENa - V) + gK * (self.EK - V) + self.gL * (self.EL - V) + self.Iext) / self.Cm

        return gtot, dv_dt



    def get_m(self, V):
        alpha_m = -0.1 * (V + 35) / (exp(-0.1 * (V + 35)) - 1)
        beta_m = 4 * exp(-(V + 60) / 18)
        m = alpha_m / (alpha_m + beta_m)
        return m



    @tf.function
    def call(self, t, y):
        phi = 5
        # y: V, h, n
        V = y[0]
        h = y[1]
        n = y[2]

        m = self.get_m(V)

        alpha_h = 0.07 * exp(-(V + 58) / 20)
        beta_h = 1 / (exp(-0.1 * (V + 28)) + 1)

        alpha_n = -0.01 * (V + 34) / (exp(-0.1 * (V + 34)) - 1)
        beta_n = 0.125 * exp(-(V + 44) / 80)

        gNa = self.gbarNa * m ** 3 * h
        gK = self.gbarKdr * n ** 4

        dv_dt = (gNa * (self.ENa - V) + gK * (self.EK - V) + self.gL * (self.EL - V) + self.Iext) / self.Cm
        dh_dt = phi * (alpha_h * (1 - h) - beta_h * h)
        dn_dt = phi * (alpha_n * (1 - n) - beta_n * n)

        #g_tot = gNa + gK + self.gL
        #tau_m = self.Cm / g_tot


        dy_dt = tf.stack([dv_dt, dh_dt, dn_dt], axis=0)

        return dy_dt

dt = 0.1
t0, t1 = 0., 55.

params = {
    "Iext": tf.Variable(0.48, dtype=tf.float64),
    "Cm" :  tf.Variable(1.0, dtype=tf.float64),
    "ENa" :  tf.Variable(55.0, dtype=tf.float64),
    "EK" : tf.Variable(-90.0,  dtype=tf.float64),
    "EL" :  tf.Variable(-65.0, dtype=tf.float64),
    "gbarNa" :   tf.Variable(35.0, dtype=tf.float64),
    "gbarKdr" : tf.Variable(9.0,  dtype=tf.float64),
    "gL" : tf.Variable(0.1, dtype=tf.float64),
}

solution_times = tf.convert_to_tensor(np.arange(0, t1, dt), dtype=tf.float64)  # np.linspace(t0, t1, 100)
y_init = tf.constant([-65.0, 0.0, 0.1], dtype=tf.float64)

#_, Vtarget, _ = simulate(Iapp=0.5, Cm=1)

lr = 1e-3
optimizer = tf.keras.optimizers.Adam(lr)
ode_fn = ODEFunc(params)
msle = tf.keras.losses.MeanSquaredLogarithmicError()
for itr in range(1):
    with tf.GradientTape() as tape:
        tape.watch(ode_fn.Iext)
        pred_y = odeint(ode_fn, y_init, solution_times)
        gtot, dv_dt = ode_fn.get_gtot_and_dv_dt(pred_y)
        tau_m = ode_fn.Cm  / gtot
        prob = ode_fn.getAB(pred_y[:, 0], tau_m, dv_dt)

        # loss = tf.keras.losses.mse( Vtarget, pred_y[:, 0] )
        # loss = msle( Vtarget+90, pred_y[:, 0]+90 )

        grad = tape.gradient(prob, ode_fn.Iext)
        print( grad.numpy() )
        # grad_vars = zip([grad, ],  [ode_fn.Iext, ])
        # optimizer.apply_gradients(grad_vars)

#print( prob.numpy() )

plt.plot(solution_times, pred_y[:, 0], label='predicted')
plt.legend()

plt.figure()
plt.plot(solution_times, prob)

plt.show()