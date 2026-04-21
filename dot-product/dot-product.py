import numpy as np

def dot_product(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError(f"Inputs must be 1D arrays. Got ndim: x={x.ndim}, y={y.ndim}")

    # Validation: Mismatched lengths
    if x.shape != y.shape:
        raise ValueError(f"Mismatched lengths: x={len(x)}, y={len(y)}")
    result = np.dot(x, y)
    return result
    pass