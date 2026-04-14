import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    N, D = X.shape
    
    # Initialize
    w = np.zeros(D)
    b = 0.0
    
    for _ in range(steps):
        # Forward pass
        z = X @ w + b              # shape (N,)
        y_hat = _sigmoid(z)         # shape (N,)
        
        # Gradients
        error = y_hat - y          # shape (N,)
        
        dw = (1 / N) * (X.T @ error)   # shape (D,)
        db = (1 / N) * np.sum(error)   # scalar
        
        # Update
        w -= lr * dw
        b -= lr * db
    
    return w, b

    pass