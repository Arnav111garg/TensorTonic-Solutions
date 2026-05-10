def hit_rate_at_k(recommendations, ground_truth, k):
    n_users = len(recommendations)
    if n_users == 0:
        return 0.0
        
    hits = 0
    
    for user_preds, user_truth in zip(recommendations, ground_truth):
        top_k = user_preds[:k]
        
        truth_set = set(user_truth)
        
        for item in top_k:
            if item in truth_set:
                hits += 1
                break
                
    return float(hits / n_users)