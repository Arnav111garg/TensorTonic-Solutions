import numpy as np

def swish(x):
    x = np.array(x, dtype=float)
    return  x / (1 + np.exp(-x))
    pass