import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    arr = np.asarray(X).astype(float)
    mu = np.mean(arr, axis=axis, keepdims=True)
    sigma = np.std(arr, axis=axis, keepdims=True)
    z = (arr - mu) / (sigma + eps)
    return z
    pass