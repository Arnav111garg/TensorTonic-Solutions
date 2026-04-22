import numpy as np

def relu(x):
    x = np.asanyarray(x)
    return np.maximum(0, x)
    pass