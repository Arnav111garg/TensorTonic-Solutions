import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # 2. Compute per-sample absolute error
    error = y_true - y_pred
    abs_error = np.abs(error)
    
    # 3. Apply piecewise formula using vectorized np.where
    # Branch 1: Quadratic (Small errors)
    # Branch 2: Linear (Large errors/Outliers)
    loss = np.where(
        abs_error <= delta,
        0.5 * np.square(error),
        delta * (abs_error - 0.5 * delta)
    )
    
    # 4. Return scalar mean
    return float(np.mean(loss))
    pass