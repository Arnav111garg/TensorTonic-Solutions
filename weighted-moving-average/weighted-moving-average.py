def weighted_moving_average(values, weights):
    n = len(values)
    k = len(weights)
    
    total_weight = sum(weights)
    wma_results = []
    
    for i in range(n - k + 1):
        weighted_sum = 0.0
        
        for j in range(k):
            weighted_sum += values[i + j] * weights[j]
            
        wma_results.append(float(weighted_sum / total_weight))
        
    return wma_results