def k_means_assignment(points, centroids):
    assignments = []
    
    for p in points:
        best_dist = float('inf')
        best_idx = 0
        
        for idx, c in enumerate(centroids):
            current_dist = sum((p_dim - c_dim) ** 2 for p_dim, c_dim in zip(p, c))
            
            if current_dist < best_dist:
                best_dist = current_dist
                best_idx = idx
        
        assignments.append(best_idx)
        
    return assignments
   