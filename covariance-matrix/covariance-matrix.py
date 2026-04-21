import numpy as np

def covariance_matrix(X):
    X = np.array(X, dtype=float)
    if X.ndim != 2:
        return None
    
    N, D = X.shape
    
    if N < 2:
        return None

    # 2. Center the data (Vectorized)
    # Subtract the mean of each column from the data points
    # Broadcasting handles the (N, D) - (D,) operation automatically
    X_centered = X - np.mean(X, axis=0)

    # 3. Compute Matrix Product (Vectorized)
    # The dot product of the transposed centered matrix and itself
    # Resulting shape: (D, N) @ (N, D) -> (D, D)
    covariance_sum = X_centered.T @ X_centered

    # 4. Apply Sample Normalization (N - 1)
    # Cast to float to ensure precision
    cov_matrix = covariance_sum / (N - 1)

    return cov_matrix
    pass