def warmup_decay_schedule(base_lr, warmup_steps, total_steps, current_step):
    if current_step <= warmup_steps:
        if warmup_steps == 0:
            return float(base_lr)
        
        lr = base_lr * (current_step / warmup_steps)
        
    else:
        decay_steps = total_steps - warmup_steps
        steps_since_warmup = current_step - warmup_steps
    
        lr = base_lr * (1 - (steps_since_warmup / decay_steps))
        lr = max(0.0, lr)
        
    return float(lr)