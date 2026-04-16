import numpy as np

def entropy_node(y):
    y = np.array(y)
    
    # Handle empty node
    if y.size == 0:
        return 0.0
    
    # Count class frequencies
    _, counts = np.unique(y, return_counts=True)
    
    # Convert to probabilities
    probs = counts / counts.sum()
    
    # Avoid log(0) by filtering zero probabilities
    probs = probs[probs > 0]
    
    # Compute entropy (base-2)
    entropy = -np.sum(probs * np.log2(probs))
    
    return float(entropy)
    pass