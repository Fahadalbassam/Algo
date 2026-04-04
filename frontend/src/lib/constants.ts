import type { FieldName, FormValues, PresetCase } from "@/lib/types";

interface FieldDefinition {
  name: FieldName;
  label: string;
  helper: string;
  placeholder: string;
  inputMode: "decimal" | "numeric";
}

export const DEFAULT_FORM_VALUES: FormValues = {
  S: "100",
  K: "100",
  T: "1",
  r: "0.05",
  sigma: "0.2",
  N: "10000",
  seed: "42",
};

export const PRESET_CASES: PresetCase[] = [
  {
    id: "itm",
    label: "In-the-money",
    description: "S exceeds K, giving the call intrinsic value at the outset.",
    values: {
      S: "120",
      K: "100",
      T: "1",
      r: "0.05",
      sigma: "0.2",
      N: "10000",
      seed: "42",
    },
  },
  {
    id: "atm",
    label: "At-the-money",
    description: "S and K are aligned for a balanced classroom reference case.",
    values: {
      S: "100",
      K: "100",
      T: "1",
      r: "0.05",
      sigma: "0.2",
      N: "10000",
      seed: "42",
    },
  },
  {
    id: "otm",
    label: "Out-of-the-money",
    description: "S is below K, so the value is dominated by time and volatility.",
    values: {
      S: "90",
      K: "110",
      T: "1",
      r: "0.05",
      sigma: "0.2",
      N: "10000",
      seed: "42",
    },
  },
];

export const FIELD_DEFINITIONS: FieldDefinition[] = [
  {
    name: "S",
    label: "S",
    helper: "Current stock price",
    placeholder: "100",
    inputMode: "decimal" as const,
  },
  {
    name: "K",
    label: "K",
    helper: "Strike price",
    placeholder: "100",
    inputMode: "decimal" as const,
  },
  {
    name: "T",
    label: "T",
    helper: "Time to maturity in years",
    placeholder: "1",
    inputMode: "decimal" as const,
  },
  {
    name: "r",
    label: "r",
    helper: "Risk-free rate as a decimal",
    placeholder: "0.05",
    inputMode: "decimal" as const,
  },
  {
    name: "sigma",
    label: "sigma",
    helper: "Volatility as a decimal",
    placeholder: "0.2",
    inputMode: "decimal" as const,
  },
  {
    name: "N",
    label: "N",
    helper: "Monte Carlo simulation count",
    placeholder: "10000",
    inputMode: "numeric" as const,
  },
  {
    name: "seed",
    label: "seed",
    helper: "Optional integer seed for reproducibility",
    placeholder: "42",
    inputMode: "numeric" as const,
  },
];
