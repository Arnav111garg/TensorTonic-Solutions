import numpy as np

def dropout(x, p=0.5, rng=None):
    x = np.array(x, dtype=float)
    if p == 0:
        return x.astype(float), np.ones_like(x, dtype=float)
    
    if rng is None:
        random_values = np.random.random(x.shape)
    else:
        random_values = rng.random(x.shape)
        
    keep_prob = 1.0 - p
    scale = 1.0 / keep_prob
    
    dropout_pattern = (random_values < keep_prob).astype(float) * scale
    
    output = x * dropout_pattern
    
    return output, dropout_pattern
    pass