# Example test payloads

Minimal JSON bodies aligned with `backend/tests/test_api.py` and `docs/api_contract.md`.

## Black-Scholes (valid)

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2
}
```

## Black-Scholes (invalid `sigma`)

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0
}
```

Expect `422`.

## Monte Carlo / Compare (valid)

Same body for `POST /price/monte-carlo` and `POST /price/compare`:

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2,
  "N": 10000,
  "seed": 42
}
```

## Monte Carlo (invalid `N`)

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2,
  "N": 0,
  "seed": 42
}
```

Expect `422`.
