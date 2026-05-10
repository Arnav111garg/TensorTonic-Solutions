def rank_transform(values):
    n = len(values)
    if n == 0:
        return []
        
    indexed = sorted(enumerate(values), key=lambda x: x[1])
    
    ranks = [0.0] * n
    i = 0
    
    while i < n:
        j = i
        while j < n - 1 and indexed[j+1][1] == indexed[i][1]:
            j += 1
            
        avg_rank = (i + 1 + j + 1) / 2.0
        
        for k in range(i, j + 1):
            original_idx = indexed[k][0]
            ranks[original_idx] = avg_rank
            
        i = j + 1
        
    return ranks