from app.checkout import checkout
from app.invoice import generate_invoice

def create_order(order):
    total = checkout(order["items"])
    invoice = generate_invoice(order)
    return {
        "order_id": order["order_id"],
        "total": total,
        "invoice": invoice,
        "status": "confirmed"
    }
