def percent_change(series):
    n = len(series)
    changes = []
    
    for i in range(1, n):
        previous = series[i-1]
        current = series[i]
        
        if previous == 0:
            changes.append(0.0)
        else:
            fractional_change = (current - previous) / previous
            changes.append(float(fractional_change))
            
    return changes