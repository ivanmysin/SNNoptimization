import numpy as np
import matplotlib.pyplot as plt
exp = np.exp
def synaptic_integration(delta_t, g0, tau_d, tau_r, tau_f, u, u0, x0, y0, SRpre):
    # TM Model that depends on tau_d
    tau1r = tau_d / ((tau_d - tau_r) if tau_d != tau_r else 1e-13)
    y_ = y0 * exp(-delta_t / tau_d)
    x_ = 1 + (x0 - 1 + tau1r * y0) * exp(-delta_t / tau_r) - tau1r * y_
    u_ = u0 * exp(-delta_t / tau_f)
    u0 = u_ + u * (1 - u_) * SRpre
    y0 = y_ + u0 * x_ * SRpre
    x0 = x_ - u0 * x_ * SRpre
    g = g0 * y0

    return g, x0, y0, u0
def run_integration(t, delta_t, g0, tau_d, tau_r, tau_f, u, u0, x0, y0, SRpre):
    for idx in range(t.size):
        g, x0, y0, u0 = synaptic_integration(delta_t, g0, tau_d, tau_r, tau_f, u, u0, x0, y0, SRpre[idx])

    return g, x0, y0, u0
#######################################################################
class Test:
    def __init__(self, params):


        self.tau_d = params["tau_d"]
        self.tau_r = params["tau_r"]
        self.tau_f = params["tau_f"]
        self.Uinc =  params["Uinc"]

        self.gbarS = params["gbarS"]
        self.Erev = params["Erev"]

        #tau_d, tau_r, tau_f, u, u0, x0, y0

        self.S = 0
        self.x = 1.0
        self.y = 0.0
        self.u = 0.0
        self.w = 1.0

        if self.tau_d != self.tau_r:
            self.tau1r = self.tau_d / (self.tau_d - self.tau_r)
        else:
            self.tau1r = 1e-13

    def update(self, dt, SRpre):
        #SRpre = self.pre.get_flow()

        y_ = self.y * exp(-dt / self.tau_d)
        x_ = 1 + (self.x - 1 + self.tau1r * self.y) * exp(-dt / self.tau_r) - self.tau1r * y_
        u_ = self.u * exp(-dt / self.tau_f)
        self.u = u_ + self.Uinc * (1 - u_) * SRpre
        self.y = y_ + self.u * x_ * SRpre
        self.x = x_ - self.u * x_ * SRpre
        gsyn = self.gbarS * self.w * self.y
        # Isyn = gsyn * (self.post.getV() - self.Erev)
        # self.post.add_Isyn(-Isyn, gsyn)

        return



#######################################################################
tau_f = 12 # 1.5 # 23.89 # 50 # ms
tau_r = 1912.0 # 128.0 # 895.2 # 750  # ms   # Synaptic depression rate
tau_d = 23.8 # 20.0 # 3.806 # 2
g0 = 1.0
u = 0.153
x0, y0, u0 = 1.0, 0.0, 0.0
dt = 0.1
t = np.arange(0, 1.5, dt)
SR_pre = np.zeros_like(t) #(np.random.rand(t.size) < (R * 0.001 * dt) ).astype(float)
SR_pre[::150] = 1


g_1, x0_1, y0_1, u0_1 = run_integration(t, dt, g0, tau_d, tau_r, tau_f, u, u0, x0, y0, SR_pre)
print(g_1, x0_1, y0_1, u0_1 )


synapse_params = {
    "w" : 5.0,
    "pre" : None,
    "post": None,
    "tau_f" : 12.0,  # ms
    "tau_r" : 1912.0, #  ms   # Synaptic depression rate
    "tau_d" : 23.8, #
    "Uinc"  : 0.153,
    "gbarS" : 1.0,
    "Erev": -75.0,
}
test = Test(synapse_params)

for idx in range(t.size):
    test.update(dt, SR_pre[idx])

print(test.y, test.x, test.y, test.u )