import pytest
from app.pricing import calculate_price

def test_regular_price():
    assert calculate_price(100, 2) == 200

def test_discount():
    assert calculate_price(100, 2, 10) == 180

def test_invalid_price():
    with pytest.raises(ValueError):
        calculate_price(-10, 1)

def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_price(100, 1, 110)
