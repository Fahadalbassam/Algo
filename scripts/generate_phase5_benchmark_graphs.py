from __future__ import annotations

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


ROOT_DIR = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT_DIR / "backend" / "app" / "benchmark_results.csv"
OUTPUT_DIR = ROOT_DIR / "docs" / "evidence"
RUNTIME_PNG_PATH = OUTPUT_DIR / "phase5_runtime_vs_n.png"
ABS_ERROR_PNG_PATH = OUTPUT_DIR / "phase5_abs_error_vs_n.png"
PRICE_COMPARISON_PNG_PATH = OUTPUT_DIR / "phase5_price_comparison.png"

REQUIRED_COLUMNS = {
    "label",
    "S",
    "K",
    "T",
    "r",
    "sigma",
    "N",
    "seed",
    "black_scholes_price",
    "black_scholes_runtime_ms",
    "monte_carlo_price",
    "monte_carlo_runtime_ms",
    "absolute_error",
    "relative_error",
}

RUNTIME_TITLE = "Monte Carlo Runtime vs Simulation Count (N)"
ABS_ERROR_TITLE = "Monte Carlo Absolute Error vs Simulation Count (N)"
PRICE_COMPARISON_TITLE = "Black-Scholes vs Monte Carlo Prices Across Benchmark Cases"


def load_benchmark_rows() -> list[dict[str, float | int | str]]:
    with CSV_PATH.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = set(reader.fieldnames or [])
        missing_columns = REQUIRED_COLUMNS - fieldnames
        if missing_columns:
            missing_list = ", ".join(sorted(missing_columns))
            raise ValueError(f"benchmark_results.csv is missing required columns: {missing_list}")

        rows: list[dict[str, float | int | str]] = []
        for row in reader:
            rows.append(
                {
                    "label": row["label"],
                    "N": int(row["N"]),
                    "black_scholes_price": float(row["black_scholes_price"]),
                    "monte_carlo_price": float(row["monte_carlo_price"]),
                    "monte_carlo_runtime_ms": float(row["monte_carlo_runtime_ms"]),
                    "absolute_error": float(row["absolute_error"]),
                }
            )

    if not rows:
        raise ValueError("benchmark_results.csv does not contain any benchmark rows.")

    return rows


def group_rows_by_label(rows: list[dict[str, float | int | str]]) -> dict[str, list[dict[str, float | int | str]]]:
    grouped: dict[str, list[dict[str, float | int | str]]] = {}
    for row in rows:
        label = str(row["label"])
        grouped.setdefault(label, []).append(row)

    for label_rows in grouped.values():
        label_rows.sort(key=lambda item: int(item["N"]))

    return grouped


def plot_runtime_vs_n(grouped_rows: dict[str, list[dict[str, float | int | str]]]) -> None:
    figure, axis = plt.subplots(figsize=(10, 6))
    for label, rows in grouped_rows.items():
        axis.plot(
            [int(row["N"]) for row in rows],
            [float(row["monte_carlo_runtime_ms"]) for row in rows],
            marker="o",
            label=label,
        )

    axis.set_title(RUNTIME_TITLE)
    axis.set_xlabel("N")
    axis.set_ylabel("monte_carlo_runtime_ms")
    axis.grid(True, alpha=0.3)
    axis.legend()
    figure.tight_layout()
    figure.savefig(RUNTIME_PNG_PATH, dpi=200)
    plt.close(figure)


def plot_abs_error_vs_n(grouped_rows: dict[str, list[dict[str, float | int | str]]]) -> None:
    figure, axis = plt.subplots(figsize=(10, 6))
    for label, rows in grouped_rows.items():
        axis.plot(
            [int(row["N"]) for row in rows],
            [float(row["absolute_error"]) for row in rows],
            marker="o",
            label=label,
        )

    axis.set_title(ABS_ERROR_TITLE)
    axis.set_xlabel("N")
    axis.set_ylabel("absolute_error")
    axis.grid(True, alpha=0.3)
    axis.legend()
    figure.tight_layout()
    figure.savefig(ABS_ERROR_PNG_PATH, dpi=200)
    plt.close(figure)


def plot_price_comparison(rows: list[dict[str, float | int | str]]) -> None:
    benchmark_case_labels = [f"{row['label']}-{row['N']}" for row in rows]
    x_positions = list(range(len(rows)))

    figure, axis = plt.subplots(figsize=(12, 6))
    axis.plot(
        x_positions,
        [float(row["black_scholes_price"]) for row in rows],
        marker="o",
        label="Black-Scholes",
    )
    axis.plot(
        x_positions,
        [float(row["monte_carlo_price"]) for row in rows],
        marker="o",
        label="Monte Carlo",
    )

    axis.set_title(PRICE_COMPARISON_TITLE)
    axis.set_xlabel("Benchmark Case (label-N)")
    axis.set_ylabel("option price")
    axis.set_xticks(x_positions)
    axis.set_xticklabels(benchmark_case_labels, rotation=45, ha="right")
    axis.grid(True, alpha=0.3)
    axis.legend()
    figure.tight_layout()
    figure.savefig(PRICE_COMPARISON_PNG_PATH, dpi=200)
    plt.close(figure)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_benchmark_rows()
    grouped_rows = group_rows_by_label(rows)
    plot_runtime_vs_n(grouped_rows)
    plot_abs_error_vs_n(grouped_rows)
    plot_price_comparison(rows)


if __name__ == "__main__":
    main()
