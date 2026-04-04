# Phase 7 Report Notes

## Dataset

Use the filtered milestone-only CE subset as raw-data support only. It is appropriate to describe it as a traceable, smaller documentation artifact derived from the larger raw dataset and useful for showing example rows or screenshot evidence.

Safe wording:
- The filtered milestone-only CE subset provides raw-data support for the milestone documentation.
- The raw dataset and filtered subset screenshots help demonstrate traceability from the original options data to the curated milestone evidence lane.
- The filtered subset is useful for showing example option rows and retained identifiers in a compact form.

Unsafe claims to avoid:
- Do not say the filtered CSV validates Black-Scholes or Monte Carlo pricing accuracy.
- Do not say the filtered CSV proves market prices match either model.
- Do not say the filtered subset generated the benchmark comparison values in the benchmark CSV.

## Benchmark Method

The benchmark lane is the source of method-comparison evidence for this milestone. It uses the verified `backend/app/benchmark_results.csv` artifact plus the phase 5 graphs and phase 6 benchmark table to compare Black-Scholes and Monte Carlo outputs under controlled benchmark inputs.

Safe wording:
- The benchmark method compares analytical Black-Scholes pricing with Monte Carlo pricing across fixed benchmark cases.
- The benchmark CSV, graphs, and benchmark table form the method-comparison evidence lane for this milestone.
- The compare-screen screenshots should be described as UI views of the locked benchmark cases, not as live market validation.

Unsafe claims to avoid:
- Do not describe the benchmark lane as proof of real-market fit.
- Do not say the benchmark results confirm tradable prices or execution quality.
- Do not combine the filtered subset and benchmark lane into a claim of end-to-end market validation.

## Results Summary

Use the benchmark results to summarize convergence and comparison behavior only. The strongest safe summary is that higher simulation counts in the benchmark lane generally reduce the gap between Monte Carlo and the Black-Scholes reference, while runtime generally increases as `N` rises.

Safe wording:
- In the benchmark lane, Monte Carlo absolute error generally decreases as the simulation count increases.
- The best absolute-error benchmark case is `OTM`, `N=100000`, with `absolute_error=0.000388`.
- The worst absolute-error benchmark case is `ATM`, `N=1000`, with `absolute_error=0.538604`.
- The fastest Monte Carlo benchmark case is `ATM`, `N=1000`, at `0.094 ms`, and the slowest is `OTM`, `N=100000`, at `2.0775 ms`.

Unsafe claims to avoid:
- Do not say the best benchmark case is the most realistic market case.
- Do not say the worst benchmark case means the model fails in live markets.
- Do not turn benchmark comparisons into claims about production trading performance.

## Graph Notes

Use the phase 5 graphs as visual summaries of the benchmark lane only. They are appropriate for showing runtime scaling, absolute-error behavior, and side-by-side price comparison across the locked benchmark cases.

Safe wording:
- The runtime graph shows how Monte Carlo runtime changes as the simulation count increases across the benchmark cases.
- The absolute-error graph shows how the Monte Carlo estimate moves closer to the Black-Scholes reference as `N` increases in the benchmark lane.
- The price comparison graph shows that the analytical and simulation outputs stay close across the exported benchmark cases.

Unsafe claims to avoid:
- Do not describe the graphs as evidence of market-price prediction accuracy.
- Do not say the graphs validate the filtered CSV against model outputs.
- Do not present the graphs as live-user or live-market screenshots.

## Limitations

Keep the limitations section explicit and practical. The filtered CSV supports documentation traceability only, while the benchmark lane supports controlled method comparison only.

Safe wording:
- The filtered subset is for raw-data support and screenshot traceability, not for market-vs-model validation.
- The benchmark evidence is limited to controlled benchmark cases captured in `backend/app/benchmark_results.csv`.
- The milestone does not establish that either pricing method matches live market prices for the raw dataset rows shown in the screenshots.
- The report should keep the raw-data support lane and the benchmark comparison lane clearly separated.

Unsafe claims to avoid:
- Do not claim validated market pricing from the raw dataset screenshots.
- Do not claim that matching benchmark-method outputs imply live-market accuracy.
- Do not imply that the milestone proves deployment readiness for trading decisions.
