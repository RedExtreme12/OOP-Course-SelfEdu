from typing import Union


class DimensionsDescriptor:

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError('габаритные размеры должны быть положительными числами')
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Dimensions:
    a = DimensionsDescriptor()
    b = DimensionsDescriptor()
    c = DimensionsDescriptor()

    def __init__(self, *args):
        a, b, c = args
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))


lst_dims = [Dimensions(*map(lambda x: int(x) if x.isdigit() else float(x), numbers_string.split()))
            for numbers_string in input().split('; ')]
lst_dims = sorted(lst_dims, key=hash)

