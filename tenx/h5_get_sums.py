import h5py
import numpy as np

with h5py.File("tenx_full.h5", "r") as f:
    dset = f["newassay001"]
    num_col = dset.shape[0]
    for i in range(0, num_col):
        arr = dset[i,:]
        sum = np.sum(arr)
        print(sum)
