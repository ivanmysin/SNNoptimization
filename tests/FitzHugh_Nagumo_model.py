import numpy as np
import matplotlib.pyplot as plt

def forward(Iext, dt, N, a, b, tau_u):
    v = -1.7
    u = 0
    V = np.zeros(N, dtype=np.float64)
    U = np.zeros_like(V)
    for idx in range(N):
        V[idx] = v
        U[idx] = u
        v = v + dt * (v - (v**3)/3 - u + Iext)
        u = u + dt * (v + a - b*u) / tau_u
    V[-1] = v
    U[-1] = u

    return V, U
##############################################################################
def backward(Iext, V, Vtarget, dt, N, b, tau_u):

    df_dx = np.zeros(shape=(2, 2), dtype=np.float64)
    df_dx[0, 1] = -1
    df_dx[1, 0] = 1 / tau_u
    df_dx[1, 1] = -b / tau_u

    dg_dx = np.zeros(shape=(2, 1), dtype=np.float64)

    df_dtheta = np.asarray([1, 0]).reshape(2, 1)

    dL_dIext = 0
    lamda = np.zeros(shape=(2, 1), dtype=np.float64)
    for idx in N - np.arange(N) - 2:
        df_dx[0, 0] = -V[idx]**2
        dg_dx[0] = V[idx] - Vtarget[idx]

        d_l = -np.dot( df_dx.T, lamda) - dg_dx
        # print(np.dot( df_dx.T, lamda))

        lamda = lamda - dt * d_l

        # print(lamda[idx, :])
        dL_dIext += np.dot(lamda.T, df_dtheta)

    dL_dIext = dL_dIext.ravel() * dt
    return dL_dIext
##############################################################################


dt = 0.01
duration = 15
Iext_target = 0.5
a = 0.7
b = 0.8
tau_u = 12.5
t = np.arange(0, duration, dt)

Vtarget, Utarget = forward(Iext_target, dt, t.size, a, b, tau_u)

Iext_start = 0.4
V, U = forward(Iext_start, dt, t.size, a, b, tau_u)
dL_dIext = backward(Iext_start, V, Vtarget, dt, t.size, b, tau_u)

step_h = 0.001
V1, _ = forward(Iext_start-step_h, dt, t.size, a, b, tau_u)
V2, _ = forward(Iext_start+step_h, dt, t.size, a, b, tau_u)

L1 = 0.5*np.sum( (V1 - Vtarget)**2 ) * dt
L2 = 0.5*np.sum( (V2 - Vtarget)**2 ) * dt
dL_dIext_num = (L2 - L1) / (2*step_h)

print(dL_dIext, dL_dIext_num)

plt.plot(t, V)
plt.plot(t, Vtarget)
plt.show()