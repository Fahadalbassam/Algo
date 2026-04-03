import type { PricingResult, StatusState, SubmissionMode, UiResult } from "@/lib/types";

interface ResultsPanelProps {
  result: UiResult | null;
  status: StatusState;
  activeAction: SubmissionMode | null;
}

function formatPrice(value: number): string {
  return new Intl.NumberFormat("en-US", {
    minimumFractionDigits: 4,
    maximumFractionDigits: 6,
  }).format(value);
}

function formatDisplayPrice(value: number): string {
  return new Intl.NumberFormat("en-US", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  }).format(value);
}

function formatRuntime(value: number): string {
  return `${new Intl.NumberFormat("en-US", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 4,
  }).format(value)} ms`;
}

function formatInteger(value: number): string {
  return new Intl.NumberFormat("en-US", {
    maximumFractionDigits: 0,
  }).format(value);
}

function formatSeed(value: number | null): string {
  if (value === null) {
    return "Not set";
  }

  return formatInteger(value);
}

function statusLabel(activeAction: SubmissionMode | null): string {
  switch (activeAction) {
    case "compare":
      return "Running comparison";
    case "black-scholes":
      return "Evaluating Black-Scholes";
    case "monte-carlo":
      return "Running Monte Carlo";
    default:
      return "Ready";
  }
}

function methodMeta(method: PricingResult["method"]): { title: string; tag: string; note: string } {
  if (method === "black_scholes") {
    return {
      title: "Black-Scholes",
      tag: "Analytical",
      note: "Closed-form benchmark for a European call under the model assumptions.",
    };
  }

  return {
    title: "Monte Carlo",
    tag: "Simulation",
    note: "Sampling-based estimate driven by N random draws and the optional seed.",
  };
}

function MethodCard({ result }: { result: PricingResult }) {
  const meta = methodMeta(result.method);

  return (
    <article className="method-card">
      <div className="method-card-header">
        <div>
          <p className="method-tagline">{meta.tag}</p>
          <h3>{meta.title}</h3>
        </div>
        <span className="method-badge">{meta.tag}</span>
      </div>
      <p className="method-price">{formatPrice(result.price)}</p>
      <dl className="method-metrics">
        <div>
          <dt>Rounded display</dt>
          <dd>{formatDisplayPrice(result.display_price)}</dd>
        </div>
        <div>
          <dt>Runtime</dt>
          <dd>{formatRuntime(result.runtime_ms)}</dd>
        </div>
      </dl>
      <p className="method-note">{meta.note}</p>
    </article>
  );
}

function SummaryMetric({
  label,
  value,
  emphasis = false,
}: {
  label: string;
  value: string;
  emphasis?: boolean;
}) {
  return (
    <article className={emphasis ? "summary-metric summary-metric-accent" : "summary-metric"}>
      <p>{label}</p>
      <strong>{value}</strong>
    </article>
  );
}

export function ResultsPanel({ result, status, activeAction }: ResultsPanelProps) {
  const showStatus = status.kind !== "idle";
  const hasBlackScholes = Boolean(result?.blackScholes);
  const hasMonteCarlo = Boolean(result?.monteCarlo);

  return (
    <section className="panel results-panel">
      <div className="panel-header">
        <div>
          <p className="section-kicker">Outputs</p>
          <h2>Results</h2>
        </div>
        <span className="status-pill">{statusLabel(activeAction)}</span>
      </div>

      {showStatus ? (
        <div className={`status-banner status-${status.kind}`}>
          <p>{status.message}</p>
        </div>
      ) : null}

      {result ? (
        <>
          <div className="method-grid">
            {hasBlackScholes ? <MethodCard result={result.blackScholes as PricingResult} /> : null}
            {hasMonteCarlo ? <MethodCard result={result.monteCarlo as PricingResult} /> : null}
          </div>

          <div className="summary-grid">
            <SummaryMetric
              label="Absolute difference"
              value={
                typeof result.absoluteError === "number"
                  ? formatPrice(result.absoluteError)
                  : "Run Compare Both"
              }
              emphasis={typeof result.absoluteError === "number"}
            />
            <SummaryMetric
              label="Simulation count"
              value={formatInteger(result.request.N)}
            />
            <SummaryMetric label="Seed" value={formatSeed(result.request.seed)} />
          </div>

          <p className="results-footnote">
            Black-Scholes is the analytical reference method. Monte Carlo is simulation-based, so
            its estimate stabilizes as the simulation count increases and becomes reproducible when
            a seed is supplied.
          </p>
        </>
      ) : (
        <div className="empty-state">
          <h3>Awaiting computation</h3>
          <p>
            Submit one of the pricing actions to display method prices, runtimes, and the
            comparison gap between the analytical and simulation-based approaches.
          </p>
        </div>
      )}
    </section>
  );
}
