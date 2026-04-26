import numpy as np

def auc(fpr, tpr):
    fpr = np.asarray(fpr)
    tpr = np.asarray(tpr)
    
    
    if fpr.shape != tpr.shape:
        raise ValueError(f"Shape mismatch: fpr {fpr.shape} vs tpr {tpr.shape}")
    
    if len(fpr) < 2:
        raise ValueError("At least 2 points (M >= 2) are required to compute AUC.")

    auc = np.trapezoid(y=tpr, x=fpr)
    
    return float(np.abs(auc))
    pass