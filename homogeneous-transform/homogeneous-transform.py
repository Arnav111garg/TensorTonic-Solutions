import numpy as np

def apply_homogeneous_transform(T, points):
    T = np.array(T, dtype=float)
    points = np.array(points, dtype=float)
    is_single_point = points.ndim == 1
    
    if is_single_point:
        pts = points.reshape(1, 3)
    else:
        pts = points
        
    ones = np.ones((pts.shape[0], 1))
    pts_h = np.hstack([pts, ones])
    
    transformed_h = pts_h @ T.T
    
    result = transformed_h[:, :3]
    
    if is_single_point:
        return result.ravel()
    return result
    pass