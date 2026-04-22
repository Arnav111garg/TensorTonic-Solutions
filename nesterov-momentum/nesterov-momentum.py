import numpy as np

def nesterov_momentum_step(w, v, grad, lr=0.01, momentum=0.9):
    w = np.array(w, dtype=float)
    v = np.array(v, dtype=float)
    grad = np.array(grad, dtype=float)
    
    
    if not (w.shape == v.shape == grad.shape):
        raise ValueError(f"Shape mismatch: w{w.shape}, v{v.shape}, grad{grad.shape}")
    new_v = momentum*v + lr*grad
    new_w = w - new_v
    return new_w, new_v
    pass