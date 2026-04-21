import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    X = np.asarray(X).astype(float)
    X_min = np.min(X, axis=axis, keepdims=True)
    X_max = np.max(X, axis=axis, keepdims=True)
    diff = X_max - X_min
    denom = np.maximum(diff, eps)
    X_scaled = (X - X_min) / denom
    return X_scaled
    pass