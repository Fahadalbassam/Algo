# Obai

## Name

Obai

## Role

Monte Carlo owner; benchmark owner.

## Owns

- `backend/app/monte_carlo.py`
- `backend/app/benchmark.py`
- Runtime measurement and error comparison in benchmark rows (separate from API responses)

## Current status

Benchmark lane runs; core MC path aligned with team contract.

## Done

- (Team fills in, e.g. benchmark grid, CSV export, timing fixes.)

## In progress

- (Optional) richer benchmark tables or reporting.

## Blocked by

- None unless benchmark needs agreed golden files or paths from Fahad.

## Next tasks

- Improve benchmarks and report outputs (tables, labels, exports) **without** changing `monte_carlo_call` to return anything other than **`float`**.
- Keep timing and extra fields in `benchmark.py` (or helpers), not inside `monte_carlo_call`.

## Main files / folders

- `backend/app/monte_carlo.py`
- `backend/app/benchmark.py`
- `backend/app/benchmark_results.csv` (generated or curated; do not commit casual regenerations)

## Notes

**Rule:** `monte_carlo_call(...)` must remain **`-> float`**. Structured responses belong in the API layer (`build_result` in `utils.py`), not in the core pricer.

## Handoffs needed

- To **Alwaleed**: stable benchmark commands and example rows or CSV paths for the report.
- To **Fahad**: heads-up if benchmark artifacts or locations change in a way that affects CI or docs.
