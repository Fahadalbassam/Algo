# API contract (backend)

Source of truth: `backend/app/main.py` and `backend/app/models.py`.

## Endpoints

| Method | Path | Request body | Response |
|--------|------|--------------|----------|
| GET | `/health` | — | `{"status": "ok"}` |
| POST | `/price/black-scholes` | `OptionInput` | `PricingResult` |
| POST | `/price/monte-carlo` | `MonteCarloInput` | `PricingResult` |
| POST | `/price/compare` | `MonteCarloInput` | `CompareResult` |

## Request fields

**OptionInput** (Black-Scholes):

- `S` (number, must be positive): spot
- `K` (number, must be positive): strike
- `T` (number, must be positive): time to maturity (years)
- `r` (number): risk-free rate (decimal, e.g. `0.05`)
- `sigma` (number, must be positive): volatility (decimal)

**MonteCarloInput** extends OptionInput with:

- `N` (integer, must be positive): number of paths/simulations
- `seed` (integer or `null`, optional): reproducibility; omit or `null` for non-fixed RNG

## Response shapes

**PricingResult**:

- `method` (string)
- `price`, `display_price`, `runtime_ms` (numbers)
- `inputs` (object): echoed request fields

**CompareResult**:

- `black_scholes`: `PricingResult`
- `monte_carlo`: `PricingResult`
- `absolute_error` (number)

Invalid payloads return HTTP `422` with validation detail from FastAPI/Pydantic.
