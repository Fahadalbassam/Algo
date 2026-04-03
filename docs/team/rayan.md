# Rayan

## Name

Rayan

## Role

Frontend owner.

## Owns

- Frontend UI and layout
- API calls and error handling
- Result display (single-method and compare)

## Current status

Frontend contract matches backend: same field names and endpoint semantics (via Next proxy to FastAPI).

## Done

- (Team fills in, e.g. workbench, presets, results panel.)

## In progress

- (Optional) UX polish or docs for local dev.

## Blocked by

- Backend not running locally (502 from proxy) — fix env or start FastAPI.

## Next tasks

- Smoke-test **black-scholes**, **monte-carlo**, and **compare** against the API on the current baseline (`fhd`).
- Confirm `BACKEND_API_BASE_URL` (default `http://127.0.0.1:8000`) in real environments.

## Main files / folders

- `frontend/src/lib/api.ts`
- `frontend/src/lib/types.ts`
- `frontend/src/lib/backend-proxy.ts`
- `frontend/src/components/pricing-workbench.tsx`
- `frontend/src/app/api/price/*/route.ts`

## Notes

**Do not change** backend endpoint path names or JSON field names (`S`, `K`, `T`, `r`, `sigma`, `N`, `seed`) unless the whole team updates the API contract and docs together.

## Handoffs needed

- To **Waleed**: screenshots or short clips of the three flows and compare output.
- To **Fahad**: any contract mismatch found during smoke tests (with request/response samples).
