# NSE Options CE Milestone Subset Limitations

- Missing `S`, `r`, and `sigma`: the subset does not contain spot price, risk-free rate, or volatility inputs required for a full pricing comparison.
- No final pricing-comparison claim allowed: this artifact is milestone-only and is not sufficient for a final market-vs-model evaluation.
- Likely truncation/completeness risk: the source file contains exactly `1048575` data rows before filtering, which is consistent with a common spreadsheet row cap, so completeness is not guaranteed.
- Filename date vs quote-date mismatch: the source filename contains `2024-11-03`, while the retained rows use `quote_date = 10/31/2024`.
- No implied-volatility or fair-value claims allowed: the subset does not support IV estimation or fair-value assertions on its own.
- No market-vs-model error claims allowed: without `S`, `r`, and `sigma`, the subset cannot support error metrics against any pricing model.
