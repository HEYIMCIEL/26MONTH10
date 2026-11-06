# register.py

def calculate_total(items: list[dict]) -> dict:
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    tax = subtotal * 10 // 100
    return {"subtotal": subtotal, "tax": tax, "total": subtotal + tax}

