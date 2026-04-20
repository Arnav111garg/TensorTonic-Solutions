import numpy as np

def r2_score(y_true, y_pred) -> float:
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    # Calculate Residual Sum of Squares
    ss_res = np.sum((y_true - y_pred) ** 2)
    
    # Calculate Total Sum of Squares
    # SS_tot = sum((y_true - mean(y_true))^2)
    diff_true = y_true - np.mean(y_true)
    ss_tot = np.sum(diff_true ** 2)
    
    # Handle the constant-target edge case
    if ss_tot == 0:
        # If all y_true are equal, check if y_pred matches perfectly
        return 1.0 if np.array_equal(y_true, y_pred) else 0.0
    
    # Standard R2 calculation
    score = 1 - (ss_res / ss_tot)
    
    return float(score)
    pass