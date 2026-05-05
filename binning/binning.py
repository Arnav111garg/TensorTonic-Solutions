def binning(values, num_bins):
    if not values:
        return []
        
    min_val = min(values)
    max_val = max(values)
    data_range = max_val - min_val
    
    if data_range == 0 or num_bins == 1:
        return [0] * len(values)
        
    bin_width = data_range / num_bins
    assignments = []
    
    for v in values:
        bin_idx = int((v - min_val) / bin_width)
        
        if bin_idx >= num_bins:
            bin_idx = num_bins - 1
            
        assignments.append(bin_idx)
        
    return assignments