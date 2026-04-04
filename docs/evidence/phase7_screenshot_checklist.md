# Phase 7 Screenshot Checklist

This checklist defines the four milestone-safe screenshots to capture later. These screenshots support raw-data traceability and benchmark-method comparison evidence only; they must not be presented as market-vs-model validation.

- [ ] Raw dataset screenshot
  Exact file or screen source: `nse_options_2024-11-03_normalized.csv`
  Exact values/rows to use: `contract_id=AARTIIND26DEC24600CE.NFO` with `quote_time` values `9:19:59`, `11:50:59`, `13:12:59`, and `14:09:59`
  Exactly what to capture: A single spreadsheet or table view showing the matching raw dataset rows for that contract and those four quote times, with the contract identifier and quote-time cells clearly visible.
  Why it matters: It provides milestone-safe traceability to the raw source data used for dataset support and shows that the selected option contract appears at multiple times in the original dataset.

- [ ] Filtered subset screenshot
  Exact file or screen source: `data/milestone/nse_options_2024-11-03_normalized_ce_milestone_subset.csv`
  Exact values/rows to use: `source_row_id` values `11`, `12`, `13`, and `14`
  Exactly what to capture: A single spreadsheet or table view showing the four filtered subset rows with `source_row_id` visible, so the retained rows can be matched back to the raw-data support lane.
  Why it matters: It demonstrates that the milestone subset preserves a traceable slice of the raw options data for documentation support, without implying that the filtered CSV itself proves pricing accuracy.

- [ ] Best-case compare screenshot
  Exact file or screen source: Frontend compare screen
  Exact values/rows to use: `S=100`, `K=110`, `T=1`, `r=0.05`, `sigma=0.2`, `N=100000`, `seed=42`
  Exactly what to capture: The compare screen after entering the locked best-case benchmark inputs and running the comparison, with both the Black-Scholes and Monte Carlo outputs visible on the same screen.
  Why it matters: It captures the benchmark lane's best absolute-error comparison case in a user-facing format and supports the method-comparison evidence already summarized in the benchmark table.

- [ ] Worst-case compare screenshot
  Exact file or screen source: Frontend compare screen
  Exact values/rows to use: `S=100`, `K=100`, `T=1`, `r=0.05`, `sigma=0.2`, `N=1000`, `seed=42`
  Exactly what to capture: The compare screen after entering the locked worst-case benchmark inputs and running the comparison, with both the Black-Scholes and Monte Carlo outputs visible on the same screen.
  Why it matters: It captures the benchmark lane's worst absolute-error comparison case in a user-facing format and shows the contrast with the best-case benchmark result without making any market-vs-model claim.
