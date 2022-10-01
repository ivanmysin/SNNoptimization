import numpy as np
import matplotlib.pyplot as plt


# equation dx/dt = -k * x
k_true = 5
k_start = 10

x0 = 5
t0 = 0
tn = 10

dt = 0.001
t = np.arange(t0, tn, dt)

####################################################
x_analitic_t = x0 * np.exp(-k_true * t)
x_numetric_t = np.zeros_like(t)
x_numetric_t[0] = x0

for idx in range(x_numetric_t.size - 1):
    x_numetric_t[idx + 1] = x_numetric_t[idx] * (1 - k_true * dt)

####################################################

learning_rate = 0.01
k = k_start

dL_dk_analitic = np.zeros(20, dtype=np.float64)
dL_dk_numetric = np.zeros_like(dL_dk_analitic)
for ls_idx in range(dL_dk_analitic.size):
    x_analitic_s = x0 * np.exp(-k * t)
    L = 0.5*np.sum( (x_analitic_s - x_analitic_t)**2 )
    dL_dk_analitic[ls_idx] = np.sum( (x_analitic_s - x_analitic_t)*x0*np.exp(-k * t) * (-t)  )

    lamda_lg = np.zeros_like(t)
    for idx in t.size-np.arange(t.size)-2:
        lamda_lg[idx] = lamda_lg[idx+1] - dt * (lamda_lg[idx+1]*k - x_analitic_s[idx+1] + x_analitic_t[idx+1])


    dL_dk_numetric[ls_idx] = -np.sum(lamda_lg * x_analitic_s) # *dt


    k = k - learning_rate*dL_dk_numetric[ls_idx]  # dL_dk_analitic[ls_idx]

    #print(dL_dk_analitic, dL_dk_numetric)


fig, axes = plt.subplots(nrows=2)
axes[0].plot(t, x_analitic_t, color='green', linewidth=5)
axes[0].plot(t, x_analitic_s, color='orange', linewidth=2)

axes[1].plot(dL_dk_analitic, color='green', linewidth=5)
axes[1].plot(dL_dk_numetric, color='orange', linewidth=2)
plt.show()