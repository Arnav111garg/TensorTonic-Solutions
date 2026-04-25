import numpy as np
from collections import Counter

def mean_median_mode(x):
    x = np.array(x, dtype=float)
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    max_freq = max(counts.values())
    
    modes = [val for val, freq in counts.items() if freq == max_freq]
    
    mode = float(min(modes))
    
    return mean, median, mode
    pass