import math
def cyclic_encoding(values, period):
    encoded_features = []
    
    two_pi = 2 * math.pi
    
    for v in values:
        angle = two_pi * (v / period)
        
        s = math.sin(angle)
        c = math.cos(angle)
        
        encoded_features.append([float(s), float(c)])
        
    return encoded_features