import numpy as np
import matplotlib.pyplot as plt
from brian2 import *
import net_lib

rates_template = '{fr} * Hz * exp({kappa} * cos(2*pi*{freq}*Hz*t - {phase}) )'
generator_params = {
    "name" : "ec3",
    "R": 0.2,
    "freq": 6.0,
    "mean_spike_rate": 5.5, # 5,
    "phase": -1.57,
}

kappa, IO = net_lib.r2kappa(generator_params["R"])
generator_params["kappa"] = kappa
generator_params["fr"] = generator_params["mean_spike_rate"] / IO

rates = rates_template.format(**generator_params)
N = 1000
duration = 1 * second
pg = PoissonGroup(N, rates=rates)
pg_sm = SpikeMonitor(pg)

run(duration)

mfr = np.asarray(pg_sm.t/ms).size / N / (duration/second)
print(generator_params["mean_spike_rate"], mfr)
firing_rate, bins = np.histogram(pg_sm.t/ms, bins=int(duration/ms)+1, range=[0, int(duration/ms)+1])
dbins = 0.001*(bins[1] - bins[0])
firing_rate = firing_rate / N / dbins

t = np.linspace(0, duration/second, 1000)
sine = np.max(firing_rate) * 0.5 * (np.cos(2*np.pi*generator_params["freq"]*t)+1)
fig, axes = plt.subplots(nrows=2)
axes[0].plot(t, sine)
axes[0].plot(0.001*bins[:-1], firing_rate)
axes[1].scatter(pg_sm.t/ms, pg_sm.i, s=2)

plt.show()


