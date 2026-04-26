import numpy as np

def percentiles(x, q):
    x = np.array(x)
    q = np.array(q, dtype=float)
    n = len(x)
    x_sorted = np.sort(x)
    indices = (q / 100.0) * (n - 1)
    idx_low = np.floor(indices).astype(int)
    idx_high = np.ceil(indices).astype(int)
    fraction = indices - idx_low
    val_low = x_sorted[idx_low]
    val_high = x_sorted[idx_high]
    
    percentiles = val_low + fraction * (val_high - val_low)
    
    return percentiles
    pass