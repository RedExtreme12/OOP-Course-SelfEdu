from operator import add, sub, mul, floordiv, mod
from typing import Union


class Box3D:

    def __init__(self, width: Union[int, float], height: Union[int, float], depth: Union[int, float]):
        self.width = width
        self.height = height
        self.depth = depth

    def do_operation(self, operation, other):
        if isinstance(other, Box3D):
            new_box = Box3D(operation(self.width, other.width),
                            operation(self.height, other.height),
                            operation(self.depth, other.depth))
            return new_box
        elif isinstance(other, (int, float)):
            new_box = Box3D(operation(self.width, other),
                            operation(self.height, other),
                            operation(self.depth, other))
            return new_box

    def __add__(self, other):
        return self.do_operation(add, other)

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        return self.do_operation(mul, other)

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        return self.do_operation(sub, other)

    def __rsub__(self, other):
        return self - other

    def __floordiv__(self, other):
        return self.do_operation(floordiv, other)

    def __rtruediv__(self, other):
        return self // other

    def __mod__(self, other):
        return self.do_operation(mod, other)

    def __rmod__(self, other):
        return self % other


box1 = Box3D(1, 2, 3)
box2 = Box3D(2, 4, 6)

box = box1 + box2 # Box3D: width=3, height=6, depth=9 (соответствующие размерности складываются)
box = box1 * 2    # Box3D: width=2, height=4, depth=6 (каждая размерность умножается на 2)
box = 3 * box2    # Box3D: width=6, height=12, depth=18
box = box2 - box1 # Box3D: width=1, height=2, depth=3 (соответствующие размерности вычитаются)
box = box1 // 2   # Box3D: width=0, height=1, depth=1 (соответствующие размерности целочисленно делятся на 2)
box = box2 % 3    # Box3D: width=2, height=1, depth=0
print(box.width, box.height, box.depth)
