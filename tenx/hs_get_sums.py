import h5pyd as h5py

with h5py.File("/shared/bioconductor/tenx_full.h5", "r") as f:
    dset = f["newassay001"]
    num_col = dset.shape[0]
    for i in range(0, num_col):
        arr = dset[i,:]
        sum = np.sum(arr)
        print(sum)
