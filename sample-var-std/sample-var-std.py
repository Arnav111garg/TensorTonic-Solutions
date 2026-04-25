import numpy as np

def sample_var_std(x):
    x = np.asarray(x)
    n = len(x)
    
    if n < 2:
        raise ValueError("Sample size must be at least 2 for Bessel's correction.")

    mean_x = np.mean(x)
    
    variance = np.sum((x - mean_x) ** 2) / (n - 1)
    
    std_dev = np.sqrt(variance)
    
    return float(variance), float(std_dev)
    pass