import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    real_scores = np.asarray(real_scores)
    fake_scores = np.asarray(fake_scores)
    wasserstein_critic_loss = np.mean(fake_scores) - np.mean(real_scores)
    return float(wasserstein_critic_loss)
    pass