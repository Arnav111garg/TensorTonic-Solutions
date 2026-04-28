import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    V_new = V.copy()
    td_error = r + gamma * V_new[s_next] - V_new[s]
    V_new[s] += alpha * td_error
    return V_new
    
    pass