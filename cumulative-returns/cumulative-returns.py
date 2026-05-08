def cumulative_returns(returns):
    cumulative_results = []
    wealth_factor = 1.0
    
    for r in returns:
        wealth_factor *= (1.0 + r)
        
        cumulative_results.append(float(wealth_factor - 1.0))
        
    return cumulative_results