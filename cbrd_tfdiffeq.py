import numpy as np
import tensorflow as tf
#from tfdiffeq import odeint, odeint_adjoint
import h5py
import matplotlib.pyplot as plt

erf = tf.math.erf
bessel_i0 = tf.math.bessel_i0
sqrt = tf.math.sqrt
exp = tf.math.exp
cos = tf.math.cos
maximum = tf.math.maximum
minimum = tf.math.minimum
abs = tf.math.abs
logical_and = tf.math.logical_and
logical_not = tf.math.logical_not
argmax = tf.math.argmax

SQRT_FROM_2 = np.sqrt(2)
SQRT_FROM_2_PI = 0.7978845608028654
PI = np.pi


@tf.function
def odeint(func, y0, t, rtol=1e-7, atol=1e-9, method=None, options=None):
    y = y0
    solution = tf.TensorArray(tf.float64, size=tf.size(t))
    solution = solution.write(0, y)
    for idx in range(1, tf.size(t)):
        dt = t[idx] - t[idx - 1]
        dy = func(t[idx], y)
        y = y + dt * dy
        solution = solution.write(idx, y)
    solution = solution.stack()
    return solution

odeint_adjoint = odeint

class BaseNeuron(tf.keras.Model):

    def __init__(self, params, dt):
        super(BaseNeuron, self).__init__(name="NeuronPopulation")

        self.Vreset = tf.constant(params["Vreset"], dtype=tf.float64)
        self.Vt = tf.constant(params["Vt"], dtype=tf.float64)


        self.El =  tf.constant(params["El"], dtype=tf.float64)
        self.C =  tf.constant(params["C"], dtype=tf.float64)
        self.sigma = tf.constant(params["sigma"], dtype=tf.float64)

        self.ref_dvdt = params["ref_dvdt"]   # refactory in updates of V and variables of states
        self.refactory = params["refactory"] # refactory for threshold

        self.Iext = tf.Variable(params["Iext"], dtype=tf.float64)
        self.input_index = None

        self.N = params["N"]
        self.start_idx = 0
        self.n_dynamic_vars = 2
        self.end_idx = self.n_dynamic_vars  * self.N


        self.gl = tf.constant(params["gl"], dtype=tf.float64)
        self.dts = tf.constant(params["dts"], dtype=tf.float64)


        self.ref_idx = tf.Variable(int(self.refactory / self.dts), dtype=tf.int32, trainable=False)
        self.ref_dvdt_idx = tf.Variable(int(self.ref_dvdt / self.dts), dtype=tf.int32, trainable=False)

        self.max_roH_idx = tf.Variable(0, dtype=tf.int32, trainable=False)
        self.dt = dt

        self.population_name = params["name"]

    @tf.function
    def H_function(self, V, dVdt, tau_m, Vt, sigma):
        delta_V = maximum((Vt - V), -1.0) #!!!!
        T = delta_V / sigma / SQRT_FROM_2
        A = exp(0.0061 - 1.12 * T - 0.257 * T**2 - 0.072 * T**3 - 0.0117 * T**4)
        dT_dt = -1.0 / sigma / SQRT_FROM_2 * dVdt
        dT_dt = minimum(dT_dt, 0.0)
        F_T = SQRT_FROM_2_PI * exp(- (T**2) ) / (1.00000001 + erf(T))
        B = -SQRT_FROM_2 * dT_dt * F_T * tau_m
        H = (A + B) / tau_m
        H = maximum(H, 0.0)
        H = minimum(H, 1.0)
        return H

    @tf.function
    def limiter(self, a, b):
        w = tf.zeros_like(a)
        selected_indx1 = ((a * b) <= 0)
        selected_indx2 = (a < 0) & (a * b > 0)

        x1 = abs(a + b) * 0.5
        x2 = 2.0 * minimum(abs(a), abs(b))

        w = tf.where(selected_indx2, -minimum(x1, x2), w)


        selected_indx3 = logical_not(logical_and(selected_indx1, selected_indx2))
        w = tf.where(selected_indx3, minimum(x1, x2), w)

        return w

    @tf.function
    def update_z(self, z, dts, Sourse):
        diff_z = z[1:] - z[:-1]
        a = diff_z[1:]
        b = diff_z[:-1]
        wi = self.limiter(a, b)
        a_ = b[1:]
        b_ = b[:-1]
        wi_1 = self.limiter(a_, b_)
        wi_1 = tf.concat([[0, ], wi_1], axis=0)

        dz_1 = -1 / dts * (diff_z[:-1] + 0.5*(1 - self.dt / dts) * (wi - wi_1) ) - Sourse[1:-1]

        dz_0 = -1 / dts * z[0] - Sourse[0]

        dz_2 = 1 / dts * (z[-2] + 0.5 * (1 - self.dt / dts) * wi[-1]) - Sourse[-1]

        dz_0 = tf.reshape(dz_0, [1, ])
        dz_2 = tf.reshape(dz_2, [1, ])

        dz_dt = tf.concat([dz_0, dz_1, dz_2], axis=0)
        return dz_dt

    def get_y0(self):
        return []

    def set_indexes(self, start_idx):
        self.start_idx = start_idx
        self.end_idx = self.start_idx + self.n_dynamic_vars * self.N
        return self.end_idx

class LIF_Neuron(BaseNeuron):
    def __init__(self, params, dt=0.1):

        super(LIF_Neuron, self).__init__(params, dt)

        #self.V = self.V + self.Vreset
        self.sigma = self.sigma / self.gl * sqrt(0.5 * self.gl / self.C)

        self.ro_start_idx = 0
        self.ro_end_idx = self.N
        self.V_start_idx = self.ro_end_idx
        self.V_end_idx = self.V_start_idx + self.N


    @tf.function
    def __call__(self, t, y, gsyn=tf.Variable(0.0, dtype=tf.float64), Isyn=tf.Variable(0.0, dtype=tf.float64)):
        ro = y[self.ro_start_idx : self.ro_end_idx]
        V = y[self.V_start_idx : self.V_end_idx]

        dVdt = (self.gl * (self.El - V) + self.Iext + Isyn) / self.C #!!!!!![self.ref_dvdt_idx: ]
        tau_m = self.C / (self.gl + tf.reduce_sum(gsyn))

        tau_m = tf.reshape(tau_m, shape=(-1, ))
        dVdt = tf.reshape(dVdt, shape=(-1, ))

        H = self.H_function(V, dVdt, tau_m, self.Vt, self.sigma)
        sourse4Pts = ro * H
        firing = tf.math.reduce_sum(sourse4Pts)
        sourse4Pts = tf.tensor_scatter_nd_update(sourse4Pts, [[0], ], -tf.reshape(firing, [1, ]))

        dro_dt = self.update_z(ro, self.dts, sourse4Pts)
        dV_dt = self.update_z(V, self.dts, -dVdt)
        dV_dt = tf.tensor_scatter_nd_update(dV_dt, [[0], [tf.size(dV_dt) - 1]], [0, dVdt[-1]])
        dy_dt = tf.concat([dro_dt, dV_dt], axis=0)
        return dy_dt

    def get_y0(self):
        V = tf.zeros(self.N, dtype=tf.float64)  + self.Vreset
        ro = tf.zeros(self.N, dtype=tf.float64)
        ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[self.N - 1, ]], [1 / self.dts, ]))
        y0 = tf.concat([ro, V], axis=0)
        return y0

class HH_Neuron(BaseNeuron):

    def __init__(self, params, dt=0.1):
        super(HH_Neuron, self).__init__(params, dt)

        self.sigma = self.sigma / self.gl * sqrt(0.5 * self.gl / self.C)

        self.ro_start_idx = 0
        self.ro_end_idx = self.N
        self.V_start_idx = self.ro_end_idx
        self.V_end_idx = self.V_start_idx + self.N

        self.max_roH_idx = tf.Variable(0, dtype=tf.int32, trainable=False)

        self.n_dynamic_vars = 2
        self.channels = []

        start_x_idx = self.V_end_idx
        for ch_idx, chann_param in enumerate(params["channels_params"]):
            chann = chann_param["channel_class"](chann_param, self.N, dt=self.dt)
            end_x_idx = chann.set_start_x_idx(self.ro_start_idx, start_x_idx)
            chann.ref_dvdt_idx = self.ref_dvdt_idx
            self.channels.append(chann)
            self.n_dynamic_vars += chann.n_gate_vars
            start_x_idx = end_x_idx


    @tf.function
    def __call__(self, t, y, gsyn=tf.Variable([0.0, ], dtype=tf.float64), Isyn=tf.Variable([0.0, ], dtype=tf.float64)):

        ro = y[self.ro_start_idx : self.ro_end_idx]
        V = y[self.V_start_idx : self.V_end_idx]

        gch = tf.constant(0.0, dtype=tf.float64)
        Ichs = tf.constant(0.0, dtype=tf.float64)
        for chann in self.channels:
            gch_tmp, Ichs_tmp = chann.get_gch_and_Ich(y)
            gch = gch + gch_tmp
            Ichs = Ichs + Ichs_tmp


        dVdt = (self.gl * (self.El - V) + Ichs + self.Iext + Isyn) / self.C  # !!!!!![self.ref_dvdt_idx: ]
        tau_m = self.C / (self.gl + tf.reduce_sum(gsyn) + tf.reduce_sum(gch) )

        tau_m = tf.reshape(tau_m, shape=(-1,))
        dVdt = tf.reshape(dVdt, shape=(-1,))

        H = self.H_function(V[self.ref_idx:], dVdt[self.ref_idx:], tau_m, self.Vt, self.sigma)
        H = tf.concat([tf.zeros(self.ref_idx, dtype=tf.float64), H], axis=0) ### !!!!! Убрать генерацию массива нулей каждый раз

        sourse4Pts = ro * H
        argmax_ro_H = argmax(sourse4Pts)

        firing = tf.math.reduce_sum(sourse4Pts)

        sourse4Pts = tf.tensor_scatter_nd_update(sourse4Pts, [[0], ], -tf.reshape(firing, [1, ]))

        dro_dt = self.update_z(ro, self.dts, sourse4Pts)

        dV_dt = tf.concat([tf.zeros(self.ref_dvdt_idx, dtype=tf.float64), dVdt[self.ref_dvdt_idx:]], axis=0)  ### !!!!! Убрать генерацию массива нулей каждый раз
        dV_dt = self.update_z(V, self.dts, -dV_dt)
        dV_dt = tf.tensor_scatter_nd_update(dV_dt, [[0], [tf.size(dV_dt) - 1]], [0, dVdt[-1]])

        dx_dt_list = tf.TensorArray(tf.float64, size=0, dynamic_size=True) # = []
        dx_dt_list_idx = 0
        for chann in self.channels:
            dxdt, dxdt_reset = chann(t, y, argmax_ro_H)
            dxdt = tf.reshape(dxdt, shape=(chann.n_gate_vars, self.N))
            start_x_idx = chann.start_x_idx
            end_x_idx = start_x_idx + self.N
            for idx_x_var in range(chann.n_gate_vars):
                x = y[start_x_idx : end_x_idx]
                dx_dt = self.update_z(x, self.dts, -dxdt[idx_x_var, :])
                # print(tf.shape(dxdt_reset))
                # print(dxdt_reset[idx_x_var])
                dx_dt = tf.tensor_scatter_nd_update(dx_dt, [[0], [self.N - 1]], [dxdt_reset[idx_x_var], dxdt[idx_x_var, -1]])
                # dx_dt_list.append(dx_dt)
                dx_dt_list = dx_dt_list.write(dx_dt_list_idx, dx_dt)
                dx_dt_list_idx += 1
                start_x_idx += self.N
                end_x_idx += self.N



        if dx_dt_list.size() > 0:
            dx_dt = dx_dt_list.stack()
            dx_dt = tf.reshape(dx_dt, [-1,])
            dy_dt = tf.concat([dro_dt, dV_dt, dx_dt], axis=0)

        else:
            dy_dt = tf.concat([dro_dt, dV_dt], axis=0)

        return dy_dt


    def get_y0(self):
        V1 = tf.zeros(self.ref_dvdt_idx, dtype=tf.float64) + self.Vreset
        V2 = tf.zeros(self.N-self.ref_dvdt_idx, dtype=tf.float64) + self.El  # - 90.0 #
        V = tf.concat([V1, V2], axis=0)

        ro = tf.zeros(self.N, dtype=tf.float64)
        ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[self.N - 1, ]], [1 / self.dts, ]))

        x0 = []
        for chann in self.channels:
            x0.append( chann.get_y0(V) )
        if len(x0) > 0:
            x0 = tf.concat(x0, axis=0)
            y0 = tf.concat([ro, V, x0], axis=0)
        else:
            y0 = tf.concat([ro, V], axis=0)
        return y0

    def set_indexes(self, start_idx):
        self.start_idx = start_idx
        self.end_idx = self.start_idx + self.n_dynamic_vars * self.N

        self.ro_start_idx = self.start_idx
        self.ro_end_idx = self.ro_start_idx + self.N
        self.V_start_idx = self.ro_end_idx
        self.V_end_idx = self.V_start_idx + self.N



        start_x_idx = self.V_end_idx
        for chann in self.channels:
            end_x_idx = chann.set_start_x_idx(self.start_idx, start_x_idx)
            start_x_idx = end_x_idx

        return self.end_idx


class BaseChannel(tf.Module):

    def __init__(self, params, N, dt=0.1):

        self.gmax = tf.Variable(params['gmax'] , dtype=tf.float64 )
        self.Erev = tf.Variable(params['Erev'], dtype=tf.float64 )
        self.x_reset = tf.Variable(params['x_reset'], dtype=tf.float64 )
        self.degrees =  tf.Variable(params['degrees'], dtype=tf.float64 )

        self.n_gate_vars = tf.size(self.degrees)
        self.degrees =  tf.reshape(self.degrees, shape=[self.n_gate_vars, -1] )

        self.N = N

        self.dt = dt

        self.start_ro_idx = 0
        self.end_ro_idx = self.N

        self.start_V_idx = self.end_ro_idx
        self.end_V_idx = self.start_V_idx + self.N

        self.start_x_idx = self.end_V_idx
        self.end_x_idx = self.start_x_idx + self.N * self.n_gate_vars

        self.ref_dvdt_idx = 1

    def set_start_x_idx(self, start_idx, start_x_idx):
        self.start_ro_idx = start_idx
        self.end_ro_idx = self.start_ro_idx + self.N

        self.start_V_idx = self.end_ro_idx
        self.end_V_idx = self.start_V_idx + self.N

        self.start_x_idx = start_x_idx
        self.end_x_idx = self.start_x_idx + self.N * self.n_gate_vars
        return self.end_x_idx

    @tf.function
    def __call__(self, t, y, argmax_ro_H=0):
        V = y[self.start_V_idx : self.end_V_idx]
        x_inf, tau_x = self.get_x_inf_and_tau_x(V)
        x_inf = tf.reshape(x_inf, shape=(self.n_gate_vars, self.N))
        tau_x = tf.reshape(tau_x, shape=(self.n_gate_vars, self.N))

        x = y[self.start_x_idx : self.end_x_idx]
        x_reshaped = tf.reshape(x, shape=(self.n_gate_vars, self.N))

        ## dxdt = (x_inf - x) / tau_x # !!!!!! Переписать через экспоненцаильный Эйлер
        ##  x_inf - (x_inf - x) * exp(-self.dt / tau_x)  #

        x_new = x_reshaped - (x_reshaped - x_inf) * (1 - exp( -self.dt / tau_x) )

        dxdt = (x_new - x_reshaped) / self.dt

        x4reset = x_reshaped[:, argmax_ro_H] - x_reshaped[:, 0]
        dxdt, dxdt_reset = self.reset(dxdt, x4reset)
        return dxdt, dxdt_reset
    def get_y0(self, V):
        x_inf, _ = self.get_x_inf_and_tau_x(V)
        if len(tf.shape(x_inf)) == 1:
            xr = tf.zeros(self.ref_dvdt_idx, dtype=tf.float64) + self.x_reset
            x_inf = tf.concat([xr, x_inf[self.ref_dvdt_idx:]], axis=0)
        else:
            indexes_list = []
            for idx in range(tf.shape(x_inf)[0]):
                indexes_list.append([idx, 0])
            x_inf = tf.tensor_scatter_nd_update(x_inf, indexes_list, self.x_reset)
            xr = tf.zeros((self.n_gate_vars, self.ref_dvdt_idx), dtype=tf.float64) + tf.reshape(self.x_reset, shape=(self.n_gate_vars, 1))
            x_inf = tf.concat([xr, x_inf[:, self.ref_dvdt_idx:]], axis=1)
        x_inf = tf.reshape(x_inf, shape=(tf.size(x_inf)))

        return x_inf

    def __get_x_inf(self, V):
        x_inf = 1.0 / (1.0 + exp(-0.045 * (V + 10)) )
        return x_inf
    def __get_tau_x(self, V):
        tau_x = 0.5 + 2.0/(1 + exp(0.045 * (V - 50)))
        return tau_x

    def get_x_inf_and_tau_x(self, V):
        x_inf = self.__get_x_inf(V)
        tau_x = self.__get_tau_x(V)

        return x_inf, tau_x


    def get_gch_and_Ich(self, y):
        V = y[self.start_V_idx : self.end_V_idx]
        x = y[self.start_x_idx : self.end_x_idx]
        x = tf.reshape(x, shape=(self.n_gate_vars, self.N) )
        x = tf.math.pow(x, self.degrees)
        g = self.gmax * tf.math.reduce_prod(x, axis=0)
        I = g * (self.Erev - V)
        return g, I

    @tf.function
    def reset(self, dxdt, x4reset):
        xr = tf.zeros((self.n_gate_vars, self.ref_dvdt_idx), dtype=tf.float64)
        dxdt = tf.concat([xr, dxdt[:, self.ref_dvdt_idx:]], axis=1)
        dxdt = tf.reshape(dxdt, shape=[-1])
        dxdt_reset = tf.zeros(self.n_gate_vars, dtype=tf.float64)
        return dxdt, dxdt_reset

class SimlestSinapse(tf.Module):
    def __init__(self, params, dt):
        super(SimlestSinapse, self).__init__(name="Synapse")
        self.dt = dt

    def get_y0(self):
        return []

class PlasticSynapse(SimlestSinapse):
    def __init__(self, params, dt=0.1, start_idx=0):
        super(PlasticSynapse, self).__init__(params, dt)

        tau_ds = []
        tau_rs = []
        tau_fs = []
        Uincs = []
        gbarSs = []
        Erevs = []
        Ws = []

        pre_indxes = []
        post_indxes = []
        for p in params:
            tau_ds.append(p["tau_d"])
            tau_rs.append(p["tau_r"])
            tau_fs.append(p["tau_f"])
            Uincs.append(p["Uinc"])
            gbarSs.append(p["gbarS"])
            Erevs.append(p["Erev"])
            Ws.append(p["w"])

            pre_indxes.append(p["pre"])
            post_indxes.append(p["post"])

        self.tau_d = tf.Variable(tau_ds, dtype=tf.float64, name='tau_d', trainable=True)
        self.tau_r = tf.Variable(tau_rs, dtype=tf.float64, name='tau_r', trainable=True)
        self.tau_f = tf.Variable(tau_fs, dtype=tf.float64, name='tau_f', trainable=True)
        self.Uinc = tf.Variable(Uincs, dtype=tf.float64, name='Uinc', trainable=True)
        self.tau1r = tf.where(self.tau_d != self.tau_r,  self.tau_d / (self.tau_d - self.tau_r), 1e-13)

        self.gbarS = tf.Variable(gbarSs, dtype=tf.float64, name='SynapticConductance', trainable=True)
        self.Erev = tf.Variable(Erevs, dtype=tf.float64, trainable=False)
        self.Erev = tf.reshape(self.Erev, shape=(-1, 1))
        
        self.W = tf.Variable(Ws, dtype=tf.float64, name='Wplasticsyns', trainable=True)

        self.pre_indxes = tf.convert_to_tensor(pre_indxes, dtype=tf.int32)
        self.post_indxes = tf.convert_to_tensor(post_indxes, dtype=tf.int32)

        self.num_synapses = len(params)
        self.num_dynamic_vars = 3 # X, Y and U
        self.start_idx = start_idx
        self.end_idx = self.start_idx + self.num_dynamic_vars * self.num_synapses

        self.start_X_idx = 0
        self.end_X_idx = self.num_synapses

        self.start_R_idx = self.end_X_idx
        self.end_R_idx = self.start_R_idx + self.num_synapses

        self.start_U_idx = self.end_R_idx
        self.end_U_idx = self.start_U_idx + self.num_synapses

    def get_G_Isyn(self, y, Vpost, neuron_post_idx):
        Rofsyn = y[self.start_idx + self.start_R_idx:self.start_idx + self.end_R_idx]
        gsyn_tmp = tf.where(self.post_indxes == neuron_post_idx, Rofsyn, 0.0)

        gsyn = self.gbarS * gsyn_tmp
        gsyn = tf.reshape(gsyn, shape=(-1, 1))
        if tf.math.equal(tf.size(gsyn), 0):
            return tf.zeros_like(Vpost), tf.zeros_like(Vpost)
        else:
            Vdiff = self.Erev - tf.reshape(Vpost, shape=(1, -1))
            Itmp = gsyn * Vdiff
            Isyn = tf.reduce_sum(Itmp, axis=0)

        return gsyn, Isyn



    @tf.function
    def __call__(self, t, y, SRpre=0):

        Spre_normed = SRpre * self.W

        X = y[self.start_X_idx : self.end_X_idx]
        Y = y[self.start_R_idx : self.end_R_idx]
        U = y[self.start_U_idx : self.end_U_idx ]

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

    def get_y0(self):
        X0 = tf.ones(self.num_synapses, dtype=tf.float64) # starting values for X, X0 = 1
        R0_U0 = tf.zeros(2 * self.num_synapses, dtype=tf.float64) # starting values for R and U, R0 = U0 = 0
        y0 = tf.concat([X0, R0_U0], axis=0)
        return y0
##########################################
class VonMissesGenerators(tf.Module):

    def __init__(self, params, dt=0.1, start_idx=0):
        super(VonMissesGenerators, self).__init__()

        Rs = []
        omegas = []
        phases = []
        mean_spike_rates = []


        for params_el in params:
            if "target" in params_el.keys():
                p = params_el["target"]
            else:
                p = params_el

            Rs.append(p["R"])
            omegas.append( p["freq"] )
            phases.append( p["phase"] )
            mean_spike_rates.append(p["mean_spike_rate"] )

        self.omega = tf.constant(omegas, dtype=tf.float64)
        self.phase = tf.constant(phases, dtype=tf.float64)
        self.mean_spike_rate = tf.constant(mean_spike_rates, dtype=tf.float64)

        R = tf.constant(Rs, dtype=tf.float64)
        self.kappa = self.r2kappa(R)

        self.mult4time = tf.constant( 2 * PI * self.omega * 0.001, dtype=tf.float64)

        I0 = bessel_i0(self.kappa)
        self.normalizator = self.mean_spike_rate / I0 * 0.001



    def r2kappa(self, R):
        """
        recalulate kappa from R for von Misses function
        """

        # if R < 0.53:
        #     kappa = 2 * R + R ** 3 + 5 / 6 * R ** 5
        #
        # elif R >= 0.53 and R < 0.85:
        #     kappa = -0.4 + 1.39 * R + 0.43 / (1 - R)
        #
        # elif R >= 0.85:
        #     kappa = 1 / (3 * R - 4 * R ** 2 + R ** 3)
        kappa = tf.where(R < 0.53,  2 * R + R ** 3 + 5 / 6 * R ** 5, 0.0)
        kappa = tf.where(logical_and(R >= 0.53, R < 0.85),  -0.4 + 1.39 * R + 0.43 / (1 - R), kappa)
        kappa = tf.where(R >= 0.85,  1 / (3 * R - 4 * R ** 2 + R ** 3), kappa)
        return kappa

    def __call__(self, t):
        firings = self.normalizator * exp(self.kappa * cos(self.mult4time * t - self.phase) )
        return firings


class Network(tf.keras.Model):

    def __init__(self, params, dt=0.1):
        super(Network, self).__init__(name="Network", dtype=tf.float64)

        params_neurons = params["params_neurons"]

        self.synapses = []
        params_synapses = self._set_connections(params_neurons, params["params_generators"], params["params_synapses"])
        Syn = PlasticSynapse(params_synapses, dt=dt)
        self.synapses.append(Syn)
        # for idx, param_synapse in enumerate(params_synapses):
        #     Syn = PlasticSynapse(param_synapse)
        #     Syn.start_idx = idx * 3 # 3 - число динамических переменных для синапса
        #     Syn.end_idx = Syn.start_idx + 3
        #     self.synapses.append(Syn)

        start_idx4_neurons = self.synapses[-1].end_idx
        self.neurons = []

        ro_0_indexes = []
        start_idx = start_idx4_neurons
        for idx, param_neuron in enumerate(params_neurons):
            Pop = param_neuron["neuron_class"](param_neuron, dt=dt)
            end_idx = Pop.set_indexes(start_idx)
            # start_idx = start_idx4_neurons + idx * Pop.n_dynamic_vars * Pop.N
            # Pop.start_idx = start_idx
            # Pop.end_idx = start_idx + Pop.n_dynamic_vars * Pop.N
            ro_0_indexes.append(start_idx)
            start_idx = end_idx
            self.neurons.append(Pop)

        self.ro_0_indexes = tf.convert_to_tensor(ro_0_indexes, dtype=tf.int32)

        self.generators = []
        generator = VonMissesGenerators(params["params_generators"])

        self.generators.append(generator)


    def _set_connections(self, neurons_params, generators_params, synapses_params):
        neurons_names = []
        for n_params in neurons_params:
            neurons_names.append(n_params["name"])

        for g_params in generators_params:
            neurons_names.append(g_params["name"])

        updated_params_synapses = []
        for s_params in synapses_params:

            try:
                pre_idx = neurons_names.index( s_params["pre_name"] )
                post_idx = neurons_names.index( s_params["post_name"] )
            except ValueError:
                continue
            s_params["pre"] = pre_idx
            s_params["post"] = post_idx

            updated_params_synapses.append(s_params)


        return updated_params_synapses

    @tf.function(
    input_signature=[tf.TensorSpec(shape=(), dtype=tf.float64), tf.TensorSpec(shape=(None, ), dtype=tf.float64)])
    def __call__(self, t, y):
        t = tf.cast(t, dtype=tf.float64)
        dy_dt = []
        neurons_firings = tf.reshape( tf.gather(y, self.ro_0_indexes), shape=(-1, ))

        all_firings = [neurons_firings, ]
        for generator in self.generators:
            artifitial_firing = generator(t)
            #firings = tf.concat(firings, artifitial_firing, axis=0)
            all_firings.append(artifitial_firing)

        firings = tf.concat(all_firings, axis=0)

        for synapse in self.synapses:
            y4syn = y[synapse.start_idx:synapse.end_idx]
            SRpre = tf.reshape(tf.gather(firings, synapse.pre_indxes) , shape=(-1, ))
            dsyn_dt = synapse(t, y4syn, SRpre=SRpre)
            dy_dt.append(dsyn_dt)

        for neuron_idx, neuron in enumerate(self.neurons):
            #y4neuron = y[ neuron.start_idx:neuron.end_idx ]
            Vpost = y[neuron.V_start_idx:neuron.V_end_idx] # 4neuron for LIF

            gsyn_full = 0.0
            Isyn_full = 0.0
            for synapse in self.synapses:
                gsyn, Isyn = synapse.get_G_Isyn(y, Vpost, neuron_idx)
                gsyn_full = gsyn_full + gsyn
                Isyn_full = Isyn_full + Isyn

            if tf.size(Isyn_full) == 0:
                Isyn_full = tf.zeros(neuron.N, dtype=tf.float64)
                gsyn_full = tf.zeros(neuron.N, dtype=tf.float64)
            dneur_dt = neuron(t, y, gsyn=gsyn_full, Isyn=Isyn_full) # for LIF y4neuron

            dy_dt.append( dneur_dt )

        dy_dt = tf.concat(dy_dt, axis=0)
        return dy_dt

    def get_y0(self):
        y0 = []
        for synapse in self.synapses:
            y0.append(synapse.get_y0())
        for neuron in self.neurons:
            y0.append(neuron.get_y0())

        y0 = tf.concat(y0, axis=0)
        return y0

    def save_simulation_data(self, file_path, solution, targets):
       # net.save_simulation_data(path, tf.concat(solutions_full, axis=1), Targets_spikes_rates)
        hf = h5py.File(file_path, 'w')
        solution_dset = hf.create_dataset('solution', data=solution.numpy())
        targets_dset = hf.create_dataset('targets', data=targets.numpy())
        for val in self.synapses[0].trainable_variables:
            hf.create_dataset(val.name, data=val.numpy())

        for neurons_idx, neuron in enumerate(self.neurons):
            solution_dset.attrs[neuron.population_name] = self.ro_0_indexes[neurons_idx]

            solution_dset.attrs[neuron.population_name + "_Iext"] = neuron.Iext.numpy()

        hf.close()

        return

    def load_trained_variables(self, filepath):
        hf = h5py.File(filepath, 'r')
        for val in self.synapses[0].trainable_variables:
            val.assign(hf[val.name][:])

    def set_optimizator(self, optimizer):
        self.optimizer = optimizer

    def loss_function(self, y_true, y_pred): # = mean_squared_logarithmic_error
        L = tf.reduce_sum( tf.math.square(tf.math.log(y_true + 1.) - tf.math.log(y_pred + 1.)))
        # L = tf.reduce_sum( tf.math.square( y_true - y_pred ) )
        return L
    
    #@tf.function
    def fit(self, t, generators4targets, n_inter=50, path4saving=None, win4_start = 2000, win4grad = 500):
        n_points_of_simulation = int(tf.size(t))
        n_loops = int((n_points_of_simulation - win4_start) / win4grad)

        y0_main = self.get_y0()
        for number_of_simulation in range(n_inter):
            solutions_full = []

            time_start_idx = 0
            time_end_idx = win4_start

            solution = odeint(self, y0_main, t[time_start_idx:time_end_idx], method="euler")
            solutions_full.append(solution)

            
            loss_over_simulation = 0.0
            clear_loss_over_simulation = 0.0

            y0 = solution[-1, :]

            trainable_variables = tuple(neuron.Iext for neuron in self.neurons)
            trainable_variables = trainable_variables + self.synapses[0].trainable_variables # (self.synapses[0].gbarS, ) # !!!!!!!!!!!!!!!!!!

            #trainable_variables = self.synapses[0].trainable_variables
            grad_over_simulation = [0] * len(trainable_variables)

            # print(n_loops)
            targets_firings = generators4targets(tf.reshape(t[time_start_idx:time_end_idx], shape=(-1, 1)))
            targets_firings_list = [targets_firings, ]

            for idx in range(n_loops):

                time_start_idx = win4_start + win4grad * idx - 1
                time_end_idx = time_start_idx + win4grad + 1
                t_slice = t[time_start_idx : time_end_idx]

                targets_firings = generators4targets(tf.reshape(t_slice, shape=(-1, 1)))
                targets_firings_list.append(targets_firings[1:])

                with tf.GradientTape(watch_accessed_variables=False) as tape:

                    tape.watch(trainable_variables)

                    solution = odeint_adjoint(self, y0, t_slice, method="euler")

                    solutions_full.append(solution[1:])

                    number_nun = tf.reduce_sum(tf.cast(tf.math.is_nan(solution), dtype=tf.int32))
                    if number_nun > 0:
                        print("Nans values in results!!!!")
                        break

                    firings = tf.gather(solution, self.ro_0_indexes, axis=1)

                    clear_loss = self.loss_function(targets_firings, firings)
                    clear_loss_over_simulation += clear_loss
                    loss = clear_loss
                    for val in self.synapses[0].trainable_variables:
                        #loss += tf.reduce_sum(10e6 * tf.nn.relu(0.005 - val))
                        loss += tf.reduce_sum(-0.001 * tf.math.log(100 * val))

                    loss += tf.reduce_sum(-0.001 * tf.math.log(100 * (1.0 - self.synapses[0].Uinc) ))
                    #loss += tf.reduce_sum(-0.001 * tf.math.log(100 * (1.0 - self.synapses[0].W) ))
                    
                    # for neuron in self.neurons:
                    #     loss += tf.reduce_sum(-0.1 * tf.math.log(1.5 - neuron.Iext))

                    grad = tape.gradient(loss, trainable_variables)

                y0 = solution[-1, :]

                for grad_idx in range(len(grad)):
                    grad_over_simulation[grad_idx] = grad_over_simulation[grad_idx] + grad[grad_idx]
                loss_over_simulation += loss
            
            if not (path4saving is None):
                self.save_simulation_data(path4saving, tf.concat(solutions_full, axis=0), tf.concat(targets_firings_list, axis=0))
            
            self.optimizer.apply_gradients(zip(grad_over_simulation, trainable_variables))

        return  tf.concat(solutions_full, axis=0), clear_loss_over_simulation, loss_over_simulation
        
    def run_simulation(self, t, y0):
        solution = odeint(self, y0, t, method="euler")
        return solution

    def get_gradients4sensivityanalysis(self, t, path4saving=None, win4_start=2000, win4grad=500):
        n_points_of_simulation = int(tf.size(t))
        n_loops = int((n_points_of_simulation - win4_start) / win4grad)
        print(n_loops)

        y0_main = self.get_y0()
        solutions_full = []

        time_start_idx = 0
        time_end_idx = win4_start

        solution = odeint(self, y0_main, t[time_start_idx:time_end_idx], method="euler")
        solutions_full.append(solution)

        y0 = solution[-1, :]

        trainable_variables = tuple(neuron.Iext for neuron in self.neurons)
        trainable_variables = trainable_variables + self.synapses[0].trainable_variables  # (self.synapses[0].gbarS, ) # !!!!!!!!!!!!!!!!!!

        for idx in range(n_loops):
            time_start_idx = win4_start + win4grad * idx - 1
            time_end_idx = time_start_idx + win4grad + 1
            
            t_slice = t[time_start_idx: time_end_idx]

            with tf.GradientTape(watch_accessed_variables=False) as tape:
                tape.watch(trainable_variables[8])
                
                solution = odeint_adjoint(self, y0, t_slice, method="euler")
                solutions_full.append(solution[1:])

                firings = tf.gather(solution, self.ro_0_indexes, axis=1)

                grad = tape.gradient(firings[:, 0], trainable_variables[8])
                print(tf.shape(grad))

                y0 = solution[-1, :]

        solution = tf.concat(solutions_full, axis=0)
        if not (path4saving is None):
            hf = h5py.File(path4saving, 'w')
            solution_dset = hf.create_dataset('solution', data=solution.numpy())

            for val in self.synapses[0].trainable_variables:
                hf.create_dataset(val.name, data=val.numpy())

            for neurons_idx, neuron in enumerate(self.neurons):
                solution_dset.attrs[neuron.population_name] = self.ro_0_indexes[neurons_idx]
                solution_dset.attrs[neuron.population_name + "_Iext"] = neuron.Iext.numpy()

            hf.close()

        return

