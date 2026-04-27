import numpy as np

def mean_squared_error(y_pred, y_true):
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    if (y_pred.shape != y_true.shape):
        return None
    mse = np.mean(np.square(y_true - y_pred))
    return float(mse)
    pass
