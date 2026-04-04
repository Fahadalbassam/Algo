# Phase 8 Report Shell

## Introduction

This milestone report documents a controlled evidence package for an option-pricing comparison project. Keep the introduction focused on two separate evidence lanes: raw-data support artifacts for traceability and benchmark-method comparison artifacts for controlled method comparison.

## Project Objective

State that the project objective is to document the data-preparation path and compare Black-Scholes and Monte Carlo outputs across locked benchmark cases. Keep the objective limited to milestone documentation, reproducible evidence, and controlled comparison rather than live-market validation.

## Dataset

Describe `data/milestone/nse_options_2024-11-03_normalized_ce_milestone_subset.csv` as a filtered CE milestone subset derived from the original normalized source file. Cite `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_decision.md` and `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_limitations.md`, and state clearly that this filtered CSV is a raw-data support artifact only.

## Data Preparation

Summarize the locked milestone filtering rules at a high level: retained option rows are CE contracts with positive expiry horizon, open interest, close price, and strike price. Use this section to note traceability and filtering discipline only, and do not turn the filtered CSV into market-vs-model validation evidence.

## Algorithms Used

Describe Black-Scholes as the analytical reference method and Monte Carlo as the simulation-based comparison method used in the benchmark lane. Keep this section at the method-description level and avoid implying that the filtered subset itself validates either method against market prices.

## Benchmark Method

Explain that `backend/app/benchmark_results.csv` is the locked benchmark-method comparison artifact for this milestone. Reference `docs/evidence/phase5_runtime_vs_n.png`, `docs/evidence/phase5_abs_error_vs_n.png`, `docs/evidence/phase5_price_comparison.png`, `docs/evidence/phase5_graph_notes.md`, and `docs/evidence/phase6_benchmark_table.md` as derived benchmark evidence used to compare method outputs across fixed benchmark cases.

## Results

Summarize only the benchmark lane here. Safe fill-ready points include that Monte Carlo runtime generally increases as `N` rises, absolute error generally decreases as `N` rises, the best absolute-error case in `docs/evidence/phase6_benchmark_table.md` is `OTM`, `N=100000`, and the worst absolute-error case is `ATM`, `N=1000`.

## Graph Discussion

Use `docs/evidence/phase5_runtime_vs_n.png` to discuss runtime scaling, `docs/evidence/phase5_abs_error_vs_n.png` to discuss absolute-error behavior, and `docs/evidence/phase5_price_comparison.png` plus `docs/evidence/phase5_graph_notes.md` to discuss side-by-side benchmark outputs. Keep every graph statement tied to benchmark behavior only.

## Screenshots and Evidence

Reference `docs/evidence/phase7_screenshot_checklist.md` for the planned screenshot set and keep the evidence lanes separate in the wording. The dataset screenshots should be described as raw-data support and traceability views, while compare-screen screenshots should be described as views of locked benchmark cases rather than live-market validation.

## Limitations

State explicitly that the filtered CE subset is not sufficient for market-vs-model validation, as documented in `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_limitations.md`. Also state that the benchmark lane supports controlled method comparison only and does not establish live-market fit, trading readiness, or deployment readiness.

## Conclusion

Conclude that the milestone delivers a traceable raw-data support lane plus a reproducible benchmark-method comparison lane. Do not conclude that the filtered CSV validates model prices against live market observations.

## Appendix / Artifacts

- Raw-data support artifacts: `data/milestone/nse_options_2024-11-03_normalized_ce_milestone_subset.csv`, `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_decision.md`, `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_limitations.md`
- Benchmark-method comparison artifacts: `backend/app/benchmark_results.csv`, `docs/evidence/phase5_runtime_vs_n.png`, `docs/evidence/phase5_abs_error_vs_n.png`, `docs/evidence/phase5_price_comparison.png`, `docs/evidence/phase5_graph_notes.md`, `docs/evidence/phase6_benchmark_table.md`
- Assembly and QA artifacts: `docs/evidence/phase7_screenshot_checklist.md`, `docs/evidence/phase7_report_notes.md`, `docs/evidence/phase8_final_qa_checklist.md`, `docs/evidence/phase8_report_shell.md`
