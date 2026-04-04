# NSE Options CE Milestone Subset Decision Memo

## Scope

- Source file name: `nse_options_2024-11-03_normalized.csv`
- This subset is milestone-only. It is not a final pricing-comparison dataset.
- The build uses the original source CSV only, preserves original source order, and does not modify backend, frontend, API contract files, or the original CSV.

## Locked Filter Rules

- `instrument_type == "OPTION"`
- `option_type == "CE"`
- `time_to_expiry_years > 0`
- `open_interest > 0`
- `close_price > 0`
- `strike_price > 0`

## Exact Output Schema

```text
source_row_id,raw_ticker,exchange,underlying_symbol,option_type,expiry_date,strike_price,quote_date,quote_time,quote_datetime,days_to_expiry,time_to_expiry_years,market_option_price,volume,open_interest,open_interest_overflow_flag
```

## Row Counts

- Rows before filtering: `1048575`
- Rows after filtering: `373234`

## Kept Columns And Why

- `source_row_id`: preserves 1-based lineage to the original data-row position before filtering.
- `raw_ticker`, `exchange`, `underlying_symbol`: preserve instrument identity, venue, and underlying linkage.
- `option_type`: keeps the exported subset explicit about the retained CE contract type.
- `expiry_date`, `quote_date`, `quote_time`, `quote_datetime`: preserve the quote/expiry timing context already present in the source.
- `strike_price`, `days_to_expiry`, `time_to_expiry_years`: keep strike and source-provided expiry horizon fields needed for the milestone subset.
- `market_option_price`: renames source `close_price` to make the retained observed option market price explicit.
- `volume`, `open_interest`, `open_interest_overflow_flag`: preserve basic trading-interest context and the source overflow indicator.

## Removed Columns And Why

- `instrument_type`: removed because the locked filter already fixes all kept rows to `OPTION`.
- `contract_series`: removed because it is blank in the kept source rows and is not part of the locked output schema.
- `expiry_code`: removed because `expiry_date` already carries the usable maturity date for the milestone subset.
- `open_price`, `high_price`, `low_price`: removed because this milestone subset keeps only the source `close_price`, renamed to `market_option_price`.

## Decision

This exported CE subset is approved only as a milestone artifact for downstream documentation and milestone checks. It must not be treated as the final dataset for pricing comparison claims.
