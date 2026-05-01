def cosine_embedding_loss(x1, x2, label, margin):
    dot_product = sum(a * b for a, b in zip(x1, x2))
    norm1 = math.sqrt(sum(a * a for a in x1))
    norm2 = math.sqrt(sum(a * a for a in x2))
    cos_sim = dot_product / (norm1 * norm2)
    if label == 1:
        return float(1 - cos_sim)
    
    elif label == -1:
        return float(max(0.0, cos_sim - margin))
    
    else:
        raise ValueError("Label must be 1 or -1.")