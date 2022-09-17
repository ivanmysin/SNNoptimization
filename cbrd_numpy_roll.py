import numpy as np
from scipy.special import erf

SQRT_FROM_2 = np.sqrt(2)
SQRT_FROM_2_PI = np.sqrt(2 / np.pi)

# base neuron class for CBRD or Monte-Carlo
class BaseNeuron:

    def __init__(self, params):

        self.Vreset = params["Vreset"]
        self.Vt = params["Vt"]

        self.gl = params["gl"]
        self.El = params["El"]
        self.C = params["C"]
        self.sigma = params["sigma"]

        self.ref_dvdt = params["ref_dvdt"]   # refactory in updates of V and variables of states
        self.refactory = params["refactory"] # refactory for threshold

        self.w_in_distr = params["w_in_distr"] # weight of neuron in model
        self.Iext = params["Iext"]
        self.Isyn = 0
        self.gsyn = 0
        self.is_use_CBRD = params["use_CBRD"] # flag use CBRD or Monte-Carlo

        self.N = params["N"]

        self.V = np.zeros(self.N)
        self.dts = params["dts"]

        if self.is_use_CBRD:

            self.t_states = np.linspace(0, self.N * self.dts, self.N)
            self.ro = np.zeros_like(self.t_states)
            self.ro[-1] = 1 / self.dts
            self.ro_H_integral = 0
            self.ts = 0



            self.ref_idx = int(self.refactory / self.dts)
            self.ref_dvdt_idx = int(self.ref_dvdt / self.dts)

            self.max_roH_idx = 0

        else:
            self.ts = np.zeros_like(self.V) + 200

        self.firing = [0]
        self.CVhist = [0]
        self.saveCV = True



    def H_function(self, V, dVdt, tau_m, Vt, sigma):
        T = (Vt - V) / sigma / SQRT_FROM_2
        A = np.exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
        dT_dt = -1.0 / sigma / SQRT_FROM_2 * dVdt
        dT_dt[dT_dt > 0] = 0
        F_T = SQRT_FROM_2_PI * np.exp(-T**2) / (1.000000001 + erf(T))
        B = -SQRT_FROM_2 * dT_dt * F_T * tau_m
        H = (A + B) / tau_m
        return H


    def update_ro(self, dt, dVdt, tau_m):
        shift = False

        if self.ts >= self.dts:
            self.ro[-1] += self.ro[-2]
            self.ro[:-1] = np.roll(self.ro[:-1], 1)
            self.ro[0] = self.ro_H_integral
            self.ro_H_integral = 0
            self.ts = 0
            shift = True

            # self.ro /= np.sum(self.ro) * self.dts
            # print (np.sum(self.ro) * self.dts)


        H = self.H_function(self.V, dVdt, tau_m, self.Vt, self.sigma)

        H[:self.ref_idx] = 0
        dro = self.ro * (1 - np.exp(-H * dt))  # dt * self.ro * H  #
        self.max_roH_idx = np.argmax(dro)
        self.ro -= dro

        # self.ro[self.ro < 0] = 0
        self.ro_H_integral += np.sum(dro)
        self.ts += dt

        return shift


    def add_Isyn(self, Isyn, gsyn):
        self.Isyn += Isyn
        self.gsyn += gsyn

    def update(self, dt):
        return 0, 0, 0, 0


    def get_flow(self):
        return self.w_in_distr * self.firing[-1]

    def get_flow_hist(self):
        return self.w_in_distr * np.asarray(self.firing)

    def get_CV(self):
        return self.w_in_distr * np.asarray(self.CVhist)

    def getV(self):
        return self.V

    def get_weights(self):

        if self.is_use_CBRD:
            weights = self.w_in_distr * self.ro * self.dts
        else:
            weights = self.w_in_distr * np.ones_like(self.V) / self.V.size

        return weights


##################################################################

class LIF_Neuron(BaseNeuron):
    artifitial_generator = False

    def __init__(self, params):

        super(LIF_Neuron, self).__init__(params)

        self.V += self.Vreset

        self.Vhist = [self.V[-1]]

        self.times = [0]

        if self.is_use_CBRD:
            self.sigma = self.sigma / self.gl * np.sqrt(0.5 * self.gl / self.C)


    def update(self, dt, duration=None):

        if (duration is None):
            duration = dt

        t = 0
        while (t < duration):

            # dVdt = -self.V / self.tau_m + self.Iext / self.tau_m + self.Isyn
            dVdt = (self.gl * (self.El - self.V) + self.Iext + self.Isyn) / self.C

            tau_m = self.C / (self.gl + self.gsyn)

            if self.is_use_CBRD:
                dVdt[:self.ref_dvdt_idx ] = 0
            else:
                dVdt += np.random.normal(0, self.sigma, self.V.size)  / self.C / np.sqrt(dt)
                dVdt[self.ts < self.ref_dvdt] = 0


            self.V += dt * dVdt

            # print(self.V[-1])

            self.Vhist.append(self.V[-1])

            self.Isyn = 0
            self.gsyn = 0

            if self.is_use_CBRD:
                shift = self.update_ro(dt, dVdt, tau_m)
                self.firing.append(1000 * self.ro[0])
                if shift:
                    self.V[:-1] = np.roll(self.V[:-1], 1)
                    self.V[0] = self.Vreset

            else:
                spiking = self.V >= self.Vt
                self.V[spiking] = self.Vreset
                self.firing.append(1000 * np.mean(spiking) / dt)
                self.ts += dt
                self.ts[spiking] = 0


            self.times.append(self.times[-1] + dt)

            t += dt

        if self.is_use_CBRD:
            return self.t_states, self.w_in_distr * self.ro, self.times, self.w_in_distr * np.asarray(
                self.firing),[]  # , self.t_states, self.V
        else:
            return np.zeros(400), np.zeros(400), self.times, self.w_in_distr * np.asarray(self.firing), []

    def get_Vdistrib(self):
        if self.is_use_CBRD:
            weights = self.ro * self.dts
            y, x = np.histogram(self.V, bins=100, weights=weights, range=[self.Vreset - 1, -45], density=True) # range=[self.Vreset - 5, self.Vt + 1]
        else:
            y, x = np.histogram(self.V, bins=100, range=[self.Vreset-1, -45], density=True)

        return y*self.w_in_distr, x

#########################################################################################

##################################################################
class Channel:
    def __init__(self, gmax, E, V, x=None, y=None, x_reset=None, y_reset=None):
        self.gmax = gmax
        self.E = E
        self.g = 0
        if not x is None:
            self.x = self.get_x_inf(V)
            self.x_reset = x_reset
        else:
            self.x = None

        if not y is None:
            self.y = self.get_y_inf(V)
            self.y_reset = y_reset
        else:
            self.y = None

    def update(self, dt, V, mask=slice(0, None)):
        self.g = self.gmax
        V = V[mask]
        if not (self.x is None):
            x_inf = self.get_x_inf(V)
            tau_x = self.get_tau_x(V)
            self.x[mask] = x_inf - (x_inf - self.x[mask]) * np.exp(-dt / tau_x)
            self.g *= self.x

        if not (self.y is None):
            y = self.y[mask]
            y_inf = self.get_y_inf(V)
            tau_y = self.get_tau_y(V)
            self.y[mask] = y_inf - (y_inf - self.y[mask]) * np.exp(-dt / tau_y)
            self.g *= self.y


    def get_I(self, V):
        I = self.g * (V - self.E)
        return I

    def get_g(self):
        return self.g

    def reset(self, spiking):
        if not (self.x is None):
            self.x[spiking] = self.x_reset

        if not (self.y is None):
            self.y[spiking] = self.y_reset

    def get_x_inf(self, V):
        return 0

    def get_y_inf(self, V):
        return 0

    def get_tau_x(self, V):
        return 0

    def get_tau_y(self, V):
        return 0

    def roll(self, max_roH_idx):
        if not (self.x is None):
            tmpx = self.x[max_roH_idx]
            self.x[:-1] = np.roll(self.x[:-1], 1)
            self.x[0] = tmpx

        if not (self.y is None):
            tmpy = self.y[max_roH_idx]
            self.y[:-1] = np.roll(self.y[:-1], 1)
            self.y[0] = tmpy
###################################################
duration = 500
dt = 0.1
params = {
    "Vreset" : -80.0,
    "Vt" : -50.0,
    "gl" : 0.01,
    "El" : -70.0,
    "C"  : 0.2,
    "sigma" : 0.3,
    "ref_dvdt" : 0,
    "refactory" :  3.0, # refactory for threshold
    "w_in_distr" : 1.0,  # weight of neuron in model
    "Iext" : 0.3,

    "use_CBRD" : True,
    "N" : 200,
    "dts" : 0.5
}


neuron_pops = LIF_Neuron(params)
t_states, ro, times, firing, _ = neuron_pops.update(dt, duration)

import matplotlib.pyplot as plt

plt.scatter(times, firing)
plt.show()













