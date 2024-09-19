from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app)


def test_create_product():
    product_data = {
        "name": "Test Product",
        "description": "This is a test product",
        "price": 100,
        "quantity": 50,
    }

    response = client.post("/products/", json=product_data)
    assert response.status_code == status.HTTP_201_CREATED
    product = response.json()
    assert product["name"] == product_data["name"]
    assert product["quantity"] == product_data["quantity"]
