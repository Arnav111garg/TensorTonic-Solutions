import numpy as np

def selu(X, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    return [float(lam * x) if x > 0 
        else float(lam * alpha * (math.exp(x) - 1)) 
        for x in X
         ]
    pass
