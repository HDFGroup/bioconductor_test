import sys
import random
import h5pyd as h5py

NUM_COLS = 27998  # 2nd index of dataset shape
cols = 100
index = 0
# calculate sums for NUM_COLS continguous columns

if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print("usage: python hs_perf [num_cols] [start]")
    sys.exit(0)
if len(sys.argv) > 1:
    cols = int(sys.argv[1])
    if cols > NUM_COLS:
        cols = NUM_COLS
if len(sys.argv) > 2:
    index = int(sys.argv[2])
    if index + cols > NUM_COLS:
        # adjust so we don't run off the array
        index = NUM_COLS - cols
print("index:", index, "cols:", cols)
print("="*40)


with h5py.File("/shared/bioconductor/tenx_full.h5", "r") as f:
    dset = f["newassay001"]
    num_col = dset.shape[0]
    for i in range(index, index+cols):
        arr = dset[i,:]
        sum = np.sum(arr)
        print(sum)
