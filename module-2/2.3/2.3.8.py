class StringValue:

    def __init__(self, min_length=2, max_length=50):
        self._min_length = min_length
        self._max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if isinstance(value, str) and self._min_length <= len(value) <= self._max_length:
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class PriceValue:

    def __init__(self, max_value=10000):
        self._max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if isinstance(value, (int, float)) and 0 <= value <= self._max_value:
            setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)

