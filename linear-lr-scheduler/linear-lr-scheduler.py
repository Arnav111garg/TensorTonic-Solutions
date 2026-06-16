def linear_lr(step, total_steps, initial_lr, end_lr=0.0, warmup_steps=0) -> float:
    
    if step >= total_steps:
        return float(end_lr)
    
    if warmup_steps > 0 and step < warmup_steps:
        progress = step / warmup_steps
        return float(progress * initial_lr)
        
    decay_steps = total_steps - warmup_steps
    steps_into_decay = step - warmup_steps
    
    decay_progress = steps_into_decay / decay_steps
    
    lr = initial_lr - decay_progress * (initial_lr - end_lr)
    
    return float(lr)
    pass