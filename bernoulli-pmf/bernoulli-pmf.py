import numpy as np

def bernoulli_pmf_and_moments(x, p):
    x = np.asarray(x)
    
    pmf = np.where(x == 1, p, np.where(x == 0, 1 - p, 0.0))
    
    mean = float(p)
    variance = float(p * (1 - p))
    
    return pmf, mean, variance
    pass