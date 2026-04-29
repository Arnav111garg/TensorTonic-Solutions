import numpy as np

def cohens_kappa(rater1, rater2):
    rater1 = np.asarray(rater1)
    rater2 = np.asarray(rater2)
    n = len(rater1)
    
    if n == 0: return 0.0

    p_o = np.sum(rater1 == rater2) / n
    
    if p_o == 1.0:
        return 1.0
    
    labels = np.unique(np.concatenate([rater1, rater2]))
    p_e = 0.0
    for label in labels:
        p_e += (np.sum(rater1 == label) / n) * (np.sum(rater2 == label) / n)
        
    if p_e == 1.0:
        return 0.0
        
    return float((p_o - p_e) / (1 - p_e))
    
    pass
    