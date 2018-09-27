import h5pyd as h5py

with h5py.File("/shared/bioconductor/tenx_full.h5", "r") as f:
    dset = f["newassay001"]
    num_col = dset.shape[0]
    print("shape", dset.shape)
    print("chunks:", dset.chunks)
 
