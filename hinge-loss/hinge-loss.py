import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    y_true = np.asanyarray(y_true)
    y_score = np.asanyarray(y_score)

    # 1. Shape Validation
    if y_true.shape != y_score.shape:
        raise ValueError(f"Shape mismatch: y_true {y_true.shape} != y_score {y_score.shape}")

    # 2. Label Validation {-1, +1}
    # Using np.all with bitwise logic is faster than np.unique for large n
    if not np.all((y_true == 1) | (y_true == -1)):
        raise ValueError("y_true must contain only values in {-1, 1}")

    # 3. Vectorized Calculation
    # loss = max(0, margin - y_true * y_score)
    losses = np.maximum(0, margin - y_true * y_score)

    # 4. Reduction
    if reduction == "mean":
        result = np.mean(losses)
    elif reduction == "sum":
        result = np.sum(losses)
    else:
        raise ValueError("reduction must be either 'mean' or 'sum'")

    return float(result)
    pass