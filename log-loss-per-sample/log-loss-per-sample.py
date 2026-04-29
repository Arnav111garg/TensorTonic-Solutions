import math

def log_loss(y_true, y_pred, eps=1e-15):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    p_clipped = np.clip(y_pred, eps, 1 - eps)
    
    loss = -(y_true * np.log(p_clipped) + (1 - y_true) * np.log(1 - p_clipped))
    
    return loss.tolist()
    pass