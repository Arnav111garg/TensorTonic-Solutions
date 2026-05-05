def interaction_features(X):
    result = []
    
    for row in X:
        n_features = len(row)
        new_row = list(row)
        
        if n_features > 1:
            interactions = []
            for i in range(n_features):
                for j in range(i + 1, n_features):
                    interactions.append(float(row[i] * row[j]))
            
            new_row.extend(interactions)
            
        result.append(new_row)
        
    return result