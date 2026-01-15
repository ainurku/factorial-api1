import math

def calculate_log(n: float, base: float = 10):
    if n <= 0:
        raise ValueError("n must be > 0")

    if base <= 0 or base == 1:
        raise ValueError("base must be > 0 and != 1")

    return math.log(n, base)
