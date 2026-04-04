# Phase 8 Final QA Checklist

## Dataset Evidence

- [ ] Confirm `data/milestone/nse_options_2024-11-03_normalized_ce_milestone_subset.csv` exists and is the filtered CE milestone subset artifact.
- [ ] Confirm `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_decision.md` exists and is the dataset decision reference.
- [ ] Confirm `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_limitations.md` exists and is the dataset limitations reference.
- [ ] Confirm the filtered CSV is treated as raw-data support only.
- [ ] Confirm no market-vs-model validation claim is made from the filtered CSV.

## Benchmark Evidence

- [ ] Confirm `backend/app/benchmark_results.csv` exists and is the locked benchmark artifact for this milestone.
- [ ] Confirm the benchmark lane is treated as method-comparison evidence.
- [ ] Confirm `docs/evidence/phase6_benchmark_table.md` is used only as benchmark-summary evidence derived from `backend/app/benchmark_results.csv`.
- [ ] Confirm any benchmark summary wording stays tied to exported benchmark cases and not to live-market validation.

## Graph Evidence

- [ ] Confirm `docs/evidence/phase5_runtime_vs_n.png` exists.
- [ ] Confirm `docs/evidence/phase5_abs_error_vs_n.png` exists.
- [ ] Confirm `docs/evidence/phase5_price_comparison.png` exists.
- [ ] Confirm `docs/evidence/phase5_graph_notes.md` exists.
- [ ] Confirm all graph discussion is framed as benchmark-lane behavior only.
- [ ] Confirm no graph text implies market-price prediction accuracy or filtered-CSV validation.

## Screenshot Evidence

- [ ] Confirm `docs/evidence/phase7_screenshot_checklist.md` exists and remains the capture guide.
- [ ] Confirm screenshot captions keep raw-data support views separate from benchmark comparison views.
- [ ] Confirm no screenshot wording describes compare-screen views as live market validation.

## Report Wording Safety

- [ ] Confirm the report clearly separates raw-data support artifacts from benchmark-method comparison artifacts.
- [ ] Confirm the filtered CSV is not presented as proof that Black-Scholes or Monte Carlo matches market prices.
- [ ] Confirm the benchmark lane is not presented as proof of tradable, deployment-ready, or live-market pricing performance.
- [ ] Confirm the report does not combine the filtered subset and benchmark outputs into an end-to-end market-validation claim.

## Reproducibility

- [ ] Confirm the report cites artifact files by exact file name where needed.
- [ ] Confirm the dataset discussion points back to the CE milestone subset CSV plus the decision and limitations docs.
- [ ] Confirm the benchmark discussion points back to `backend/app/benchmark_results.csv` plus the phase 5 and phase 6 evidence artifacts.
- [ ] Confirm no wording implies hidden preprocessing, changed pricing logic, or unlogged evidence generation.

## File Audit Trail

- [ ] Confirm phase 3 dataset artifacts exist: `data/milestone/nse_options_2024-11-03_normalized_ce_milestone_subset.csv`, `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_decision.md`, and `docs/data/nse_options_2024-11-03_normalized_ce_milestone_subset_limitations.md`.
- [ ] Confirm the benchmark export artifact exists: `backend/app/benchmark_results.csv`.
- [ ] Confirm phase 5 evidence artifacts exist: `docs/evidence/phase5_runtime_vs_n.png`, `docs/evidence/phase5_abs_error_vs_n.png`, `docs/evidence/phase5_price_comparison.png`, and `docs/evidence/phase5_graph_notes.md`.
- [ ] Confirm the phase 6 artifact exists: `docs/evidence/phase6_benchmark_table.md`.
- [ ] Confirm phase 7 artifacts exist: `docs/evidence/phase7_screenshot_checklist.md` and `docs/evidence/phase7_report_notes.md`.
- [ ] Confirm phase 8 artifacts exist: `docs/evidence/phase8_final_qa_checklist.md` and `docs/evidence/phase8_report_shell.md`.
- [ ] Confirm all required milestone files now exist.
- [ ] Confirm `alwaleed.md` has entries for each approved step, including phase 3, benchmark export patch, benchmark CSV regeneration, phase 5, phase 6, phase 7, and phase 8.

## Submission Readiness

- [ ] Confirm both phase 8 markdown files exist and are ready for handoff.
- [ ] Confirm the report shell can be filled without rewriting the evidence-safety boundaries.
- [ ] Confirm every referenced artifact name is spelled exactly as stored in the repository.
- [ ] Confirm no backend pricing logic, frontend files, API files, dataset files, filtered CSV files, or `benchmark.py` were modified in this step.
