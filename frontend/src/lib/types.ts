export type SubmissionMode = "black-scholes" | "monte-carlo" | "compare";

export interface FormValues {
  S: string;
  K: string;
  T: string;
  r: string;
  sigma: string;
  N: string;
  seed: string;
}

export type FieldName = keyof FormValues;
export type FieldErrors = Partial<Record<FieldName, string>>;

export interface PricingPayload {
  S: number;
  K: number;
  T: number;
  r: number;
  sigma: number;
  N: number;
  seed?: number;
}

export interface PricingResult {
  method: string;
  price: number;
  display_price: number;
  runtime_ms: number;
  inputs: Record<string, number | null>;
}

export interface CompareResult {
  black_scholes: PricingResult;
  monte_carlo: PricingResult;
  absolute_error: number;
}

export interface UiResult {
  mode: SubmissionMode;
  blackScholes?: PricingResult;
  monteCarlo?: PricingResult;
  absoluteError?: number;
  request: {
    N: number;
    seed: number | null;
  };
}

export interface StatusState {
  kind: "idle" | "loading" | "success" | "error";
  message?: string;
}

export interface PresetCase {
  id: string;
  label: string;
  description: string;
  values: FormValues;
}
