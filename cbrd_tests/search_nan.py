import numpy as np
import matplotlib.pyplot as plt
import h5py

hf = h5py.File('/home/ivan/Data/interneurons_theta/solution_7.hdf5', 'r')
dset_solution = hf['solution'][:]

idx_fist = 1000000000
for idx in range(3 * 46):
    x = dset_solution[:, idx]

    idx_tmp = np.argwhere( np.logical_or((x < 0.0), (x > 100)))
    idx_tmp = idx_tmp.ravel()

    try:
        if idx_fist > idx_tmp[0]:
            idx_fist = idx_tmp[0]
            print(idx, idx_fist)
    except IndexError:
        continue
print(idx_fist)


