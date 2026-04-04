# Phase 5 Benchmark Graph Notes

## Monte Carlo Runtime vs Simulation Count (N)
- Exact graph title: Monte Carlo Runtime vs Simulation Count (N)
- What it shows: This graph plots `monte_carlo_runtime_ms` against `N` for the benchmark labels in `backend/app/benchmark_results.csv`, making it easy to see how Monte Carlo runtime changes as the simulation count increases across the ITM, ATM, and OTM cases.
- Why it is safe for the milestone: It is a read-only visualization derived directly from the already verified benchmark CSV, so it adds reporting evidence without changing pricing logic, APIs, frontend behavior, datasets, or benchmark generation code.
- Report-ready caption: Monte Carlo runtime generally increases as the simulation count grows across the benchmark cases. The chart provides milestone evidence that the benchmark artifact captures the expected scaling trend from 1,000 to 100,000 simulations.

## Monte Carlo Absolute Error vs Simulation Count (N)
- Exact graph title: Monte Carlo Absolute Error vs Simulation Count (N)
- What it shows: This graph plots `absolute_error` against `N` for each benchmark label, showing how the Monte Carlo estimate compares with the Black-Scholes reference as the number of simulations rises.
- Why it is safe for the milestone: It uses only the locked benchmark CSV as input and summarizes an existing exported metric, so it is a reporting-only artifact that does not alter any model implementation or milestone dataset.
- Report-ready caption: Monte Carlo absolute error trends downward as the number of simulations increases, showing convergence toward the analytical Black-Scholes result. This makes the figure suitable as milestone evidence that higher simulation counts improve pricing accuracy across the benchmark cases.

## Black-Scholes vs Monte Carlo Prices Across Benchmark Cases
- Exact graph title: Black-Scholes vs Monte Carlo Prices Across Benchmark Cases
- What it shows: This graph compares `black_scholes_price` and `monte_carlo_price` for each benchmark case label formed as `label-N`, so each exported case can be visually checked for consistency between the analytical and simulation-based prices.
- Why it is safe for the milestone: It is a read-only comparison built from the verified benchmark export and does not modify any backend pricing logic, dataset artifact, filtered CSV, API file, or frontend file.
- Report-ready caption: Black-Scholes and Monte Carlo prices stay closely aligned across the benchmark cases, with the Monte Carlo series moving closer to the analytical reference at larger simulation counts. The figure serves as a concise milestone visual for cross-checking benchmark pricing consistency case by case.
