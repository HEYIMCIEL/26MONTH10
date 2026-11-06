from models import Product
from register import CashRegister

catalog={
    "P001": Product(code="P001", name="Pen", price=10.99),
    "P002": Product(code="P002", name="Pencil", price=5.99),
    "P003": Product(code="P003", name="Notebook", price=15.99),
}

register = CashRegister()


print("===Welcome to the Cash Register System===")
for product in catalog.values():
    print(f"{product.code}: {product.name} - ${product.price:,.2f}")

while True:
    code = input("Enter product code (or 'done' to finish): ")
    if code.lower() == "done":
        break

    if code not in catalog:
        print("Invalid product code. Please try again.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {catalog[code].name}: "))
        if quantity < 0:
            raise ValueError("Quantity must be non-negative.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid quantity.")
        continue   