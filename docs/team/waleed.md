# Waleed

## Name

Waleed

## Role

Report owner; QA owner.

## Owns

- Evidence pack (screenshots, tables)
- Report structure and presentation prep
- Light QA checklist against the agreed baseline

## Current status

Baseline on **`fhd`**: backend tests green, benchmark runnable, API contract stable for frontend.

## Done

- (Team fills in as report sections are drafted.)

## In progress

- (Optional) assembling setup and results sections from the current baseline.

## Blocked by

- Missing benchmark exports or final example cases from Obai / Nawaf if those are required for the report narrative.

## Next tasks

- Use the **current baseline** for environment setup and “how we run the stack” in the report.
- Request **benchmark outputs** from Obai (command + sample table or CSV excerpt, not necessarily committed files).
- Request **final example cases** from Nawaf once mapping is defined.
- Track **missing evidence** (e.g. compare screenshot, error-state screenshot, latency note) in a short checklist.

## Main files / folders

- `docs/team/TEAM_BASELINE.md` (reference for branch and contract)
- `docs/api_contract.md` (reference for JSON shapes)
- Obai/Nawaf deliverables (screenshots, tables — typically outside repo or in report assets)

## Notes

Prefer **reproducible** evidence: branch name, commit hash, and commands used to generate numbers or screenshots.

## Handoffs needed

- From **Rayan**: UI screenshots for BS / MC / compare flows.
- From **Obai**: benchmark summary table or agreed CSV snippet.
- From **Nawaf**: example JSON cases and mapping one-pager for the data section.
