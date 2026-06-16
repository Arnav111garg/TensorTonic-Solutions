import numpy as np

def softmax(x):
    axis = -1
    
    x_max = np.max(x, axis=axis, keepdims=True)
    stabilized_x = x - x_max
    
    exp_x = np.exp(stabilized_x)
    
    probabilities = exp_x / np.sum(exp_x, axis=axis, keepdims=True)
    
    return probabilities
    pass