from collections import Counter

class Product:
    def __init__(self, name: str, price: int, discount_quantity: int = None, discount_price: int = None):
        self.name = name
        self.price = price
        self.discount_quantity = discount_quantity
        self.discount_price = discount_price

    def calculate_price(self, quantity: int) -> int:
        if self.discount_quantity and self.discount_price:
            discounted_sets = quantity // self.discount_quantity
            remaining_items = quantity % self.discount_quantity
            return discounted_sets * self.discount_price + remaining_items * self.price
        return quantity * self.price


class Cart:
    def __init__(self):
        self.items = Counter()
        self.product_catalog = {}

    def add_product(self, product: Product):
        self.product_catalog[product.name] = product

    def scan(self, product_name: str):
        if product_name in self.product_catalog:
            self.items[product_name] += 1
        else:
            raise ValueError(f"Product {product_name} not found in catalog")

    def total(self) -> int:
        return sum(
            self.product_catalog[item].calculate_price(quantity)
            for item, quantity in self.items.items()
        )


class Checkout:
    def __init__(self):
        self.cart = Cart()
        self.setup_products()

    def setup_products(self):
        self.cart.add_product(Product('A', 50, 3, 130))
        self.cart.add_product(Product('B', 30, 2, 45))
        self.cart.add_product(Product('C', 20))
        self.cart.add_product(Product('D', 15))

    def scan_items(self, items: str):
        for item in items:
            self.cart.scan(item)

    def get_total(self) -> int:
        return self.cart.total()


if __name__ == "__main__":
    checkout = Checkout()
    items = input("Enter items: ")
    checkout.scan_items(items)
    print("Total price:", checkout.get_total())
