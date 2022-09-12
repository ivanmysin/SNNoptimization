import numpy as np
from scipy.special import erf
import matplotlib.pyplot as plt


def update_z(z, dt, dts, Sourse):
    dz = np.zeros_like(z)

    S = Sourse

    diff_z = np.diff(z)
    a = diff_z[1:]
    b = diff_z[:-1]

    wi = limiter(a, b)

    a_ = b[1:]
    b_ = b[:-1]
    wi_1 = limiter(a_, b_)
    wi_1 = np.append(0, wi_1)

    dz[1:-1] = -dt/dts * ( diff_z[:-1] + dt / dts * (wi - wi_1)) - dt * S[1:-1] # * z[1:-1]


    dz[0] = -dt/dts * z[0] - dt * S[0]
    dz[-1] = dt/dts * (z[-2] + dt/dts * wi[-1]) - dt * S[-1] # * z[-1]

    return dz

def limiter(a, b):
    w = np.zeros_like(a)

    selected_indx1 = ( (a * b) <= 0 )

    selected_indx2 = (a < 0) & (a * b > 0)

    x1 = np.abs(a[selected_indx2] + b[selected_indx2]) * 0.5
    x2 = 2 * np.minimum(np.abs(a[selected_indx2]), np.abs(b[selected_indx2]))
    w[selected_indx2] = -np.minimum(x1, x2)

    selected_indx3 = np.logical_not(selected_indx1 & selected_indx2)

    x1 = np.abs(a[selected_indx3] + b[selected_indx3]) * 0.5
    x2 = 2 * np.minimum(np.abs(a[selected_indx3]), np.abs(b[selected_indx3]))

    w[selected_indx3] = np.minimum(x1, x2)
    return w

def H_function(V, dV_dt, Vt, dt, tau_m, sigma):
    #print(dV_dt[-1], V[-1], Vt) # 0.6 9.0 10

    k = tau_m / dt
    g_tot = 1 / tau_m # (Cm = 1) !!!!

    T = np.sqrt(0.5*(1+k)) * g_tot * (Vt - V) / sigma

    A_inf = np.exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
    A = A_inf * (1 - (1 + k)**(-0.71 + 0.0825 * (T + 3) ) )

    dT_dt = -g_tot/sigma * np.sqrt(0.5+0.5*k) * dV_dt

    dT_dt[dT_dt < 0] = 0

    F_T = np.sqrt(2/np.pi) * np.exp(-T**2) / (1 + erf(T))

    B = -np.sqrt(2) * tau_m * dT_dt * F_T

    H = A + B

    return H
#########################################################################################################
def simulate_monte_carlo(Iext, Vt, dt, tau_m, sigma, Vr, nsteps):
    print(Iext, Vt, dt, tau_m, sigma, Vr, nsteps)
    V = np.zeros(5000, dtype=np.float64) + Vr
    spike_rate = []

    sigma_V = sigma / np.sqrt(dt) / tau_m

    for _ in range(nsteps):

        # self.V += dt * (-self.V + self.muext + self.Isyn + self.sigmaext**2 * np.random.randn(self.N) ) / self.tau
        dV_dt = (-V + Iext) / tau_m + np.random.normal(0, sigma_V, V.size)

        V += dt * dV_dt
        fired = V > Vt
        V[fired] = Vr
        firing = np.mean(fired)
        spike_rate.append(firing)

    return spike_rate

def cbrd(Iext, Vt, dt, tau_m, sigma, Vr, nsteps, dts):
    Pts = np.zeros(400, dtype=np.float64)
    Pts[-1] = 1
    V = np.zeros_like(Pts) + Vr

    spike_rate = []
    V_hist = []

    for _ in range(nsteps):
        dV_dt = (-V + Iext) / tau_m

        H = H_function(V, dV_dt, Vt, dt, tau_m, sigma)
        # print(H)

        sourse4Pts = Pts * H

        sourse4Pts[0] = -np.sum(sourse4Pts)
        dPts = update_z(Pts, dt, dts, sourse4Pts)
        dV = update_z(V, dt, dts, -dV_dt)

        # print(dPts)
        spike_rate.append(-sourse4Pts[0])  # sourse4Pts[0]
        V_hist.append(V[-1])

        dV[0] = 0
        dV[-1] = dt * dV_dt[-1]

        Pts += dPts
        V += dV
        # print(dV)
    return spike_rate
##################################################################

def main():

    dt = 0.1
    dts = 0.5
    tau_m = 10
    Vr = 0
    Vt = 10
    Iext = 15
    sigma = 1.5
    nsteps = 10000

    # spike_rate1 = cbrd(Iext - 0.1, Vt, dt, tau_m, sigma, Vr, nsteps, dts)
    # spike_rate2 = cbrd(Iext + 0.1, Vt, dt, tau_m, sigma, Vr, nsteps, dts)
    # grad = (spike_rate2[-1] - spike_rate1[-1]) / 0.2
    # print(grad)

    spike_rate = cbrd(Iext, Vt, dt, tau_m, sigma, Vr, nsteps, dts)
    spike_rate_mc = simulate_monte_carlo(Iext, Vt, dt, tau_m, sigma, Vr, nsteps)

    plt.plot(spike_rate)
    plt.plot(spike_rate_mc)
    # # plt.plot(V_hist)
    # print(spike_rate[-1], spike_rate_mc[-1])
    #
    # plt.show()


main()