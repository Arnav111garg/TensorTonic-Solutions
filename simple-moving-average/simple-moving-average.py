def simple_moving_average(values, window_size):
    n = len(values)
    sma_results = []
    
    for i in range(n - window_size + 1):
        window = values[i : i + window_size]
        
        window_average = sum(window) / window_size
        
        sma_results.append(float(window_average))
        
    return sma_results
    