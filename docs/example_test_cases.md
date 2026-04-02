# Example Test Cases

Short, practical request examples for teammate testing.

## 1. In-the-Money Call

Label: ITM baseline

Request JSON:

```json
{
  "S": 120,
  "K": 100,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2,
  "N": 10000,
  "seed": 42
}
```

Use with endpoint(s):
- `POST /price/black-scholes` (use fields `S`, `K`, `T`, `r`, `sigma`)
- `POST /price/monte-carlo`
- `POST /price/compare`

## 2. Near At-the-Money Call

Label: ATM-ish reference

Request JSON:

```json
{
  "S": 100,
  "K": 100,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2,
  "N": 10000,
  "seed": 42
}
```

Use with endpoint(s):
- `POST /price/black-scholes` (use fields `S`, `K`, `T`, `r`, `sigma`)
- `POST /price/monte-carlo`
- `POST /price/compare`

## 3. Out-of-the-Money Call

Label: OTM stress case

Request JSON:

```json
{
  "S": 90,
  "K": 110,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2,
  "N": 10000,
  "seed": 42
}
```

Use with endpoint(s):
- `POST /price/black-scholes` (use fields `S`, `K`, `T`, `r`, `sigma`)
- `POST /price/monte-carlo`
- `POST /price/compare`
