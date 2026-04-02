from time import perf_counter

from app.black_scholes import black_scholes_call
from app.monte_carlo import monte_carlo_call


CASES = [
    {"S": 100, "K": 95, "T": 1, "r": 0.05, "sigma": 0.2, "N": 1000},
    {"S": 100, "K": 100, "T": 1, "r": 0.05, "sigma": 0.2, "N": 10000},
    {"S": 100, "K": 110, "T": 1, "r": 0.05, "sigma": 0.2, "N": 50000},
]


def run_benchmark_cases() -> list[dict]:
    results: list[dict] = []

    for case in CASES:
        bs_start = perf_counter()
        bs_price = black_scholes_call(case["S"], case["K"], case["T"], case["r"], case["sigma"])
        bs_runtime_ms = (perf_counter() - bs_start) * 1000

        mc_start = perf_counter()
        mc_price = monte_carlo_call(
            case["S"],
            case["K"],
            case["T"],
            case["r"],
            case["sigma"],
            case["N"],
            seed=42,
        )
        mc_runtime_ms = (perf_counter() - mc_start) * 1000

        results.append(
            {
                "inputs": case,
                "black_scholes_price": bs_price,
                "black_scholes_runtime_ms": round(bs_runtime_ms, 4),
                "monte_carlo_price": mc_price,
                "monte_carlo_runtime_ms": round(mc_runtime_ms, 4),
                "absolute_error": abs(bs_price - mc_price),
            }
        )

    return results


if __name__ == "__main__":
    for row in run_benchmark_cases():
        print(row)
