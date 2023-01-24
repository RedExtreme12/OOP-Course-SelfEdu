class FloatValue:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if isinstance(value, float):
            setattr(instance, self.name, value)
        else:
            raise TypeError('Присваивать можно только вещественный тип данных.')

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Cell:

    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value

    # def __repr__(self):
    #     return str(self.value)


class TableSheet:

    def __init__(self, n: int, m: int):
        self.cells = [[Cell() for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)
value_generator = iter(range(1, 16))
for row in table.cells:
    for cell in row:
        cell.value = float(next(value_generator))
    print(row)
