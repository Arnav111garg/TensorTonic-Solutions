def he_initialization(W, fan_in):
    limit = math.sqrt(6 / (fan_in))
    range_val = 2 * limit
    
    scaled_W = []
    for row in W:
        scaled_row = [float(v * range_val - limit) for v in row]
        scaled_W.append(scaled_row)
        
    return scaled_W