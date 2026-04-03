# Nawaf

## Name

Nawaf

## Role

Dataset owner.

## Owns

- Cleaned dataset artifacts (subsets, derived columns)
- Mapping specification (CSV columns → API inputs)
- Example cases for docs and manual testing

## Current status

Local normalized options file exists but is **not** final for pricing API use: needs enrichment and product alignment (calls vs puts).

## Done

- (Team fills in, e.g. initial normalization pipeline or column naming.)

## In progress

- Defining how market data maps to `S`, `K`, `T`, `r`, `sigma`.

## Blocked by

- Decisions on risk-free source and spot timestamp alignment (quote vs underlying close).

## Next tasks

- Map **`strike_price` → `K`**.
- Map **`time_to_expiry_years` → `T`** (confirm convention vs `days_to_expiry`).
- Define **source and derivation** for **`S`** (spot by underlying + time).
- Define **source** for **`r`** (curve or flat rate + currency/market).
- Define **`sigma`** (implied from option price vs external IV surface).
- Clarify **call subset** vs **put** rows; API currently models **European call** only — document put handling or filter to calls for examples.
- Deliver **example_cases** (small JSON list) and a **small cleaned subset** for the team (not the full raw file).

## Main files / folders

- Local: `nse_options_2024-11-03_normalized.csv` (**gitignored** — do not commit)
- `docs/example_test_cases.md` (coordinate updates when examples are ready)

## Notes

The large raw/normalized CSV stays **local** and **gitignored**. Share small excerpts, mapping docs, and agreed example payloads instead.

## Handoffs needed

- To **Fahad** / team: written mapping spec + sample rows before any automated ingestion.
- To **Waleed**: table of example cases and data lineage notes for the report.
