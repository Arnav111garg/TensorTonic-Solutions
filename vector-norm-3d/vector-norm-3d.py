import numpy as np

def vector_norm_3d(v):
    v = np.asarray(v)
    
    if v.ndim == 1:
        norm = np.sqrt(np.sum(v**2))
        return float(norm)
    
    elif v.ndim == 2:
        return np.sqrt(np.sum(v**2, axis=1))
    
    else:
        raise ValueError("Input must be 1D (shape 3,) or 2D (shape N, 3).")
    pass