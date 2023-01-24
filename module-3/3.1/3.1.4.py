from typing import Any


def check_type(x: Any, types: tuple) -> bool:
    if type(x) in types:
        if int in types or float in types:
            return x > 0
        return True

    return False


class Product:

    id_counter = 1

    TYPES = {
        'id': (int, ),
        'name': (str, ),
        'weight': (int, float),
        'price': (int, float),
    }

    def __new__(cls, *args, **kwargs):
        new_product = super().__new__(cls)
        setattr(new_product, 'id', cls.id_counter)
        cls.id_counter += 1

        return new_product

    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if check_type(value, self.TYPES[key]):
            object.__setattr__(self, key, value)
        else:
            raise TypeError('Неверный тип присваиваемых данных.')

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)
