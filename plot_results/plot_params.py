import sys
sys.path.extend(['/home/ivan/PycharmProjects/SNNoptimization'])
import numpy as np
import matplotlib.pyplot as plt
import pickle
#from code_generated_params import params_net
from scipy.stats import pearsonr

with open('/home/ivan/Data/Opt_res/params_net.pickle', 'rb') as file:
    params_net = pickle.load(file)

neurons = {}
for cell in params_net['params_neurons']:
    neurons[cell['name']] = cell

    print(cell['name'], cell['Iext'])

generators = {}
for cell in params_net['params_generators']:
    generators[cell['name']] = cell


cos_phase_diff = []
syn_ps1 = []
syn_ps2 = []

for syn in params_net['params_synapses']:
    if syn["Erev"] != -75.0:
        continue
    pre_name = syn['pre_name']
    post_name = syn['post_name']

    if post_name == 'olm':
         continue
    #
    # if pre_name == post_name:
    #     continue

    phi_pre = neurons[pre_name]['target']['phase']
    #phi_pre = generators[pre_name]['phase']

    phi_post = neurons[post_name]['target']['phase']

    cos_df = np.sin(phi_post - phi_pre) # np.cos(phi_post - phi_pre) #

    #syn_ps.append(syn['gbarS']*syn['w']*neurons[pre_name]['target']['mean_spike_rate'])

    syn_ps1.append(syn['gbarS'])
    syn_ps2.append(syn['tau_d'])

    #syn_ps3.append(syn['Uinc'])
    #syn_ps4.append(syn['tau_r'])
    #syn_ps5.append(syn['tau_f'])


    cos_phase_diff.append(cos_df)

    print(pre_name, ", ", post_name, ", ", syn['gbarS'])

R, p = pearsonr(cos_phase_diff, syn_ps1)
print(R, p)
plt.scatter(cos_phase_diff, syn_ps1)
#plt.scatter(syn_ps, syn_ps2)
plt.show()


