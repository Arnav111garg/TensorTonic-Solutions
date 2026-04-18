import numpy as np

def manhattan_distance(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)

    if x.shape != y.shape:
        raise ValueError("Shapes must match")
    
    return float(np.sum(np.abs(x - y)))
    pass