import h5pyd as h5py
import numpy as np
import time

max_retry = 60

with h5py.File("/shared/bioconductor/tenx_full.h5", "r") as f:
    dset = f["newassay001"]
    num_col = dset.shape[0]
    for i in range(0, num_col):
        # TBD: Move this retry logic into h5pyd
        retry_count = 0
        while True:
            try:
                arr = dset[i,:]
                break
            except OSError as oe:
                retry_count += 1
                print("ERROR[{}]: {}".format(retry_count, oe))
                time.sleep(1)


        sum = np.sum(arr)
        print(sum)
