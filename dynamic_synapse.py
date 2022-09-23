import numpy as np
import matplotlib.pyplot as plt
exp = np.exp

def synaptic_event(delta_t, g0, tau_d, tau_r, tau_f, u, u0, x0, y0):
    # TM Model that depends on tau_d
    tau1r = tau_d / ((tau_d - tau_r) if tau_d != tau_r else 1e-13)
    y_ = y0 * exp(-delta_t / tau_d)
    x_ = 1 + (x0 - 1 + tau1r * y0) * exp(-delta_t / tau_r) - tau1r * y_
    u_ = u0 * exp(-delta_t / tau_f)
    u0 = u_ + u * (1 - u_)
    y0 = y_ + u0 * x_
    x0 = x_ - u0 * x_
    # g0 /= u0
    g = g0 * y0

    # Original TM Model
    # x_ = 1 + (x0 - 1) * exp(-delta_t / tau_r)
    # u_ = u + (u0 - u) * exp(-delta_t / tau_f)
    # g = g0 * u_ * x_
    # x0 = x_ - u_ * x_
    # u0 = u_ + u * (1 - u_)
    return g, x0, y0, u0


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


tau_f = 12 # 1.5 # 23.89 # 50 # ms
tau_r = 1912.0 # 128.0 # 895.2 # 750  # ms   # Synaptic depression rate
tau_d = 23.8 # 20.0 # 3.806 # 2

u_S = 0.0
R_S = 1.0
U_0 = 0.153 #0.264 # 0.2851 # 0.15 # 0.45 #
r_S = 0
A_S = 0

g_hist = []

dt = 0.1
duration = 200
R = 15 # Гц

t = np.arange(0, duration + dt, dt)


# for idx in range(t.size):
#
#     #print(SR_pre)
#     # Usage of releasable neurotransmitter per single action potential:
#     # du_S_dt = -u_S / tau_f + SR_pre[idx] * U_0 * (1 - u_S)
#     # u_S += dt * du_S_dt
#     # r_S = u_S * x_S
#     # # Fraction of synaptic neurotransmitter resources available:
#     # dx_S_dt = (1 - x_S) / tau_d - r_S # 1 (event-driven)
#     # x_S += dt * dx_S_dt
#
#     #########################
#     du_S_dt = -u_S / tau_f + SR_pre[idx] * U_0 * (1 - u_S)
#     u_S += dt * du_S_dt
#
#     rs = u_S * R_S * SR_pre[idx]
#     dR_S_dt = (1 - R_S - A_S) / tau_r - rs
#
#     dA_S_dt = -A_S / tau_d + rs
#
#     R_S += dt * dR_S_dt
#     A_S += dt * dA_S_dt
#     # print(du_S_dt)
#     g_hist.append(A_S)

g0 = 1  #, tau_d, tau_r, tau_f, u = input_vec
u = U_0
x0, y0, u0 = 1.0, 0.0, 0.0
delta_t = np.arange(0, 20 + dt, dt)
g_hist = np.empty(0, dtype=np.float64)

g, x0, y0, u0 = synaptic_event(0.0, g0, tau_d, tau_r, tau_f, u, u0, x0, y0)
start_x = x0
start_y = y0
start_u = u0
g_hist = np.append(g_hist, g)

#print(g0, tau_d, tau_r, tau_f, u, u0, x0, y0)
print(delta_t[-1])
for idx in range(10):
    g, x0, y0, u0 = synaptic_event(delta_t[-1], g0, tau_d, tau_r, tau_f, u, u0, x0, y0)
    g_hist = np.append(g_hist, g)

g_hist2 = []
t_sourse = np.linspace(0, (idx+1)*delta_t[-1], g_hist.size)

SR_pre = np.zeros_like(t) #(np.random.rand(t.size) < (R * 0.001 * dt) ).astype(float)
SR_pre[::delta_t.size] = 1
x0, y0, u0 = 1.0, 0.0, 0.0 # start_x, start_y, start_u
#g_hist2.append(y0)
g0 = 1


#print(g0, tau_d, tau_r, tau_f, u, u0, x0, y0)
for idx in range(t.size):
    g, x0, y0, u0 = synaptic_integration(dt, g0, tau_d, tau_r, tau_f, u, u0, x0, y0, SR_pre[idx])
    g_hist2.append(g)

plt.scatter(t_sourse, g_hist, color="red", label="Sourses model")
plt.plot(t, g_hist2, color="green", label="Iterate model")
plt.legend()
plt.show()

# fig, axes = plt.subplots(nrows=2, sharex=True)
# axes[0].plot(t, g_hist)
# axes[1].plot(t, SR_pre)
#
# axes[0].set_xlim(0, duration)
# axes[0].set_ylim(0, None)
# plt.show()



