import sys
sys.path.append('../')
from code_generated_params import params_net

connections = {
            # connection to pyramidal neurons
            "ca3_spatial2pyr": {
                "gmax": 1000,
                "gmax_std" : 0.9,

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob": 0.6,

                "delay": 1.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "rad_list",

                #"NMDA" : {
                #    "gNMDAmax" : 0.02, # mS
                #    "gmax_std" : 0.001,
                #    "tcon" : 2.3,   # ms
                #    "tcoff" : 95.0, # ms
                #    "enmda" : 0,
                #},
            },

            "ca3_non_spatial2pyr": {
                "gmax": 0.016, #
                "gmax_std" : 0.002, # 0.5, #

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob": 0.4, # 0.3,

                "delay": 1.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "rad_list",

                #"NMDA" : {
                #    "gNMDAmax" : 0.02, # mS
                #    "gmax_std" : 0.001,
                #    "tcon" : 2.3,   # ms
                #    "tcoff" : 95.0, # ms
                #    "enmda" : 0,
                #},
            },

           "mec2pyr": {
                "gmax": 500 , #1000* 20 #0.1, # 0.06,
                "gmax_std" : 0.4, #  0.007,

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob":  0.6,

                "delay": 10,
                "delay_std" : 2,


                "sourse_compartment" : "acell",
                "target_compartment" : "lm_list",

                # "NMDA" : {
                #     "gNMDAmax" : 0.01, # mS
                #     "gmax_std" : 0.001,
                #     "tcon" : 2.3,   # ms
                #     "tcoff" : 95.0, # ms
                #     "enmda" : 0,
                #},
            },

            "pyr2pyr": {
                "gmax": 0.01,
                "gmax_std" : 0.007,

                "Erev": 0.0,
                "tau_rise": 0.1,
                "tau_decay": 1.5,

                "prob":  0.01,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "axon",
                "target_compartment" : "basal_list",

                # "NMDA" : {
                #     "gNMDAmax" : 0.02, # mS
                #    "gmax_std" : 0.001,
                #    "tcon" : 2.3,   # ms
                #    "tcoff" : 95.0, # ms
                #    "enmda" : 0,
                #},
            },

            "cckbas2pyr": {
                "gmax": 2.5,
                "gmax_std" : 1.2,

                "Erev": -75,
                "tau_rise": 0.2,
                "tau_decay": 4.2,

                "prob": 0.63,

                "delay": 2.5,
                "delay_std" : 1.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "soma_list",
            },


           "ivy2pyr": {
                "gmax": 0.053,
                "gmax_std" : 0.02,

                "Erev": -75,
                "tau_rise": 1.1,
                "tau_decay": 11,

                "prob": 0.13,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "lm_list",
            },


           "aac2pyr": {
                "gmax": 20.5,
                "gmax_std" : 10,

                "Erev": -75,
                "tau_rise": 0.28,
                "tau_decay": 8.4,

                "prob": 0.29,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "axon_list",
            },

           "olm2pyr": {
                "gmax": 1.7,
                "gmax_std" : 0.9,

                "Erev": -75,
                "tau_rise": 0.13,
                "tau_decay": 11,

                "prob": 0.29,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "lm_list",
            },

           "pvbas2pyr": {
                "gmax": 30 ,
                "gmax_std" : 0.9,

                "Erev": -75,
                "tau_rise": 0.3,
                "tau_decay": 6.2,

                "prob": 0.8,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "soma_list",
            },

           "bis2pyr": {
                "gmax": 0.009,
                "gmax_std" : 0.005,

                "Erev": -75,
                "tau_rise": 0.11,
                "tau_decay": 9.7,

                "prob": 0.14,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

           "ngf2pyr": {
                "gmax": 0.098,
                "gmax_std" : 0.05,

                "Erev": -75,
                "tau_rise": 9,
                "tau_decay": 39,

                "prob": 0.29,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "lm_list",
            },

           "sca2pyr": {
                "gmax": 0.098,
                "gmax_std" : 0.05,

                "Erev": -75,
                "tau_rise": 0.3,
                "tau_decay": 6.2,

                "prob": 0.29,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "rad_list",
            },
            # end connection to pyramids

            # connection to pvbas
            "ca3_spatial2pvbas": {
                "gmax": 15,
                "gmax_std" : 0.2,

                "Erev": 0,
                "tau_rise": 2.0,
                "tau_decay": 6.3,

                "prob": 0.6,

                "delay": 1.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",

                #"NMDA" : {
                #    "gNMDAmax" : 0.01, # mS
                #    "gmax_std" : 0.001,
                #    "tcon" : 2.3,   # ms
                #    "tcoff" : 95.0, # ms
                #    "enmda" : 0,
                #},
            },

            "ca3_non_spatial2pvbas": {
                "gmax": 0.9,
                "gmax_std" : 0.1,

                "Erev": 0,
                "tau_rise": 2.0,
                "tau_decay": 6.3,

                "prob": 0.06,

                "delay": 1.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",

                #"NMDA" : {
                #    "gNMDAmax" : 0.01, # mS
                #    "gmax_std" : 0.001,
                #    "tcon" : 2.3,   # ms
                #    "tcoff" : 95.0, # ms
                #    "enmda" : 0,
                #},
            },

            "pyr2pvbas": {
                "gmax": 0.5,
                "gmax_std" : 0.04,

                "Erev": 0,
                "tau_rise": 0.07,
                "tau_decay": 0.2,

                "prob": 0.13,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "axon",
                "target_compartment" : "dendrite_list",

                #"NMDA" : {
                #    "gNMDAmax" : 0.01, # mS
                #    "gmax_std" : 0.001,
                #    "tcon" : 2.3,   # ms
                #    "tcoff" : 95.0, # ms
                #    "enmda" : 0,
                #},
            },

            "pvbas2pvbas": {
                "gmax": 10.0,
                "gmax_std" : 0.01,

                "Erev": -75,
                "tau_rise": 0.8,
                "tau_decay": 4.8,

                "prob": 0.7,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "soma",
            },

            "cckbas2pvbas": {
                "gmax": 10.0,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.43,
                "tau_decay": 4.49,

                "prob": 0.38,

                "delay": 4.5,
                "delay_std" : 2.0,


                "sourse_compartment" : "soma",
                "target_compartment" : "soma",
            },

            "olm2pvbas": {
                "gmax": 0.73,
                "gmax_std" : 0.35,

                "Erev": -75,
                "tau_rise": 0.25,
                "tau_decay": 7.5,

                "prob": 0.5,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            # hypotetical connections
            "bis2pvbas": {
                "gmax": 1.1,
                "gmax_std" : 0.05,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.5,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "ngf2pvbas": {
                 "gmax": 1.0,
                 "gmax_std" : 0.05,

                 "Erev": -75,
                 "tau_rise": 0.5,
                 "tau_decay": 4.0,

                 "prob": 0.8,

                 "delay": 1.2,
                 "delay_std" : 0.2,


                 "sourse_compartment" : "soma",
                 "target_compartment" : "dendrite_list",
             },

            "ivy2pvbas": {
                "gmax": 10.1,
                "gmax_std" : 0.5,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.8,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "sca2pvbas": {
                 "gmax": 1.1,
                 "gmax_std" : 0.05,

                 "Erev": -75,
                 "tau_rise": 0.5,
                 "tau_decay": 4.0,

                 "prob": 0.5,

                 "delay": 1.2,
                 "delay_std" : 0.2,


                 "sourse_compartment" : "soma",
                 "target_compartment" : "dendrite_list",
            },

            # end connection to pvbas

            # connections to cckbas
            "msteevracells2cckbas" : {
                "gmax" : 3.5,
                "gmax_std" : 0.2,
                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 5.0,

                "prob": 0.5,

                "delay": 10.5,
                "delay_std" : 2.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "pvbas2cckbas": {
                "gmax": 1.0,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.29,
                "tau_decay": 2.67,

                "prob": 0.05,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },


           "cckbas2cckbas": {
                "gmax": 0.2,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.2,
                "tau_decay": 4.2,

                "prob": 0.63,

                "delay": 2.7,
                "delay_std" : 0.5,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },


            # hypotetical connections
            "bis2cckbas": {
                "gmax": 1.0,
                "gmax_std" : 0.7,

               "Erev": -75,
               "tau_rise": 0.5,
               "tau_decay": 4.0,

               "prob": 0.2,

               "delay": 1.2,
               "delay_std" : 0.2,


               "sourse_compartment" : "soma",
               "target_compartment" : "dendrite_list",
            },


            "ngf2cckbas": {
                 "gmax": 0.5,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 10.0,

                "prob": 0.1,

                "delay": 1.2,
                "delay_std" : 0.2,
                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            # end connections to cckbas


            # connections to aac
            "msteevracells2aac" : {
                "gmax" : 0.9,
                "gmax_std" : 0.7,
                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob": 0.5,

                "delay": 10.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "soma",
            },

            "pyr2aac": {
                "gmax": 0.04,
                "gmax_std" : 0.02,

                "Erev": 0,
                "tau_rise": 0.3,
                "tau_decay": 0.6,

                "prob": 0.07,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "axon",
                "target_compartment" : "dendrite_list",
            },

            "ca3_spatial2aac": {
                "gmax": 0.7,
                "gmax_std" : 0.2,

                "Erev": 0,
                "tau_rise": 2,
                "tau_decay": 6.3,

                "prob": 0.02,

                "delay": 2.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "ca3_non_spatial2aac": {
                "gmax": 0.7,
                "gmax_std" : 0.2,

                "Erev": 0,
                "tau_rise": 2,
                "tau_decay": 6.3,

                "prob": 0.02,

                "delay": 2.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },


            # hypotetical connections
            "mec2aac": {
                "gmax": 1.0,
                "gmax_std" : 0.05,

                "Erev": 0,
                "tau_rise": 2,
                "tau_decay": 6.3,

                "prob": 0.01,

                "delay": 10.0,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },


            "olm2aac": {
                "gmax": 1.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "bis2aac": {
                "gmax": 1.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "pvbas2aac": {
                "gmax": 1.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2, # 0.8,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "cckbas2aac": {
                "gmax": 0.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "ivy2aac": {
                "gmax": 0.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "sca2aac": {
                "gmax": 1.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.1,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },
            # end connections to aac

            # connections to olm
            "msach2olm" : {
                "gmax" : 1.5,
                "gmax_std" : 0.1,
                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob": 0.6,

                "delay": 10.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "soma",
            },

           "pyr2olm": {
                "gmax": 0.031,
                "gmax_std" : 0.0015,

                "Erev": 0,
                "tau_rise": 0.3,
                "tau_decay": 0.6,

                "prob": 0.081,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "axon",
                "target_compartment" : "dendrite_list",
            },


           # hypotetical connections
           "ivy2olm": {
                "gmax": 1.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.5,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

           "sca2olm": {
                "gmax": 1.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },
            # end connections to olm

            # connections to bis
           "pyr2bis": {
                "gmax": 0.3, # 0.14,
                "gmax_std" : 0.07,

                "Erev": 0,
                "tau_rise": 1.3,
                "tau_decay": 8.0,

                "prob": 0.14,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "axon",
                "target_compartment" : "dendrite_list",
            },

           "pvbas2bis": {
                "gmax": 0.035,
                "gmax_std" : 0.015,

                "Erev": -75,
                "tau_rise": 0.29,
                "tau_decay": 2.67,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "cckbas2bis": {
                "gmax": 0.1,
                "gmax_std" : 0.05,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "sca2bis": {
                "gmax": 0.1,
                "gmax_std" : 0.05,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.05,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },



            # hypotetical connetions to bis
            "ca3_spatial2bis": {
                "gmax": 0.02, # 0.14,
                "gmax_std" : 0.01,

                "Erev": 0,
                "tau_rise": 1.3,
                "tau_decay": 8.0,

                "prob": 0.06,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "ca3_non_spatial2bis": {
                "gmax": 0.02,
                "gmax_std" : 0.01,

                "Erev": 0,
                "tau_rise": 1.3,
                "tau_decay": 8.0,

                "prob": 0.06,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "mec2bis": {
                "gmax": 0.5,
                "gmax_std" : 0.3,

                "Erev": 0,
                "tau_rise": 1.3,
                "tau_decay": 8.0,

                "prob": 0.01,

                "delay": 10.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "bis2bis": {
                "gmax": 0.5,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            # end connections to bis

            # connections to ivy
           "pyr2ivy": {
                "gmax": 0.041,
                "gmax_std" : 0.021,

                "Erev": 0,
                "tau_rise": 0.3,
                "tau_decay": 0.6,

                "prob": 0.13,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "axon",
                "target_compartment" : "dendrite_list",
            },

            # hypotetical connections
            "ivy2ivy": {
                "gmax": 0.5,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.5,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "pvbas2ivy": {
                "gmax": 0.5,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.5,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "cckbas2ivy": {
                "gmax": 0.5,
                "gmax_std" : 0.07,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.1,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "sca2ivy": {
                "gmax": 3.5,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.2,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

             # end connections to ivy


            # connections to ngf
            "ca3_spatial2ngf": {
                "gmax": 1.42,
                "gmax_std" : 0.6 ,

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob": 0.2,

                "delay": 1.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "ca3_non_spatial2ngf": {
                "gmax": 1.42,
                "gmax_std" : 0.6 ,

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob": 0.2,

                "delay": 1.5,
                "delay_std" : 0.5,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "mec2ngf": {
                "gmax": 1.7,
                "gmax_std" : 0.3,

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 3,

                "prob": 0.1, # ! need to optimize

                "delay": 10.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "olm2ngf": {
                "gmax": 1.27,
                "gmax_std" : 0.6,

                "Erev": -75,
                "tau_rise": 1.3,
                "tau_decay": 10.2,

                "prob": 0.4,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

           "ngf2ngf": {
                "gmax": 0.75,
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 3.1,
                "tau_decay": 42,

                "prob": 0.7,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            # hypotetical connections
            "ivy2ngf": {
                "gmax": 0.9, # 20
                "gmax_std" : 0.7,

                "Erev": -75,
                "tau_rise": 3.1,
                "tau_decay": 42,

                "prob": 0.8,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },
            # end of connections to ngf


            # connections to sca
           "olm2sca": {
                "gmax": 1.3,
                "gmax_std" : 0.6,

                "Erev": -75,
                "tau_rise": 0.07,
                "tau_decay": 29,

                "prob": 0.1,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },


           "sca2sca": {
                "gmax": 0.03,
                "gmax_std" : 0.015,

                "Erev": -75,
                "tau_rise": 4 ,
                "tau_decay": 34.3,

                "prob": 0.3,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            # hypotetical connections
            "ca3_spatial2sca": {
                "gmax": 0.05,
                "gmax_std" : 0.02,

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.06,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "ca3_non_spatial2sca": {
                "gmax": 0.05,
                "gmax_std" : 0.02,

                "Erev": 0,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.06,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "acell",
                "target_compartment" : "dendrite_list",
            },

            "ivy2sca": {
                "gmax": 0.5,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.1,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "ngf2sca": {
                "gmax": 0.5,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.5,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },

            "bis2sca": {
                "gmax": 0.5,
                "gmax_std" : 0.2,

                "Erev": -75,
                "tau_rise": 0.5,
                "tau_decay": 4.0,

                "prob": 0.5,

                "delay": 1.2,
                "delay_std" : 0.2,


                "sourse_compartment" : "soma",
                "target_compartment" : "dendrite_list",
            },
} # end of connetion settings


connects = []
for elem in params_net["params_synapses"]:
    connects.append(elem["pre_name"] + "2" + elem["post_name"])

for key in connections.keys():
    if "2pyr" in key:
        continue
    if "sca" in key:
        continue

    key = key.replace("pyr", "ca1pyr")
    key = key.replace("ca3_spatial", "ca3pyr")
    key = key.replace("ca3_non_spatial", "ca3pyr")
    key = key.replace("mec", "ec3")
    if not(key in connects):
        print(key)