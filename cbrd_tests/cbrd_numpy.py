# import matplotlib
# matplotlib.use("Qt5Agg")
import numpy as np
from scipy.signal import parzen
import matplotlib.pyplot as plt

from scipy.special import erf


class CBRD4LIF:

    def __init__(self, dt, dts, Nts, tau_m=10, Vr=0, Vt=10, Iext=15, sigma=1.5):

        # параметры пространства
        self.dt = dt
        self.dts = dts
        self.Nts = Nts

        # объявляем переменные для симуляции Р
        self.ts_states = np.linspace(0, self.dts * self.Nts, self.Nts)
        self.Pts = np.zeros_like(self.ts_states)
        self.Pts[-1] = 1
        self.dt_dts_ratio = self.dt/self.dts
        self.half_dt_ratio = 0.5 * (1 - self.dt_dts_ratio)
        self.dP = np.zeros_like(self.Pts)

        # параметры нейрона
        self.tau_m = tau_m
        self.Vt = Vt
        self.Vr = Vr
        self.Iext = Iext
        self.sigma = sigma

        # параметры для симуляции потенциала
        self.V = np.zeros_like(self.ts_states) + self.Vr #+ 9
        self.dV = np.zeros_like(self.ts_states)
        self.dV_dt = (-self.V + self.Iext) / self.tau_m # np.zeros_like(self.ts_states)

        # переменные для записи потока
        self.flow_x = []
        self.flow_y = []

        self.t = 0

    def update_V(self):

        for i in range(1, self.Nts-1):

            if i > 1:

                a = self.V[i+1] - self.V[i]
                b = self.V[i] - self.V[i-1]

                a_ = self.V[i] - self.V[i-1]
                b_ = self.V[i-1] - self.V[i-2]

                wi = self.limiter(a, b)
                wi_1 = self.limiter(a_, b_)

            else:
                a = self.V[i + 1] - self.V[i]
                b = self.V[i] - self.V[i - 1]
                wi = self.limiter(a, b)
                wi_1 = 0

            self.dV_dt[i] = (-self.V[i] + self.Iext) / self.tau_m
            self.dV[i] = -self.dt_dts_ratio * (self.V[i] - self.V[i-1] + self.half_dt_ratio*( wi - wi_1 ) ) + self.dt * self.dV_dt[i]



        self.dV[0] = 0
        self.dV[-1] = self.dt * (-self.V[-1] + self.Iext) / self.tau_m
        self.V += self.dV


    def H_function(self):
        #print(self.dV_dt[-1], self.V[-1], self.Vt)



        k = self.tau_m / self.dt
        g_tot = 1 / self.tau_m # (Cm = 1) !!!!

        T = np.sqrt(0.5*(1+k)) * g_tot * (self.Vt - self.V) / self.sigma

        A_inf = np.exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
        A = A_inf * (1 - (1 + k)**(-0.71 + 0.0825 * (T + 3) ) )

        dT_dt = -g_tot/self.sigma * np.sqrt(0.5+0.5*k) * self.dV_dt

        dT_dt[dT_dt < 0] = 0

        F_T = np.sqrt(2/np.pi) * np.exp(-T**2) / (1 + erf(T))

        B = -np.sqrt(2) * self.tau_m * dT_dt * F_T

        H = A + B

        return H

    def limiter(self, a, b):
        if a * b <= 0:
            w = 0

        elif a < 0 and a*b > 0:
            w = -min( [abs(a + b)*0.5, 2*min([abs(a), abs(b) ]) ])

        else:
            w = min( [abs(a + b)*0.5, 2*min([ abs(a), abs(b) ]) ])

        return w

    def update(self):

        H = self.H_function()

        for i in range(1, self.Nts-1):

            a = self.Pts[i + 1] - self.Pts[i]
            b = self.Pts[i] - self.Pts[i - 1]
            wi = self.limiter(a, b)

            if i > 1:
                a_ = self.Pts[i] - self.Pts[i-1]
                b_ = self.Pts[i-1] - self.Pts[i-2]
                wi_1 = self.limiter(a_, b_)

            else:
                wi_1 = 0

            self.dP[i] = - self.dt_dts_ratio * (self.Pts[i] - self.Pts[i-1] + self.half_dt_ratio*( wi - wi_1 ) ) - self.dt * self.Pts[i]*H[i]

        a_ = self.Pts[-1] - self.Pts[-2]
        b_ = self.Pts[-2] - self.Pts[-3]
        wi_1 = self.limiter(a_, b_)

        self.dP[0] = -self.dt_dts_ratio * self.Pts[0] - self.dt * np.sum(-self.Pts * H)
        self.dP[-1] = self.dt_dts_ratio * ( self.Pts[-2] + self.half_dt_ratio*wi_1 ) - self.dt * self.Pts[-1] * H[-1]

        self.Pts += self.dP


        # print(np.sum( self.Pts) )     # !!!!!!!!!
        # self.Pts /= np.sum( self.Pts) # !!!!!!!!!


        self.flow_x.append(self.t)
        self.flow_y.append(1000 * self.Pts[0] / self.dts)


        self.update_V()

        self.t += self.dt

        return self.ts_states, self.Pts, self.flow_x, self.flow_y

    def update_with_vectors(self):
        H = self.H_function()
        # print(H[-1])
        diff_Pts = np.diff(self.Pts)

        a = diff_Pts[1:]     # self.Pts[i + 1] - self.Pts[i]
        b = diff_Pts[:-1]        # self.Pts[i] - self.Pts[i - 1]
        wi = self.limiter_with_vectors(a, b)

        a_ = b[1:]
        b_ = b[:-1]
        wi_1 = self.limiter_with_vectors(a_, b_)
        wi_1 = np.append(0, wi_1)

        # print(diff_Pts.size)
        # print(wi.size)
        # print(wi_1.size)

        self.dP[1:-1] = -self.dt_dts_ratio * (diff_Pts[:-1] + self.half_dt_ratio * (wi - wi_1)) - self.dt * self.Pts[1:-1] * H[1:-1]

        a_ = self.Pts[-1] - self.Pts[-2]
        b_ = self.Pts[-2] - self.Pts[-3]
        wi_1 = self.limiter(a_, b_)

        self.dP[0] = -self.dt_dts_ratio * self.Pts[0] - self.dt * np.sum(-self.Pts * H)
        self.dP[-1] = self.dt_dts_ratio * (self.Pts[-2] + self.half_dt_ratio * wi_1) - self.dt * self.Pts[-1] * H[-1]

        self.Pts += self.dP

        self.flow_x.append(self.t)
        self.flow_y.append(1000 * self.Pts[0] / self.dts)

        self.update_V()

        self.t += self.dt

    def limiter_with_vectors(self, a, b):

        w = np.zeros_like(a)

        selected_indx1 = a * b <= 0
        selected_indx2 = (a<0) & (a*b > 0)

        x1 = np.abs(a[selected_indx2] + b[selected_indx2])*0.5
        x2 = 2*np.minimum(np.abs(a[selected_indx2]), np.abs(b[selected_indx2]) )
        w[selected_indx2] = -np.minimum(x1, x2)


        selected_indx3 = np.logical_not(selected_indx1&selected_indx2)

        x1 =  np.abs(a[selected_indx3] + b[selected_indx3])*0.5
        x2 = 2 * np.minimum(np.abs(a[selected_indx3]), np.abs(b[selected_indx3]))

        w[selected_indx3] = np.minimum(x1, x2)


        # if a * b <= 0:
        #    w = 0

        # elif a < 0 and a*b > 0:
        #     w = -min( [abs(a + b)*0.5, 2*min([abs(a), abs(b) ]) ])

        # else:
        #     w = min( [abs(a + b)*0.5, 2*min([ abs(a), abs(b) ]) ])

        return w


############################################################################
# solve cbrd equation
Nts = 400
dt = 0.1
dts = 0.5

cbrd = CBRD4LIF(dt, dts, Nts)

for _ in range(1000):
    cbrd.update_with_vectors()

    # print(cbrd.dV)
    # break
#print(cbrd.V[-1])




plt.plot(cbrd.flow_x, cbrd.flow_y)
plt.show()