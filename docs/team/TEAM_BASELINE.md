# Team baseline

## Project summary

European option pricing stack: FastAPI backend (Black–Scholes + Monte Carlo), Next.js frontend with a pricing workbench, and optional benchmark/reporting scripts. Core math returns plain floats; HTTP responses are structured JSON.

## Integration branch

Current stable integration baseline: **`fhd`**. Treat this branch as the shared checkpoint before promoting to `main`.

## Backend / API contract (source of truth)

- `black_scholes_call(...)` → **`float`**
- `monte_carlo_call(...)` → **`float`**
- API handlers build structured JSON (`method`, `price`, `display_price`, `runtime_ms`, `inputs`; compare adds nested results + `absolute_error`)

## Official endpoints and field names

**Endpoints**

- `GET /health`
- `POST /price/black-scholes`
- `POST /price/monte-carlo`
- `POST /price/compare`

**Request / echo field names (do not rename casually)**

- `S`, `K`, `T`, `r`, `sigma`
- `N`, `seed` (Monte Carlo / compare only)

## Current validation status

- Backend tests: **8 passing** (`pytest` in `backend`)
- `python -m app.benchmark` from `backend`: **works**
- Frontend contract vs API: **stable** (no drift assumed on `fhd`)

## Do not commit casually

- Large local normalized options CSV (gitignored; e.g. `nse_options_2024-11-03_normalized.csv`)
- Regenerated `backend/app/benchmark_results.csv` unless the team explicitly refreshes that artifact
- `package-lock.json` changes that are only OS/npm drift with no `package.json` change

## Next team priorities

| Owner | Focus |
|--------|--------|
| **Fahad** | Integration baseline, merge safety, API contract as source of truth |
| **Obai** | Benchmark / report improvements **without** changing `monte_carlo_call` return type (`float`) |
| **Rayan** | Frontend smoke tests; black-scholes, monte-carlo, compare flows vs live API |
| **Nawaf** | Dataset mapping and enrichment for `S`, `r`, `sigma`; call subset vs put handling |
| **Alwaleed** | Report evidence, screenshots, QA, presentation-ready outputs |

## Merge rules

1. **Do not change the API contract** (paths, response shape, field names) without team agreement and doc updates.
2. Use **`fhd` as the integration baseline** before merging to `main`.
3. **Run tests** (backend pytest; frontend/build as agreed) before merging integration work.
