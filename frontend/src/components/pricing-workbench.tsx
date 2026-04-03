"use client";

import { useState, type FormEvent } from "react";

import { ParameterField } from "@/components/parameter-field";
import { ResultsPanel } from "@/components/results-panel";
import { submitPricing } from "@/lib/api";
import { DEFAULT_FORM_VALUES, FIELD_DEFINITIONS, PRESET_CASES } from "@/lib/constants";
import type {
  CompareResult,
  FieldErrors,
  FieldName,
  FormValues,
  PricingPayload,
  PricingResult,
  PresetCase,
  StatusState,
  SubmissionMode,
  UiResult,
} from "@/lib/types";
import { validateForm } from "@/lib/validation";

const LOADING_MESSAGES: Record<SubmissionMode, string> = {
  "black-scholes": "Requesting the analytical Black-Scholes result from the backend.",
  "monte-carlo": "Running the Monte Carlo pricing request through the backend.",
  compare: "Comparing Black-Scholes and Monte Carlo outputs through the compare endpoint.",
};

const SUCCESS_MESSAGES: Record<SubmissionMode, string> = {
  "black-scholes": "Black-Scholes pricing completed successfully.",
  "monte-carlo": "Monte Carlo pricing completed successfully.",
  compare: "Comparison completed successfully.",
};

function buildUiResult(
  mode: SubmissionMode,
  payload: PricingPayload,
  response: PricingResult | CompareResult,
): UiResult {
  if (mode === "compare") {
    const compareResult = response as CompareResult;

    return {
      mode,
      blackScholes: compareResult.black_scholes,
      monteCarlo: compareResult.monte_carlo,
      absoluteError: compareResult.absolute_error,
      request: {
        N: payload.N,
        seed: payload.seed ?? null,
      },
    };
  }

  const pricingResult = response as PricingResult;

  return {
    mode,
    blackScholes: mode === "black-scholes" ? pricingResult : undefined,
    monteCarlo: mode === "monte-carlo" ? pricingResult : undefined,
    request: {
      N: payload.N,
      seed: payload.seed ?? null,
    },
  };
}

function cloneValues(values: FormValues): FormValues {
  return {
    S: values.S,
    K: values.K,
    T: values.T,
    r: values.r,
    sigma: values.sigma,
    N: values.N,
    seed: values.seed,
  };
}

export function PricingWorkbench() {
  const [values, setValues] = useState<FormValues>(cloneValues(DEFAULT_FORM_VALUES));
  const [errors, setErrors] = useState<FieldErrors>({});
  const [status, setStatus] = useState<StatusState>({
    kind: "idle",
  });
  const [result, setResult] = useState<UiResult | null>(null);
  const [activeAction, setActiveAction] = useState<SubmissionMode | null>(null);
  const [selectedPresetId, setSelectedPresetId] = useState<string>("atm");

  function handleFieldChange(field: FieldName, value: string) {
    setValues((currentValues) => ({
      ...currentValues,
      [field]: value,
    }));
    setSelectedPresetId("");

    if (errors[field]) {
      setErrors((currentErrors) => {
        const nextErrors = { ...currentErrors };
        delete nextErrors[field];
        return nextErrors;
      });
    }

    if (status.kind === "error") {
      setStatus({ kind: "idle" });
    }
  }

  function applyPreset(preset: PresetCase) {
    setValues(cloneValues(preset.values));
    setErrors({});
    setStatus({ kind: "idle" });
    setSelectedPresetId(preset.id);
  }

  async function runAction(mode: SubmissionMode) {
    const validation = validateForm(values);

    if (!validation.payload) {
      setErrors(validation.errors);
      setStatus({
        kind: "error",
        message: "Correct the highlighted inputs before submitting a pricing request.",
      });
      return;
    }

    setErrors({});
    setActiveAction(mode);
    setStatus({
      kind: "loading",
      message: LOADING_MESSAGES[mode],
    });

    try {
      const response = await submitPricing(mode, validation.payload);
      setResult(buildUiResult(mode, validation.payload, response));
      setStatus({
        kind: "success",
        message: SUCCESS_MESSAGES[mode],
      });
    } catch (error) {
      const message =
        error instanceof Error ? error.message : "An unexpected error occurred while pricing.";

      setStatus({
        kind: "error",
        message,
      });
    } finally {
      setActiveAction(null);
    }
  }

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    void runAction("compare");
  }

  return (
    <section className="workspace-grid">
      <section className="panel input-panel">
        <div className="panel-header">
          <div>
            <p className="section-kicker">Input Set</p>
            <h2>Option Parameters</h2>
          </div>
          <span className="status-pill">European call</span>
        </div>

        <p className="panel-copy">
          Enter model parameters in decimal form and use the compare action as the primary workflow
          for presentation-ready benchmarking.
        </p>

        <div className="preset-section">
          <div className="subsection-header">
            <h3>Example cases</h3>
            <span>Loaded from project docs</span>
          </div>
          <div className="preset-grid">
            {PRESET_CASES.map((preset) => (
              <button
                key={preset.id}
                type="button"
                className={selectedPresetId === preset.id ? "preset-button preset-active" : "preset-button"}
                onClick={() => applyPreset(preset)}
              >
                <strong>{preset.label}</strong>
                <span>{preset.description}</span>
              </button>
            ))}
          </div>
        </div>

        <form className="pricing-form" onSubmit={handleSubmit}>
          <div className="field-grid">
            {FIELD_DEFINITIONS.map((field) => (
              <ParameterField
                key={field.name}
                id={field.name}
                label={field.label}
                helper={field.helper}
                placeholder={field.placeholder}
                inputMode={field.inputMode}
                value={values[field.name]}
                error={errors[field.name]}
                onChange={handleFieldChange}
              />
            ))}
          </div>

          <p className="form-footnote">
            Use decimal inputs for <code>r</code> and <code>sigma</code>, for example{" "}
            <code>0.05</code> and <code>0.2</code>. The compare button is the default action and
            calls the backend compare endpoint first.
          </p>

          <div className="action-row">
            <button
              type="submit"
              className="action-button action-primary"
              disabled={activeAction !== null}
            >
              {activeAction === "compare" ? "Running Compare..." : "Compare Both"}
            </button>
            <button
              type="button"
              className="action-button"
              disabled={activeAction !== null}
              onClick={() => void runAction("black-scholes")}
            >
              {activeAction === "black-scholes" ? "Computing..." : "Black-Scholes"}
            </button>
            <button
              type="button"
              className="action-button"
              disabled={activeAction !== null}
              onClick={() => void runAction("monte-carlo")}
            >
              {activeAction === "monte-carlo" ? "Computing..." : "Monte Carlo"}
            </button>
          </div>
        </form>
      </section>

      <ResultsPanel result={result} status={status} activeAction={activeAction} />
    </section>
  );
}
