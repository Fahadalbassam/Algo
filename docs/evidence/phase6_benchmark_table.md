# Phase 6 Benchmark Table

This table provides benchmark-method comparison evidence derived directly from the verified `backend/app/benchmark_results.csv` export. It summarizes all 15 benchmark cases across the ITM, ATM, and OTM scenarios without making any market-vs-model validation claim.

- Best absolute-error case: `OTM`, `N=100000`, `absolute_error=0.000388`, `relative_error=6.4e-05`
- Worst absolute-error case: `ATM`, `N=1000`, `absolute_error=0.538604`, `relative_error=0.051538`
- Fastest Monte Carlo case: `ATM`, `N=1000`, `monte_carlo_runtime_ms=0.094`
- Slowest Monte Carlo case: `OTM`, `N=100000`, `monte_carlo_runtime_ms=2.0775`

## How to read this table

Read each row as one exported benchmark case from the verified CSV: `label` identifies the scenario, `N` and `seed` identify the Monte Carlo run settings, the two price columns compare the analytical and simulation outputs, the runtime columns show method timing, and the error columns quantify the gap between the two pricing methods.

| label | S | K | T | r | sigma | N | seed | black_scholes_price | black_scholes_runtime_ms | monte_carlo_price | monte_carlo_runtime_ms | absolute_error | relative_error |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ITM | 100 | 95 | 1 | 0.05 | 0.2 | 1000 | 42 | 13.346464945879582 | 0.2874 | 12.820639539702782 | 0.1237 | 0.525825 | 0.039398 |
| ITM | 100 | 95 | 1 | 0.05 | 0.2 | 5000 | 42 | 13.346464945879582 | 0.1058 | 13.052862397725642 | 0.1629 | 0.293603 | 0.021999 |
| ITM | 100 | 95 | 1 | 0.05 | 0.2 | 10000 | 42 | 13.346464945879582 | 0.0886 | 13.23930937259921 | 0.2477 | 0.107156 | 0.008029 |
| ITM | 100 | 95 | 1 | 0.05 | 0.2 | 50000 | 42 | 13.346464945879582 | 0.0844 | 13.353402458871148 | 0.9685 | 0.006938 | 0.00052 |
| ITM | 100 | 95 | 1 | 0.05 | 0.2 | 100000 | 42 | 13.346464945879582 | 0.0976 | 13.3097791348107 | 2.0178 | 0.036686 | 0.002749 |
| ATM | 100 | 100 | 1 | 0.05 | 0.2 | 1000 | 42 | 10.450583572185565 | 0.1292 | 9.911979607280376 | 0.094 | 0.538604 | 0.051538 |
| ATM | 100 | 100 | 1 | 0.05 | 0.2 | 5000 | 42 | 10.450583572185565 | 0.0741 | 10.168919879680967 | 0.2315 | 0.281664 | 0.026952 |
| ATM | 100 | 100 | 1 | 0.05 | 0.2 | 10000 | 42 | 10.450583572185565 | 0.1332 | 10.345182037175293 | 0.2874 | 0.105402 | 0.010086 |
| ATM | 100 | 100 | 1 | 0.05 | 0.2 | 50000 | 42 | 10.450583572185565 | 0.0878 | 10.457691538845074 | 0.9415 | 0.007108 | 0.00068 |
| ATM | 100 | 100 | 1 | 0.05 | 0.2 | 100000 | 42 | 10.450583572185565 | 0.113 | 10.420541193153111 | 2.0134 | 0.030042 | 0.002875 |
| OTM | 100 | 110 | 1 | 0.05 | 0.2 | 1000 | 42 | 6.040088129724239 | 0.1519 | 5.5200914817839255 | 0.1045 | 0.519997 | 0.086091 |
| OTM | 100 | 110 | 1 | 0.05 | 0.2 | 5000 | 42 | 6.040088129724239 | 0.0781 | 5.787079621025758 | 0.1698 | 0.253009 | 0.041888 |
| OTM | 100 | 110 | 1 | 0.05 | 0.2 | 10000 | 42 | 6.040088129724239 | 0.0906 | 5.98238972647839 | 0.26 | 0.057698 | 0.009553 |
| OTM | 100 | 110 | 1 | 0.05 | 0.2 | 50000 | 42 | 6.040088129724239 | 0.0904 | 6.064207989130908 | 0.9579 | 0.02412 | 0.003993 |
| OTM | 100 | 110 | 1 | 0.05 | 0.2 | 100000 | 42 | 6.040088129724239 | 0.1254 | 6.039699893165324 | 2.0775 | 0.000388 | 6.4e-05 |
