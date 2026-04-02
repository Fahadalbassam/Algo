import numpy as np


def monte_carlo_call(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    N: int,
    seed: int | None = None,
) -> float:
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(N)

    drift = (r - 0.5 * sigma**2) * T
    diffusion = sigma * np.sqrt(T) * z
    terminal_prices = S * np.exp(drift + diffusion)

    payoffs = np.maximum(terminal_prices - K, 0.0)
    discounted_price = np.exp(-r * T) * np.mean(payoffs)
    return float(discounted_price)
