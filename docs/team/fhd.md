# Fahad

## Name

Fahad

## Role

Project lead; backend owner; integration owner.

## Owns

- Backend structure and layout
- API contract (endpoints, JSON shape, field names)
- Final merge decisions and branch safety

## Current status

Integration baseline tracked on branch **`fhd`**. Core pricing functions return floats; API layer returns structured JSON.

## Done

- (Team fills in as milestones land on `fhd`.)

## In progress

- Maintaining `fhd` as the shared integration baseline.

## Blocked by

- None recorded here unless a dependency appears (e.g. unresolved API vs dataset decisions).

## Next tasks

- Push or publish the baseline so the team can branch from it.
- Guard the API contract on review (no casual renames or shape changes).
- Validate incoming merges against tests and live endpoint checks.
- Coordinate dataset schema validation with Nawaf when ingestion is in scope.

## Main files / folders

- `backend/app/main.py`
- `backend/app/models.py`
- `backend/app/utils.py`
- `backend/app/black_scholes.py`
- `docs/api_contract.md`

## Notes

- Source of truth for HTTP behavior is the backend implementation; keep `docs/api_contract.md` aligned when behavior changes intentionally.

## Handoffs needed

- From **Obai**: benchmark output conventions if reports depend on CSV columns or paths.
- From **Nawaf**: finalized mapping spec before any dataset-driven API or examples ship.
- From **Rayan**: any proxy/env (`BACKEND_API_BASE_URL`) issues found during smoke tests.
