from app.pricing import calculate_price

def checkout(items):
    total = 0
    for item in items:
        total += calculate_price(
            item["unit_price"],
            item["quantity"],
            item.get("discount", 0)
        )
    return round(total, 2)
