import math

from app.black_scholes import black_scholes_call
from app.monte_carlo import monte_carlo_call


def test_black_scholes_returns_positive_sensible_value() -> None:
    price = black_scholes_call(100, 95, 1, 0.05, 0.2)

    assert price > 0
    assert price < 100


def test_monte_carlo_is_close_to_black_scholes() -> None:
    bs = black_scholes_call(100, 95, 1, 0.05, 0.2)
    mc = monte_carlo_call(100, 95, 1, 0.05, 0.2, 100000, 42)

    assert math.isclose(mc, bs, abs_tol=0.15)
