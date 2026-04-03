import type { FieldErrors, FormValues, PricingPayload } from "@/lib/types";

interface ValidationResult {
  errors: FieldErrors;
  payload: PricingPayload | null;
}

function parseRequiredNumber(value: string): number | null {
  const parsed = Number(value.trim());
  if (!Number.isFinite(parsed)) {
    return null;
  }

  return parsed;
}

function parsePositiveNumber(value: string): number | null {
  const parsed = parseRequiredNumber(value);
  if (parsed === null || parsed <= 0) {
    return null;
  }

  return parsed;
}

function parsePositiveInteger(value: string): number | null {
  const parsed = parseRequiredNumber(value);
  if (parsed === null || !Number.isInteger(parsed) || parsed <= 0) {
    return null;
  }

  return parsed;
}

function parseOptionalInteger(value: string): number | undefined | null {
  const trimmed = value.trim();
  if (!trimmed) {
    return undefined;
  }

  const parsed = Number(trimmed);
  if (!Number.isInteger(parsed)) {
    return null;
  }

  return parsed;
}

export function validateForm(values: FormValues): ValidationResult {
  const errors: FieldErrors = {};

  const S = parsePositiveNumber(values.S);
  if (S === null) {
    errors.S = "Enter a positive stock price.";
  }

  const K = parsePositiveNumber(values.K);
  if (K === null) {
    errors.K = "Enter a positive strike price.";
  }

  const T = parsePositiveNumber(values.T);
  if (T === null) {
    errors.T = "Enter a positive time to maturity.";
  }

  const r = parseRequiredNumber(values.r);
  if (r === null) {
    errors.r = "Enter the risk-free rate as a number such as 0.05.";
  }

  const sigma = parsePositiveNumber(values.sigma);
  if (sigma === null) {
    errors.sigma = "Enter a positive volatility value such as 0.2.";
  }

  const N = parsePositiveInteger(values.N);
  if (N === null) {
    errors.N = "Enter a positive integer simulation count.";
  }

  const seed = parseOptionalInteger(values.seed);
  if (seed === null) {
    errors.seed = "Seed must be a whole number or left blank.";
  }

  if (Object.keys(errors).length > 0) {
    return {
      errors,
      payload: null,
    };
  }

  return {
    errors: {},
    payload: {
      S: S as number,
      K: K as number,
      T: T as number,
      r: r as number,
      sigma: sigma as number,
      N: N as number,
      ...(seed !== undefined ? { seed } : {}),
    },
  };
}
