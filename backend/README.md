# Option Pricing Backend

This backend exposes option pricing APIs for European call options using Black–Scholes and Monte Carlo, plus a compare endpoint. For project context, setup from the repo root, dataset notes, and roadmap, see the **[root README](../README.md)**.

## Setup

1. Create a virtual environment:
  `python -m venv .venv`
2. Activate the virtual environment (PowerShell):
  `.\.venv\Scripts\Activate.ps1`
3. Install dependencies:
  `pip install -r requirements.txt`
4. Run the API:
  `uvicorn app.main:app --reload`

## Endpoints

- `GET /health`
- `POST /price/black-scholes`
- `POST /price/monte-carlo`
- `POST /price/compare`

## Sample Request Body: Black-Scholes

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2
}
```

## Sample Request Body: Monte Carlo

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
