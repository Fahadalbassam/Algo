import { PricingWorkbench } from "@/components/pricing-workbench";

export default function Home() {
  return (
    <main className="page-shell">
      <section className="hero-panel">
        <p className="hero-kicker">Computational Finance Project</p>
        <h1>European Call Option Pricing</h1>
        <p className="hero-copy">
          Compare the analytical Black-Scholes formula with Monte Carlo simulation for a European
          call option. The interface is tuned for coursework demos, report screenshots, and quick
          numerical validation against the backend API.
        </p>
        <div className="hero-meta">
          <span>Academic presentation layout</span>
          <span>Compare endpoint prioritized</span>
          <span>Client-side validation included</span>
        </div>
      </section>

      <PricingWorkbench />
    </main>
  );
}
