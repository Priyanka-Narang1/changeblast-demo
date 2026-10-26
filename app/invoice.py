from app.checkout import checkout

def generate_invoice(order):
    total = checkout(order["items"])
    return {
        "order_id": order["order_id"],
        "customer": order["customer"],
        "total": total,
        "status": "generated"
    }
