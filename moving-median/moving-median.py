def moving_median(values, window_size):
    n = len(values)
    results = []
    
    for i in range(n - window_size + 1):
        window = sorted(values[i : i + window_size])
        
        if window_size % 2 == 1:
            median = float(window[window_size // 2])
        else:
            mid1 = window[window_size // 2 - 1]
            mid2 = window[window_size // 2]
            median = (mid1 + mid2) / 2.0
            
        results.append(float(median))
        
    return results