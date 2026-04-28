import numpy as np

def normalize_3d(v):
    v = np.asarray(v, dtype=float)
    axis = v.ndim - 1
    norms = np.linalg.norm(v, axis=axis, keepdims=True)
    nonzero_mask = norms > 1e-10
    res = np.zeros_like(v)
    np.divide(v, norms, out=res, where=nonzero_mask)
    
    return res
    pass