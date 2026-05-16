import numpy as np

def cross_entropy_loss(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    N = y_pred.shape[0]
    
    correct_class_probs = y_pred[np.arange(N), y_true]
    
    loss = -np.mean(np.log(correct_class_probs))
    
    return float(loss)
    pass