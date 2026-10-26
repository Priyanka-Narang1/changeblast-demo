from app.checkout import checkout

def test_checkout_multiple_items():
    items = [
        {"unit_price": 100, "quantity": 2},
        {"unit_price": 50, "quantity": 1, "discount": 10}
    ]
    assert checkout(items) == 245
