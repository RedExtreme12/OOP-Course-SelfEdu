import sys
from collections import defaultdict
from typing import Union


class ShopItem:

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]):
        self.name = name
        self.weight = weight
        self.price = price

    def __members(self):
        return self.name.lower(), self.weight, self.price

    def __hash__(self):
        return hash(self.__members())

    def __eq__(self, other: 'ShopItem'):
        return self.__members() == other.__members()


"""
Системный блок: 1500 75890.56
Монитор Samsung: 2000 34000
Клавиатура: 200.44 545
Монитор Samsung: 2000 34000
"""


lst_in = list(map(str.strip, sys.stdin.readlines()))
shop_items = {}
for item_str in lst_in:
    item_name, item_number_characteristics = item_str.split(':')
    item_weight, item_price = item_number_characteristics.split(' ')[1:]

    item_obj = ShopItem(item_name, item_weight, item_price)

    shop_item = shop_items.setdefault(item_obj, [item_obj, 0])
    shop_items[item_obj][1] += 1
