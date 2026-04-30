def elu(X, alpha):

    return [
        float(x) if x > 0 
        else float(alpha * (math.exp(x) - 1)) 
        for x in X
    ]