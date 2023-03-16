import numpy as np
import matplotlib.pyplot as plt

exp = np.exp

class Synapse:
    def __init__(self, params):
        for key, val in params.items():
            setattr(self, key, val)

        if self.tau_d != self.tau_r:
            self.tau1r = self.tau_d / (self.tau_d - self.tau_r)
        else:
            self.tau1r = 1e-13

    def step(self, t, y, SRpre=0):
        Spre_normed = SRpre * self.W

        X = y[0]
        Y = y[1]
        U = y[2]

        y_ = Y * exp(-self.dt / self.tau_d)

        x_ = 1 + (X - 1 + self.tau1r * Y) * exp(-self.dt / self.tau_r) - self.tau1r * Y

        u_ = U * exp(-self.dt / self.tau_f)
        u0 = u_ + self.Uinc * (1 - u_) * Spre_normed
        y0 = y_ + u0 * x_ * Spre_normed
        x0 = x_ - u0 * x_ * Spre_normed

        dXdt = (x0 - X) / self.dt
        dYdt = (y0 - Y) / self.dt
        dUdt = (u0 - U) / self.dt
        dy_dt = tf.concat([dXdt, dYdt, dUdt], axis=0)

    return dy_dt

