import numpy as np

def silhouette_score(X, labels):
    n_samples = X.shape[0]
    unique_labels = np.unique(labels)
    n_clusters = len(unique_labels)
    
    if n_clusters < 2:
        raise ValueError("Silhouette Score requires at least 2 clusters.")

    sq_norms = np.sum(X**2, axis=1, keepdims=True)
    dist_matrix = np.sqrt(np.maximum(sq_norms + sq_norms.T - 2 * np.dot(X, X.T), 0.0))

    a = np.zeros(n_samples)
    b = np.full(n_samples, np.inf)

    cluster_masks = (labels == unique_labels[:, np.newaxis])
    cluster_sizes = np.sum(cluster_masks, axis=1)

    for i, label in enumerate(unique_labels):
        mask = cluster_masks[i]
        size = cluster_sizes[i]
        
        cluster_dist_sum = np.sum(dist_matrix[:, mask], axis=1)
        
        if size > 1:
            a[mask] = cluster_dist_sum[mask] / (size - 1)
        else:
            a[mask] = 0.0

        other_mask = ~mask
        neighbor_avg_dist = cluster_dist_sum[other_mask] / size
        
        b[other_mask] = np.minimum(b[other_mask], neighbor_avg_dist)

    max_ab = np.maximum(a, b)
    s = np.zeros(n_samples)
    
    valid_mask = max_ab > 0
    s[valid_mask] = (b[valid_mask] - a[valid_mask]) / max_ab[valid_mask]
    
    return float(np.mean(s))
    pass