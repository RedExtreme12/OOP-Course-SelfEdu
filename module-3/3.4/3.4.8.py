from typing import Union, List


class Item:

    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other: Union['Item', int, float]):
        if isinstance(other, Item):
            return self.money + other.money
        elif isinstance(other, (int, float)):
            return self.money + other
        else:
            raise ArithmeticError()

    def __radd__(self, other):
        return self + other


class Budget:

    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, it: Item):
        self.items.append(it)

    def remove_item(self, indx: int):
        self.items.pop(indx)

    def get_items(self):
        return self.items


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x
print(s)
