from fastapi import FastAPI

from app.models import CompareResult, OptionInput, MonteCarloInput, PricingResult
from app.utils import get_timestamp, elapsed_ms, build_result
from app.black_scholes import black_scholes_call
from app.monte_carlo import monte_carlo_call

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/price/black-scholes", response_model=PricingResult)
def price_black_scholes(payload: OptionInput) -> PricingResult:
    start = get_timestamp()
    price = black_scholes_call(payload.S, payload.K, payload.T, payload.r, payload.sigma)
    runtime_ms = elapsed_ms(start)
    return build_result("black_scholes", price, runtime_ms, payload.model_dump())


@app.post("/price/monte-carlo", response_model=PricingResult)
def price_monte_carlo(payload: MonteCarloInput) -> PricingResult:
    start = get_timestamp()
    price = monte_carlo_call(
        payload.S,
        payload.K,
        payload.T,
        payload.r,
        payload.sigma,
        payload.N,
        payload.seed,
    )
    runtime_ms = elapsed_ms(start)
    return build_result("monte_carlo", price, runtime_ms, payload.model_dump())


@app.post("/price/compare", response_model=CompareResult)
def price_compare(payload: MonteCarloInput) -> CompareResult:
    bs_start = get_timestamp()
    bs_price = black_scholes_call(payload.S, payload.K, payload.T, payload.r, payload.sigma)
    bs_runtime_ms = elapsed_ms(bs_start)

    mc_start = get_timestamp()
    mc_price = monte_carlo_call(
        payload.S,
        payload.K,
        payload.T,
        payload.r,
        payload.sigma,
        payload.N,
        payload.seed,
    )
    mc_runtime_ms = elapsed_ms(mc_start)

    inputs = payload.model_dump()
    bs_result = build_result("black_scholes", bs_price, bs_runtime_ms, inputs)
    mc_result = build_result("monte_carlo", mc_price, mc_runtime_ms, inputs)

    return {
        "black_scholes": bs_result,
        "monte_carlo": mc_result,
        "absolute_error": abs(bs_price - mc_price),
    }
