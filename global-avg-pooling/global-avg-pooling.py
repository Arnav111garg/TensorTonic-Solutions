import numpy as np

def global_avg_pool(x):
    if x.ndim not in (3, 4):
        raise ValueError(f"Expected input with 3 or 4 dimensions, got {x.ndim}.")
        
    gap_result = np.mean(x, axis=(-2, -1), dtype=np.float64)
    
    return gap_result
    pass