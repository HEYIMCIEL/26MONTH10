import datetime
import json
from pathlib import Path

from models import CartItem, Product
class CashRegister:
    def __init__(self):
        self.items: list[CartItem] = []

    def add_item(self, product: Product, quantity: int  ):
        cart_item = CartItem(product=product, quantity=quantity)
        self.items.append(cart_item)

    def subtotal(self):
        return sum(item.subtotal() for item in self.items)

    def tax(self):
        return self.subtotal() * self.TAX_RATE

    def total(self):
        return self.subtotal() + self.tax()

    def print_receipt(self):
        print("----Receipt----")
        for item in self.items:
            print(f"{item.product.name} x {item.quantity} = {item.subtotal()}")
        print(f"Before Tax: {self.subtotal()}")
        print(f"Tax: {self.tax()}")
        print(f"Total: {self.total()}") 

    def save_sales(self, filepath: str="sales.json"):
        path=Path(filepath)
        if path.exists():
            with path.open("r", encoding="utf-8") as file:
                sales = json.load(file)
            if not isinstance(sales, list):
                raise ValueError("Sales data is not a list")
        else:
            sales = []  

        sales.append({
            "timestamp":datetime.now().isoformat(timespec="seconds"),
            "items":[
                {
                    "code": item.product.code,
                    "name": item.product.name,
                    "price": item.product.price,
                    "quantity": item.quantity,
                }
                for item in self.items
            ],
            "subtotal": self.subtotal(),
            "tax": self.tax(),
            "total": self.total(),
        })

        with path.open("w", encoding="utf-8") as file:
            json.dump(sales, file, ensure_ascii=False, indent=2)


        
