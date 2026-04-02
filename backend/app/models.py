from pydantic import BaseModel, Field


class OptionInput(BaseModel):
    S: float = Field(..., gt=0, description="Current stock price")
    K: float = Field(..., gt=0, description="Strike price")
    T: float = Field(..., gt=0, description="Time to maturity in years")
    r: float = Field(..., description="Risk-free interest rate as decimal")
    sigma: float = Field(..., gt=0, description="Volatility as decimal")


class MonteCarloInput(OptionInput):
    N: int = Field(..., gt=0, description="Number of simulations")
    seed: int | None = Field(default=None, description="Random seed for reproducibility")


class PricingResult(BaseModel):
    method: str
    price: float
    display_price: float
    runtime_ms: float
    inputs: dict


class CompareResult(BaseModel):
    black_scholes: PricingResult
    monte_carlo: PricingResult
    absolute_error: float