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
        u0 = u_ + self.Uinc * (1 - u_) * Spre_normed #/ self.dt
        y0 = y_ + u0 * x_ * Spre_normed #/ self.dt
        x0 = x_ - u0 * x_ * Spre_normed #/ self.dt

        dXdt = (x0 - X) / self.dt
        dYdt = (y0 - Y) / self.dt
        dUdt = (u0 - U) / self.dt
        dy_dt = np.asarray([dXdt, dYdt, dUdt])
        return dy_dt

    def integrate(self, t, y0, SRpre):
        solution = [y0, ]
        self.dt = t[1] - t[0]
        y = y0
        for idx, ts in enumerate(t[1:]):
            dydt = self.step(t, y, SRpre[idx+1])
            y = y + self.dt * dydt
            solution.append(y)
        solution = np.stack(solution)
        return solution
####################################################################
params = {
    "W": 0.5,
    "pre_name": "ca1pyr",
    "post_name": "aac",
    "tau_f": 68.64285237,
    "tau_r": 295.4773937,
    "tau_d": 3.28320237,
    "Uinc": 0.203744416,
    "gbarS": 1.494119161,
    "Erev": 0.0,
}

synapse = Synapse(params)
y0 = np.asarray([1.0, 0.0, 0.0])
t = np.arange(0, 500, 0.1)
SRpre = np.zeros_like(t)
SRpre[1::500] = 1

solution = synapse.integrate(t, y0, SRpre)

fig, axes = plt.subplots()
axes.plot(t, solution)

plt.show()