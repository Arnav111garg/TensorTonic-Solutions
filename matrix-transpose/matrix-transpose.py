import numpy as np

def matrix_transpose(A):
    A = np.array(A)
    N, M = A.shape
    
    # Create empty output matrix
    B = np.empty((M, N), dtype=A.dtype)
    
    # Fill manually
    for i in range(N):
        for j in range(M):
            B[j, i] = A[i, j]
    
    return B

    pass
