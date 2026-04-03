# API Contract

This document describes the current backend API contract.

Backend is the source of truth for input/output naming. If this document and backend behavior ever differ, follow the backend implementation.

## GET /health

Purpose: simple service health check.

Response example:

```json
{
  "status": "ok"
}
```

## POST /price/black-scholes

Request body:

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2
}
```

Response example:

```json
{
  "method": "black_scholes",
  "price": 13.3465,
  "display_price": 13.35,
  "runtime_ms": 0.21,
  "inputs": {
    "S": 100,
    "K": 95,
    "T": 1,
    "r": 0.05,
    "sigma": 0.2
  }
}
```

## POST /price/monte-carlo

Request body:

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2,
  "N": 10000,
  "seed": 42
}
```

Response example:

```json
{
  "method": "monte_carlo",
  "price": 13.241,
  "display_price": 13.24,
  "runtime_ms": 1.15,
  "inputs": {
    "S": 100,
    "K": 95,
    "T": 1,
    "r": 0.05,
    "sigma": 0.2,
    "N": 10000,
    "seed": 42
  }
}
```

## POST /price/compare

Request body:

```json
{
  "S": 100,
  "K": 95,
  "T": 1,
  "r": 0.05,
  "sigma": 0.2,
  "N": 10000,
  "seed": 42
}
```

Response example:

```json
{
  "black_scholes": {
    "method": "black_scholes",
    "price": 13.3465,
    "display_price": 13.35,
    "runtime_ms": 0.2,
    "inputs": {
      "S": 100,
      "K": 95,
      "T": 1,
      "r": 0.05,
      "sigma": 0.2,
      "N": 10000,
      "seed": 42
    }
  },
  "monte_carlo": {
    "method": "monte_carlo",
    "price": 13.241,
    "display_price": 13.24,
    "runtime_ms": 1.1,
    "inputs": {
      "S": 100,
      "K": 95,
      "T": 1,
      "r": 0.05,
      "sigma": 0.2,
      "N": 10000,
      "seed": 42
    }
  },
  "absolute_error": 0.1055
}
```
