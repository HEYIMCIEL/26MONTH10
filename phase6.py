from dataclasses import dataclass


@dataclass
class Product:
    code: str
    name: str
    price: int

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price Over 0")


@dataclass
class CartItem:
    product: Product
    quantity: int

    def __post_init__(self):
        if self.quantity < 0:
            raise ValueError("Quantity Over 0")

    def subtotal(self):
        return self.product.price * self.quantity
