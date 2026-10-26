def calculate_price(unit_price, quantity, discount=0):
    if unit_price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    if not 0 <= discount <= 100:
        raise ValueError("Discount must be between 0 and 100")
    subtotal = unit_price * quantity
    return round(subtotal * (1 - discount / 100), 2)
