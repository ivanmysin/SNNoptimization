import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
exp = tf.math.exp
cos = tf.math.cos
abs = tf.math.abs
sqrt = tf.math.sqrt

t = tf.linspace(0, 2, 2000)
dt = t[1] - t[0]
omega_theta = 5.0
omega_gamma_s = 40.0
peak_gamma_on_theta_phase = tf.Variable(0.5*np.pi, dtype=tf.float64)




with tf.GradientTape() as tape:
    theta_phi = 2 * np.pi * t * omega_theta
    fs = 1 / dt
    tape.watch(peak_gamma_on_theta_phase)
    gamma_s_envelope = 0.1 * exp(1.0 * cos(theta_phi - peak_gamma_on_theta_phase) )
    gamma_s =  gamma_s_envelope * cos( 2*np.pi*t*omega_gamma_s)
    #gamma_m = 0.01 * exp(2 * cos(theta_phi) ) * cos( 2*np.pi*t*90)
    #######################################################
    omega0 = 6.0
    s = omega0 / (2*np.pi*omega_gamma_s)
    t_morlet =  tf.range(-2.5, 2.5, dt, dtype=tf.float64)
    #print(tf.size(t_morlet))
    #t_morlet =  tf.linspace(-0.5, 0.5, 200)

    morlet = (np.pi**(-0.25)) * exp( tf.complex(-0.5*(t_morlet/s)**2, omega0*t_morlet/s) )

    #######################################################
    lfp = cos(theta_phi) + gamma_s #+ gamma_m

    data   = tf.reshape(lfp, [1, int(lfp.shape[0]), 1], name='lfp')
    kernel = tf.reshape(morlet, [int(morlet.shape[0]), 1, 1], name='morlet')

    wavelet_spetum_real = tf.squeeze( tf.nn.conv1d(data, tf.math.real(kernel), stride=1, padding='SAME') ) / sqrt(tf.cast(s, tf.float64))
    wavelet_spetum_imag = tf.squeeze( tf.nn.conv1d(data, tf.math.imag(kernel), stride=1, padding='SAME') ) / sqrt(tf.cast(s, tf.float64))

    wavelet_spetum = 0.008*sqrt(wavelet_spetum_real**2 + wavelet_spetum_imag**2)

    L = tf.math.reduce_sum( tf.math.square(peak_gamma_on_theta_phase - gamma_s_envelope) )
    dLdp = tape.gradient(L, peak_gamma_on_theta_phase)
    print(dLdp)


plt.plot(t, wavelet_spetum)
plt.plot(t, gamma_s_envelope)
#plt.plot(t_morlet, morlet)

plt.show()