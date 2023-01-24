from functools import partial
from typing import Union
from itertools import zip_longest
from operator import add, sub, mul


class Vector:

    def __init__(self, *args):
        self.coords = list(args)

    def do_binary_operation(self, other_obj: 'Vector', operation):
        if len(self) != len(other_obj):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*(operation(i, j) for i, j in zip_longest(self.coords, other_obj.coords, fillvalue=0)))

    def do_assignment_operation(self, other: Union[int, float, 'Vector'], operation):
        if isinstance(other, Vector):
            self.coords = self.do_binary_operation(other, operation).coords
        else:
            self.coords = Vector(*(operation(i, other) for i in self.coords)).coords
        return self

    def __add__(self, other: 'Vector'):
        return self.do_binary_operation(other, add)

    def __sub__(self, other):
        return self.do_binary_operation(other, sub)

    def __mul__(self, other):
        return self.do_binary_operation(other, mul)

    def __iadd__(self, other):
        return self.do_assignment_operation(other, add)

    def __isub__(self, other):
        return self.do_assignment_operation(other, sub)

    def __eq__(self, other: 'Vector'):
        return self.coords == other.coords

    def __len__(self):
        return len(self.coords)


v1 = Vector(1, 2, 3, 4)
v2 = Vector(1, 2, 3, 5)
# print((v1 + v2).coords)
# print((v1 - v2).coords)
# print((v1 * v2).coords)
# v1 += 10
v1 -= v2
print(v1.coords)
