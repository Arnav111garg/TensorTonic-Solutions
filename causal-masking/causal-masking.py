import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    T = scores.shape[-1]
    future_mask = np.triu(np.ones((T, T), dtype=bool), k=1)
    
    masked_scores = scores.copy()
    
    masked_scores[..., future_mask] = mask_value
    
    return masked_scores
    pass