# from time import perf_counter

# from app.black_scholes import black_scholes_call
# from app.monte_carlo import monte_carlo_call


# CASES = [
#     {"S": 100, "K": 95, "T": 1, "r": 0.05, "sigma": 0.2, "N": 1000},
#     {"S": 100, "K": 100, "T": 1, "r": 0.05, "sigma": 0.2, "N": 10000},
#     {"S": 100, "K": 110, "T": 1, "r": 0.05, "sigma": 0.2, "N": 50000},
# ]


# def run_benchmark_cases() -> list[dict]:
#     results: list[dict] = []

#     for case in CASES:
#         bs_start = perf_counter()
#         bs_price = black_scholes_call(case["S"], case["K"], case["T"], case["r"], case["sigma"])
#         bs_runtime_ms = (perf_counter() - bs_start) * 1000

#         mc_start = perf_counter()
#         mc_price = monte_carlo_call(
#             case["S"],
#             case["K"],
#             case["T"],
#             case["r"],
#             case["sigma"],
#             case["N"],
#             seed=42,
#         )
#         mc_runtime_ms = (perf_counter() - mc_start) * 1000

#         results.append(
#             {
#                 "inputs": case,
#                 "black_scholes_price": bs_price,
#                 "black_scholes_runtime_ms": round(bs_runtime_ms, 4),
#                 "monte_carlo_price": mc_price,
#                 "monte_carlo_runtime_ms": round(mc_runtime_ms, 4),
#                 "absolute_error": abs(bs_price - mc_price),
#             }
#         )

#     return results


# if __name__ == "__main__":
#     for row in run_benchmark_cases():
#         print(row)
import csv
from pathlib import Path
from time import perf_counter

try:
    from app.black_scholes import black_scholes_call
    from app.monte_carlo import monte_carlo_call
except ModuleNotFoundError:
    # Allow direct execution: python backend/app/benchmark.py
    from black_scholes import black_scholes_call
    from monte_carlo import monte_carlo_call


BASE_CASES = [
    {"label": "ITM", "S": 100, "K": 95, "T": 1, "r": 0.05, "sigma": 0.2},
    {"label": "ATM", "S": 100, "K": 100, "T": 1, "r": 0.05, "sigma": 0.2},
    {"label": "OTM", "S": 100, "K": 110, "T": 1, "r": 0.05, "sigma": 0.2},
]

N_VALUES = [1000, 5000, 10000, 50000, 100000]


def run_benchmark_cases() -> list[dict]:
    results: list[dict] = []

    for base_case in BASE_CASES:
        for N in N_VALUES:
            case = {**base_case, "N": N}

            print(f"Running {case['label']} with N={case['N']}")

            bs_price = black_scholes_call(
                case["S"],
                case["K"],
                case["T"],
                case["r"],
                case["sigma"],
            )

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

            absolute_error = abs(bs_price - mc_price)
            relative_error = absolute_error / bs_price if bs_price != 0 else 0.0

            results.append(
                {
                    "label": case["label"],
                    "S": case["S"],
                    "K": case["K"],
                    "T": case["T"],
                    "r": case["r"],
                    "sigma": case["sigma"],
                    "N": case["N"],
                    "black_scholes_price": bs_price,
                    "monte_carlo_price": mc_price,
                    "monte_carlo_runtime_ms": round(mc_runtime_ms, 4),
                    "absolute_error": round(absolute_error, 6),
                    "relative_error": round(relative_error, 6),
                }
            )

    return results


def export_results_to_csv(results: list[dict], filename: str = "benchmark_results.csv") -> Path:
    output_path = Path(__file__).resolve().parent / filename

    if not results:
        raise ValueError("No benchmark results to export.")

    fieldnames = list(results[0].keys())

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    return output_path


if __name__ == "__main__":
    results = run_benchmark_cases()

    print(f"\nTotal rows: {len(results)}\n")

    for row in results:
        print(row)

    csv_path = export_results_to_csv(results)
    print(f"\nCSV created at: {csv_path}")