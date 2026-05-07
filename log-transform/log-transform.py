import math
def log_transform(values):
    return [float(math.log1p(v)) for v in values]