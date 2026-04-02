import time


def get_timestamp() -> float:
    return time.perf_counter()


def elapsed_ms(start_time: float) -> float:
    return (time.perf_counter() - start_time) * 1000


def build_result(method: str, price: float, runtime_ms: float, inputs: dict) -> dict:
    return {
        "method": method,
        "price": float(price),
        "display_price": round(float(price), 2),
        "runtime_ms": round(float(runtime_ms), 4),
        "inputs": inputs,
    }