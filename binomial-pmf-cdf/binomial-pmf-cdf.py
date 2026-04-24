import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    if k < 0:
        return 0.0, 0.0
    if k > n:
        return 0.0, 1.0

    def calculate_pmf(k_val):
        return comb(n, k_val) * (p**k_val) * ((1 - p)**(n - k_val))

    pmf = float(calculate_pmf(k))

    i_values = np.arange(k + 1)
    all_pmfs = calculate_pmf(i_values)
    cdf = float(np.sum(all_pmfs))

    return pmf, cdf
    pass