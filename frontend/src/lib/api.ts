import type { CompareResult, PricingPayload, PricingResult, SubmissionMode } from "@/lib/types";

const ENDPOINT_MAP: Record<SubmissionMode, string> = {
  "black-scholes": "/api/price/black-scholes",
  "monte-carlo": "/api/price/monte-carlo",
  compare: "/api/price/compare",
};

interface BackendIssue {
  loc?: Array<string | number>;
  msg?: string;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function formatBackendIssues(detail: BackendIssue[]): string {
  return detail
    .map((issue) => {
      const location = issue.loc?.[issue.loc.length - 1];
      if (typeof location === "string" && issue.msg) {
        return `${location}: ${issue.msg}`;
      }

      return issue.msg ?? "Validation error.";
    })
    .join(" ");
}

function extractErrorMessage(payload: unknown, status: number): string {
  if (!isRecord(payload)) {
    return `Request failed with status ${status}.`;
  }

  const detail = payload.detail;

  if (typeof detail === "string") {
    return detail;
  }

  if (Array.isArray(detail)) {
    return formatBackendIssues(detail as BackendIssue[]);
  }

  return `Request failed with status ${status}.`;
}

export class ApiError extends Error {
  status: number;

  constructor(message: string, status: number) {
    super(message);
    this.name = "ApiError";
    this.status = status;
  }
}

export async function submitPricing(
  mode: SubmissionMode,
  payload: PricingPayload,
): Promise<PricingResult | CompareResult> {
  const response = await fetch(ENDPOINT_MAP[mode], {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data = (await response.json().catch(() => null)) as unknown;

  if (!response.ok) {
    throw new ApiError(extractErrorMessage(data, response.status), response.status);
  }

  return data as PricingResult | CompareResult;
}
