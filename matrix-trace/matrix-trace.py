import numpy as np

def matrix_trace(A):
    A = np.asarray(A)
    rows, cols = A.shape
    if rows != cols:
        raise ValueError("Trace is only defined for square matrices.")
    
    trace_sum = 0
    for i in range(rows):
        trace_sum += A[i, i]
        
    return trace_sum
    pass
