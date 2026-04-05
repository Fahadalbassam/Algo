# SPY options project dataset

## Purpose

This document describes the reproducible preprocessing step that produces `data/processed/spy_options_project_dataset.csv` for the option-pricing app. The pipeline is implemented in `scripts/prepare_spy_project_dataset.py` and does **not** rely on hand-editing rows.

## Source

- **Options:** `data/milestone/option_SPY_dataset_combined.csv`
- **Risk-free rate:** [FRED series DGS3MO](https://fred.stlouisfed.org/series/DGS3MO) (3-Month Treasury Constant Maturity, daily, percent per annum), downloaded from  
  `https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS3MO`  
  and cached in-repo at `data/raw/fred_dgs3mo.csv` for reproducibility.

## Why DGS3MO is joined

The milestone file supplies spot (`underlying`), strike, time to expiry, implied volatility, and market price, but not a risk-free rate. For Black–Scholes and Monte Carlo inputs, we need a short-term Treasury yield as a standard proxy for **r**. DGS3MO is joined **by quote date** using the latest FRED observation on or before that date (`pandas.merge_asof` with backward direction), so non-trading days on the options side still get the most recent published rate.

## Output columns

| Column | Meaning |
|--------|---------|
| `quote_date` | Option quote date (from `dt`) |
| `expiry_date` | Option expiry date (from `expr`) |
| `option_type` | Always `call` for this extract |
| `S` | Underlying price (from `underlying`) |
| `K` | Strike (from `strike`) |
| `T` | Time to expiry in years: `daysToExpiration / 365.0` |
| `r` | Risk-free rate as decimal: FRED DGS3MO ÷ 100 |
| `sigma` | Implied volatility (from `iv`) |
| `market_option_price` | Mid/mark price (from `mark`) |
| `bid` | Bid (from `bid`) |
| `ask` | Ask (from `ask`) |
| `open_interest` | Open interest (from `openInterest`) |

Columns such as `bs`, `theoreticalOptionValue`, and `theoreticalVolatility` from the source file are **not** copied into this dataset and are not used as model inputs or targets; the app computes theory paths internally.

## Running the pipeline

From the repository root (with `pandas` installed):

```bash
python scripts/prepare_spy_project_dataset.py
```

Use `--refresh-fred` to force a new download of the FRED series.

## Row filters

Rows are kept only when: `S`, `K`, `T`, `sigma`, and `market_option_price` are strictly positive; `open_interest`, `bid`, and `ask` are non-negative; and `r` is present after the FRED join.
