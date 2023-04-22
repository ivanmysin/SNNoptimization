import numpy as np
import tensorflow as tf
import cbrd_tfdiffeq

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

class LIFCompartment(cbrd_tfdiffeq.HH_Neuron):
    def __init__(self, params, dt):
        super(LIFCompartment, self).__init__(params, dt)

        self.neibour_compartments = []

        self.is_sim_rho = params["is_sim_rho"]
        self.connected_compartments = []
        self.connection_strength = tf.constant([], dtype=tf.float64)
        #self.connection_strength = tf.zeros(shape=(0,), dtype=tf.float64)

        if not self.is_sim_rho:
            self.n_dynamic_vars = 1

            del self.ro_start_idx
            del self.ro_end_idx

            self.V_start_idx = 0
            self.V_end_idx =  self.N

    def add_compartment(self, compartment, connection_strength):
        self.connected_compartments.append(compartment)
        self.connection_strength = tf.concat([self.connection_strength, tf.reshape(connection_strength, shape=(1,))], axis=0)

    def set_indexes(self, start_idx):
        self.start_idx = start_idx
        self.end_idx = self.start_idx + self.n_dynamic_vars * self.N

        if self.is_sim_rho:
            self.ro_start_idx = self.start_idx
            self.ro_end_idx = self.ro_start_idx + self.N
            self.V_start_idx = self.ro_end_idx
            self.V_end_idx = self.V_start_idx + self.N
        else:
            self.V_start_idx = self.start_idx
            self.V_end_idx = self.V_start_idx + self.N


        start_x_idx = self.V_end_idx
        for chann in self.channels:
            end_x_idx = chann.set_start_x_idx(self.start_idx, start_x_idx)
            start_x_idx = end_x_idx

        return self.end_idx

    def get_V_by_y(self, y):
        V = y[self.V_start_idx: self.V_end_idx]
        return V

    @tf.function
    def __call__(self, t, y, argmax_ro_H = None, gsyn=tf.Variable([0.0, ], dtype=tf.float64), Isyn=tf.Variable([0.0, ], dtype=tf.float64)):
        if self.is_sim_rho:
            ro = y[self.ro_start_idx: self.ro_end_idx]

        V = y[self.V_start_idx : self.V_end_idx]

        gch = tf.constant(0.0, dtype=tf.float64)
        Ichs = tf.constant(0.0, dtype=tf.float64)
        for chann in self.channels:
            gch_tmp, Ichs_tmp = chann.get_gch_and_Ich(y)
            gch = gch + gch_tmp
            Ichs = Ichs + Ichs_tmp

        I_comps = tf.constant(0.0, dtype=tf.float64)
        for comp_idx, compartment in  enumerate(self.connected_compartments):
            I_comps = I_comps + self.connection_strength[comp_idx] * (compartment.get_V_by_y(y) - V)

        dVdt = (self.gl * (self.El - V) + Ichs + self.Iext + Isyn + I_comps) / self.C  # !!!!!![self.ref_dvdt_idx: ]
        tau_m = self.C / (self.gl + tf.reduce_sum(gsyn) + tf.reduce_sum(gch))

        tau_m = tf.reshape(tau_m, shape=(-1,))
        dVdt = tf.reshape(dVdt, shape=(-1,))

        if self.is_sim_rho:
            H = self.H_function(V[self.ref_idx:], dVdt[self.ref_idx:], tau_m, self.Vt, self.sigma)
            H = tf.concat([tf.zeros(self.ref_idx, dtype=tf.float64), H],
                          axis=0)  ### !!!!! Убрать генерацию массива нулей каждый раз

            sourse4Pts = ro * H
            argmax_ro_H = argmax(sourse4Pts)

            firing = tf.math.reduce_sum(sourse4Pts)

            sourse4Pts = tf.tensor_scatter_nd_update(sourse4Pts, [[0], ], -tf.reshape(firing, [1, ]))

            dro_dt = self.update_z(ro, self.dts, sourse4Pts)

        # else:
        #     argmax_ro_H = argmax_ro_H

        dV_dt = self.reset(dVdt, V, argmax_ro_H)

        dV_dt = self.update_z(V, self.dts, -dV_dt)
        dV_dt = tf.tensor_scatter_nd_update(dV_dt, [[0], [tf.size(dV_dt) - 1]], [0, dVdt[-1]])
        #dV_dt = tf.tensor_scatter_nd_update(dV_dt, [[tf.size(dV_dt) - 1], ], [dVdt[-1], ])

        dx_dt_list = tf.TensorArray(tf.float64, size=0, dynamic_size=True)  # = []
        dx_dt_list_idx = 0
        for chann in self.channels:
            dxdt, dxdt_reset = chann(t, y, argmax_ro_H)
            dxdt = tf.reshape(dxdt, shape=(chann.n_gate_vars, self.N))
            start_x_idx = chann.start_x_idx
            end_x_idx = start_x_idx + self.N
            for idx_x_var in range(chann.n_gate_vars):
                x = y[start_x_idx: end_x_idx]
                dx_dt = self.update_z(x, self.dts, -dxdt[idx_x_var, :])
                dx_dt = tf.tensor_scatter_nd_update(dx_dt, [[0], [self.N - 1]],
                                                    [dxdt_reset[idx_x_var], dxdt[idx_x_var, -1]])
                # dx_dt_list.append(dx_dt)
                dx_dt_list = dx_dt_list.write(dx_dt_list_idx, dx_dt)
                dx_dt_list_idx += 1
                start_x_idx += self.N
                end_x_idx += self.N

        if dx_dt_list.size() > 0:
            dx_dt = dx_dt_list.stack()
            dx_dt = tf.reshape(dx_dt, [-1, ])
            if self.is_sim_rho:
                dy_dt = tf.concat([dro_dt, dV_dt, dx_dt], axis=0)
            else:
                dy_dt = tf.concat([dV_dt, dx_dt], axis=0)
        else:
            if self.is_sim_rho:
                dy_dt = tf.concat([dro_dt, dV_dt], axis=0)
            else:
                dy_dt = tf.concat([dV_dt], axis=0)

        if not self.is_sim_rho:
            argmax_ro_H = None
        return dy_dt, argmax_ro_H

    def get_y0(self):
        V1 = tf.zeros(self.ref_dvdt_idx, dtype=tf.float64) + self.Vreset
        V2 = tf.zeros(self.N-self.ref_dvdt_idx, dtype=tf.float64) + self.El  # - 90.0 #
        V = tf.concat([V1, V2], axis=0)

        if self.is_sim_rho:
            ro = tf.zeros(self.N, dtype=tf.float64)
            ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[self.N - 1, ]], [1 / self.dts, ]))

        x0 = []
        for chann in self.channels:
            x0.append( chann.get_y0(V) )
        if len(x0) > 0:
            x0 = tf.concat(x0, axis=0)
            if self.is_sim_rho:
                y0 = tf.concat([ro, V, x0], axis=0)
            else:
                y0 = tf.concat([V, x0], axis=0)
        else:
            if self.is_sim_rho:
                y0 = tf.concat([ro, V], axis=0)
            else:
                y0 = V
        return y0

    def reset(self, dVdt, V, argmax_ro_H=0):
        dV_dt = tf.concat([tf.zeros(self.ref_dvdt_idx, dtype=tf.float64), dVdt[self.ref_dvdt_idx:]], axis=0)
        return dV_dt


class Soma(LIFCompartment):
    def get_y0(self):
        Vsp = tf.zeros(self.ref_dvdt_idx-1, dtype=tf.float64) + self.Vreset #  - 20.0 #!!!
        Vres = tf.zeros(1, dtype=tf.float64) + self.Vreset
        V2 = tf.zeros(self.N-self.ref_dvdt_idx, dtype=tf.float64) + self.El  # - 90.0 #
        V = tf.concat([Vsp, Vres, V2], axis=0)

        if self.is_sim_rho:
            ro = tf.zeros(self.N, dtype=tf.float64)
            ro = tf.Variable(tf.tensor_scatter_nd_update(ro, [[self.N - 1, ]], [1 / self.dts, ]))

        x0 = []
        for chann in self.channels:
            x0.append( chann.get_y0(V) )
        if len(x0) > 0:
            x0 = tf.concat(x0, axis=0)
            if self.is_sim_rho:
                y0 = tf.concat([ro, V, x0], axis=0)
            else:
                y0 = tf.concat([V, x0], axis=0)
        else:
            if self.is_sim_rho:
                y0 = tf.concat([ro, V], axis=0)
            else:
                y0 = V
        return y0


class Dendrite(LIFCompartment):
    def reset(self, dVdt, V, argmax_ro_H=0):
        dVdt_reset = (V[argmax_ro_H] - V[0]) / self.dt
        dVdt_reset = tf.reshape(dVdt_reset, shape=(1, ))
        dV_dt = tf.concat([dVdt_reset, dVdt[1:]], axis=0)
        return dV_dt