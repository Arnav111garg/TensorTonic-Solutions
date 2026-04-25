import numpy as np

def geometric_pmf_mean(k, p):
    k = np.asanyarray(k)
    pmf = np.where(k >= 1, ((1 - p) ** (k - 1)) * p, 0.0)
    mean = 1.0 / p
    
    return pmf, float(mean)
    pass