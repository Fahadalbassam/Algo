# import numpy as np


# def monte_carlo_call(
#     S: float,
#     K: float,
#     T: float,
#     r: float,
#     sigma: float,
#     N: int,
#     seed: int | None = None,
# ) -> float:
#     rng = np.random.default_rng(seed)
#     z = rng.standard_normal(N)

#     drift = (r - 0.5 * sigma**2) * T
#     diffusion = sigma * np.sqrt(T) * z
#     terminal_prices = S * np.exp(drift + diffusion)

#     payoffs = np.maximum(terminal_prices - K, 0.0)
#     discounted_price = np.exp(-r * T) * np.mean(payoffs)
#     return float(discounted_price)
import time
import numpy as np


def monte_carlo_price(
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


def monte_carlo_call(
    S: float,
    K: float,
    T: float,
    r: float,
    sigma: float,
    N: int,
    seed: int | None = None,
) -> dict:
    if S <= 0:
        raise ValueError("S must be greater than 0")
    if K <= 0:
        raise ValueError("K must be greater than 0")
    if T <= 0:
        raise ValueError("T must be greater than 0")
    if sigma <= 0:
        raise ValueError("sigma must be greater than 0")
    if N <= 0:
        raise ValueError("N must be greater than 0")

    start_time = time.perf_counter()

    price = monte_carlo_price(
        S=S,
        K=K,
        T=T,
        r=r,
        sigma=sigma,
        N=N,
        seed=seed,
    )

    runtime_ms = (time.perf_counter() - start_time) * 1000

    return {
        "method": "monte_carlo",
        "price": price,
        "display_price": round(price, 2),
        "runtime_ms": round(runtime_ms, 2),
        "inputs": {
            "S": S,
            "K": K,
            "T": T,
            "r": r,
            "sigma": sigma,
            "N": N,
            "seed": seed,
        },
    }


if __name__ == "__main__":
    result = monte_carlo_call(
        S=100,
        K=100,
        T=1,
        r=0.05,
        sigma=0.2,
        N=10000,
        seed=42,
    )
    print(result)