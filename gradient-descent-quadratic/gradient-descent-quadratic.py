def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    for _ in range(steps):
        grad = 2 * a * x0 + b   # derivative
        x0 = x0 - lr * grad      # update
    
    return float(x0)
    pass