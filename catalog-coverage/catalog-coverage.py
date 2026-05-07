def catalog_coverage(recommendations, n_items):
    if n_items <= 0:
        return 0.0
        
    recommended_items = set()
    for user_recs in recommendations:
        for item_id in user_recs:
            recommended_items.add(item_id)
            
    unique_rec_count = len(recommended_items)
    coverage = unique_rec_count / n_items
    
    return float(coverage)