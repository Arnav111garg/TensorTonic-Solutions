import numpy as np

def majority_classifier(y_train, X_test):
    y_train = np.asarray(y_train)
    
    if y_train.size == 0:
        return np.array([], dtype=int)

    
    classes, first_indices, counts = np.unique(
        y_train, 
        return_index=True, 
        return_counts=True)
    
    max_freq = np.max(counts)
    
    candidates_mask = (counts == max_freq)
    
    candidate_first_appearances = first_indices[candidates_mask]
    
    winner_idx_within_candidates = np.argmin(candidate_first_appearances)
    
    majority_class = classes[candidates_mask][winner_idx_within_candidates]
    
    n_test = len(X_test)
    
    return np.full(n_test, majority_class, dtype=int)
    pass