import numpy as np
import h5py

filepath = '/home/ivan/Data/interurons_test/solution_001.hdf5'

with h5py.File(filepath, 'r') as file:
    dset_solution = file['solution']
    dset_targets = file['targets']
    solution = dset_solution[:]
    targets = dset_targets[:]

    pop_indxes_keys = {}
    for key, value in dset_solution.attrs.items():
        if key.find("Iext") == -1:
            pop_indxes_keys[key] = value

    loss = 0
    for idx, (neuron_name, neuron_idx) in enumerate(sorted(pop_indxes_keys.items(), key=lambda item: item[1])):
        firings = solution[10000:, neuron_idx]
        target = targets[:, idx]

        loss += np.sum( (firings - target)**2 )
print(loss)