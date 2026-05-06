def frequency_encoding(values):
    n = len(values)
    if n == 0:
        return []
        
    counts = {}
    for v in values:
        counts[v] = counts.get(v, 0) + 1
        
    frequencies = {val: count / n for val, count in counts.items()}
    
    return [float(frequencies[v]) for v in values]