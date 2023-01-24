class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Product):
    pass


class TV(Product):
    pass


class Notebook(Product):
    pass


class Cup(Product):
    pass


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{product.name}: {product.price}' for product in self.goods]


cart = Cart()

cart.add(
    TV('LG', 1000),
)
cart.add(
    TV('Samsung', 1200)
)
cart.add(
    Notebook('MacBook', 2500)
)
cart.add(
    Notebook('Lenovo', 800)
)
cart.add(
    Cup('Little cup', 5)
)
