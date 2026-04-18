def f1_micro(y_true, y_pred) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Input lengths must match")
    n = len(y_true)
    
    # Count correct predictions
    tp = 0
    for yt, yp in zip(y_true, y_pred):
        if yt == yp:
            tp += 1
    
    # Micro-F1 (same as accuracy here)
    return float(tp / n) if n > 0 else 0.0 
    
    
    pass