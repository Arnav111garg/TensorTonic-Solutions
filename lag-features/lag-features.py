def lag_features(series, lags):
    if not series or not lags:
        return []
        
    max_lag = max(lags)
    n = len(series)
    result = []
    
    for t in range(max_lag, n):
        row = [series[t - lag] for lag in lags]
        result.append(row)
        
    return result