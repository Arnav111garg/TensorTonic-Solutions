def differencing(series, order):
    current_series = list(series)
    
    for _ in range(order):
        current_series = [
            current_series[i] - current_series[i-1] 
            for i in range(1, len(current_series))]
        
    return current_series