from app.invoice import generate_invoice

def test_invoice_generation():
    order = {
        "order_id": "ORD-101",
        "customer": "Demo Customer",
        "items": [{"unit_price": 100, "quantity": 2}]
    }
    invoice = generate_invoice(order)
    assert invoice["total"] == 200
    assert invoice["status"] == "generated"
