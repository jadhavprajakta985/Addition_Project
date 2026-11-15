
from fastapi.testclient import TestClient
from main import app

# Create test client
client = TestClient(app)


# Test 1: Home endpoint
def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Welcome to Addition Application"
    }


# Test 2: Normal addition
def test_addition():

    response = client.post(
        "/add",
        json={"num1": 10, "num2": 20}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 30


# Test 3: Negative numbers
def test_negative_numbers():

    response = client.post(
        "/add",
        json={"num1": -10, "num2": -20}
    )

    assert response.status_code == 200
    assert response.json()["result"] == -30


# Test 4: Decimal numbers
def test_decimal_numbers():

    response = client.post(
        "/add",
        json={"num1": 2.5, "num2": 3.5}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 6


# Test 5: Invalid input
def test_invalid_input():

    response = client.post(
        "/add",
        json={"num1": "hello", "num2": 20}
    )

    assert response.status_code == 422
