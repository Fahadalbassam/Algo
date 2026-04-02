from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_price_black_scholes_valid_input() -> None:
    payload = {
        "S": 100,
        "K": 95,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
    }

    response = client.post("/price/black-scholes", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["method"] == "black_scholes"
    assert "price" in body
    assert "display_price" in body
    assert "runtime_ms" in body
    assert "inputs" in body


def test_price_black_scholes_invalid_sigma() -> None:
    payload = {
        "S": 100,
        "K": 95,
        "T": 1,
        "r": 0.05,
        "sigma": 0,
    }

    response = client.post("/price/black-scholes", json=payload)
    assert response.status_code == 422


def test_price_compare_valid_input() -> None:
    payload = {
        "S": 100,
        "K": 95,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "N": 10000,
        "seed": 42,
    }

    response = client.post("/price/compare", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert "black_scholes" in body
    assert "monte_carlo" in body
    assert "absolute_error" in body


def test_price_monte_carlo_valid_input() -> None:
    payload = {
        "S": 100,
        "K": 95,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "N": 10000,
        "seed": 42,
    }

    response = client.post("/price/monte-carlo", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["method"] == "monte_carlo"
    assert "price" in body
    assert "display_price" in body
    assert "runtime_ms" in body
    assert "inputs" in body


def test_price_monte_carlo_invalid_n() -> None:
    payload = {
        "S": 100,
        "K": 95,
        "T": 1,
        "r": 0.05,
        "sigma": 0.2,
        "N": 0,
        "seed": 42,
    }

    response = client.post("/price/monte-carlo", json=payload)
    assert response.status_code == 422
