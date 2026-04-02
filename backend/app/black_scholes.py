import math
from scipy.stats import norm


def black_scholes_call(S: float, K: float, T: float, r: float, sigma: float) -> float:
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    return float(call_price)