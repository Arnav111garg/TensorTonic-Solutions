import numpy as np

def adamw_step(w, m, v, grad, lr=0.001, beta1=0.9, beta2=0.999, weight_decay=0.01, eps=1e-8):
    w = np.asanyarray(w)
    m = np.asanyarray(m)
    v = np.asanyarray(v)
    grad = np.asanyarray(grad)

    # 2. Update biased first moment estimate
    # m_t = beta1 * m_{t-1} + (1 - beta1) * g_t
    new_m = beta1 * m + (1 - beta1) * grad

    # 3. Update biased second raw moment estimate
    # v_t = beta2 * v_{t-1} + (1 - beta2) * g_t^2
    new_v = beta2 * v + (1 - beta2) * (grad**2)

    # 4. Apply Decoupled Weight Decay
    # w_t = w_{t-1} - lr * weight_decay * w_{t-1}
    # This is the "W" in AdamW - it happens before or during the main update
    w_decayed = w - lr * weight_decay * w

    # 5. Compute the Adaptive Gradient Update
    # For a single step function where 't' (time step) isn't provided for bias correction,
    # we use the raw moment estimates as requested by the simplified update logic.
    adaptive_update = new_m / (np.sqrt(new_v) + eps)

    # 6. Final Parameter Update
    new_w = w_decayed - lr * adaptive_update

    return new_w, new_m, new_v
    pass