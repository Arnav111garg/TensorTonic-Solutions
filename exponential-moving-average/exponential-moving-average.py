def exponential_moving_average(values, alpha):
    if not values:
        return []

    ema_results = []
    
    current_ema = float(values[0])
    ema_results.append(current_ema)
    
    for i in range(1, len(values)):
        current_ema = alpha * values[i] + (1 - alpha) * current_ema
        ema_results.append(float(current_ema))
        
    return ema_results