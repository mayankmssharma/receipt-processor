from fastapi.testclient import TestClient
import pytest
# from main import app
import app
from app.models import Item, Receipt

client = TestClient(app)

# Test data based on the examples you provided
example_1 = Receipt(
    retailer="Target",
    purchaseDate="2022-01-01",
    purchaseTime="13:01",
    total="35.35",
    items=[
        Item(shortDescription="Mountain Dew 12PK", price="6.49"),
        Item(shortDescription="Emils Cheese Pizza", price="12.25"),
        Item(shortDescription="Knorr Creamy Chicken", price="1.26"),
        Item(shortDescription="Doritos Nacho Cheese", price="3.35"),
        Item(shortDescription="   Klarbrunn 12-PK 12 FL OZ  ", price="12.00")
    ]
)

example_2 = Receipt(
    retailer="M&M Corner Market",
    purchaseDate="2022-03-20",
    purchaseTime="14:33",
    total="9.00",
    items=[
        Item(shortDescription="Gatorade", price="2.25"),
        Item(shortDescription="Gatorade", price="2.25"),
        Item(shortDescription="Gatorade", price="2.25"),
        Item(shortDescription="Gatorade", price="2.25")
    ]
)


def test_calculate_points_with_examples():
    from app.calculate_points import calculate_points

    points_example_1 = calculate_points(example_1)
    points_example_2 = calculate_points(example_2)

    assert points_example_1 == 28
    assert points_example_2 == 109
