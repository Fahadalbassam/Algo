# European option pricing: Black–Scholes vs Monte Carlo

Course team project: compare two approaches to pricing **European call options** under shared inputs, with a small FastAPI service, a Next.js UI, tests, a reproducible benchmark export, and dataset pipelines for coursework and future analysis.

## Overview

The app lets you enter spot, strike, time to maturity, risk-free rate, volatility, and (for Monte Carlo) path count and optional seed. It returns prices and timings so you can contrast a **closed-form Black–Scholes** price with a **Monte Carlo** estimate and see how accuracy and runtime behave as you change simulation count.

**Problem:** Analytical formulas are fast and exact under model assumptions; simulation is flexible and intuitive but noisy and more expensive. Comparing both on the **same parameters** makes the tradeoff concrete.

**Why these two:** Black–Scholes is the standard analytical baseline for European calls in the Black–Scholes world. Monte Carlo estimates the same quantity by averaging discounted payoffs over simulated paths. Side-by-side output highlights **convergence** toward the analytical value as `N` grows and the **runtime cost** of doing so.

**Scope today:** European **call** options only (see API contract and backend models).

## Tech stack

| Layer | Stack |
|--------|--------|
| Backend | Python, FastAPI |
| Frontend | Next.js (App Router), TypeScript |
| Quality | `pytest`, API tests |
| Benchmarks | `backend/app/benchmark.py` → `backend/app/benchmark_results.csv` |
| Plots | `scripts/generate_phase5_benchmark_graphs.py` → PNGs in `docs/evidence/` |
| Data | Scripts under `scripts/`; SPY pipeline documented in `docs/data/spy_project_dataset.md` |

## Current status (milestone 2)

- **Milestone 2:** Delivered — working backend, working frontend compare flow, benchmark CSV export, evidence plots, and a reproducible processed SPY options pipeline (FRED-backed `r`).
- **Working:** Health check, pricing endpoints, compare endpoint, backend tests, benchmark runner.
- **Still in progress:** Deeper final analysis, richer dataset-backed experiments, and course report polish (see [Roadmap](#roadmap)).

This is a **development / coursework** project, not a production trading system.

## End product vision

- Users enter option parameters and run **Black–Scholes**, **Monte Carlo**, or **compare** in one place.
- The UI shows **prices**, **runtimes**, and (on compare) **absolute error** between methods under those inputs.
- **Controlled benchmarks** document behavior on a fixed grid (ITM / ATM / OTM × several `N` values) in `benchmark_results.csv` and the plots under `docs/evidence/`.
- **Later milestones** extend written analysis and optional market-facing evaluation using curated datasets, without mixing “documentation subset” and “fixed benchmark grid” claims (see limitations below).

## Repository layout

```
backend/          FastAPI app, pricing logic, tests, benchmark export
frontend/       Next.js UI and API routes that proxy to the backend
docs/           API contract, examples, team notes, data/evidence docs
scripts/        Dataset and benchmark plot utilities
data/           Processed/milestone artifacts (large raw files often gitignored)
```

Handy references: [`docs/api_contract.md`](docs/api_contract.md), [`docs/example_test_cases.md`](docs/example_test_cases.md), [`docs/team/TEAM_BASELINE.md`](docs/team/TEAM_BASELINE.md).

## Setup and run

### Backend

From `backend/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API base URL defaults to `http://127.0.0.1:8000`. More detail: [`backend/README.md`](backend/README.md).

### Frontend

From `frontend/`:

```powershell
npm install
npm run dev
```

Optional: copy `frontend/.env.example` to `frontend/.env.local` and set `BACKEND_API_BASE_URL` if the API is not on `http://127.0.0.1:8000`.

### Run tests

From `backend/` with the virtual environment active:

```powershell
pytest
```

### Run the benchmark export

From `backend/` (writes `backend/app/benchmark_results.csv`):

```powershell
python -m app.benchmark
```

Coordinate with the team before committing a regenerated CSV ([`docs/team/TEAM_BASELINE.md`](docs/team/TEAM_BASELINE.md)).

### Regenerate benchmark plots

From the **repository root** (requires matplotlib; reads only `backend/app/benchmark_results.csv`):

```powershell
python scripts/generate_phase5_benchmark_graphs.py
```

Outputs: `docs/evidence/phase5_runtime_vs_n.png`, `phase5_abs_error_vs_n.png`, `phase5_price_comparison.png`.

### SPY processed dataset

Reproducible pipeline (options file + FRED DGS3MO for risk-free rate) is documented in [`docs/data/spy_project_dataset.md`](docs/data/spy_project_dataset.md). From the repo root:

```powershell
python scripts/prepare_spy_project_dataset.py
```

Use `--refresh-fred` to force re-downloading the Treasury series.

## Dataset notes

- **NSE milestone subset:** `data/milestone/nse_options_2024-11-03_normalized_ce_milestone_subset.csv` is a filtered **call-option** extract for traceability and documentation. It is **not** sufficient for full model-vs-market pricing without extra fields; see [`docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_decision.md`](docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_decision.md) and [`docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_limitations.md`](docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_limitations.md).
- **SPY project dataset:** Enriched options rows with **`r`** from **FRED DGS3MO** (joined by quote date). Details: [`docs/data/spy_project_dataset.md`](docs/data/spy_project_dataset.md).
- **Benchmark CSV:** `backend/app/benchmark_results.csv` summarizes **Black–Scholes vs Monte Carlo** on a **fixed parameter grid**. It supports method comparison and coursework figures; it does **not** by itself validate live market prices.

## API summary

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/health` | Liveness check (`{"status": "ok"}`) |
| `POST` | `/price/black-scholes` | Analytical European call price |
| `POST` | `/price/monte-carlo` | Monte Carlo estimate (`N`, optional `seed`) |
| `POST` | `/price/compare` | Both methods plus error metrics |

Full request/response shapes: [`docs/api_contract.md`](docs/api_contract.md).

## Roadmap

**Milestone 2 (done):** Implemented comparators, stable API contract, UI compare flow, automated tests, benchmark export, plot script, milestone NSE subset documentation, SPY+FRED preprocessing path.

**Later / final:** Stronger written analysis, optional dataset-driven case studies, any additional validation story the course requires—using artifacts and limitations spelled out in `docs/data/` and team notes.

## Team

Roles and integration baseline: [`docs/team/`](docs/team/) (see `TEAM_BASELINE.md` and individual profiles).
