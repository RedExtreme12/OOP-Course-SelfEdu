import math
from functools import wraps


def check_types_parts_of_complex_numbers(func):
    @wraps(func)
    def wrapper(self, value):
        if isinstance(value, (int, float)):
            return func(self, value)
        else:
            raise ValueError("Неверный тип данных.")

    return wrapper


class Complex:

    def __init__(self, real, img):
        self._real = self._img = None
        self.real = real
        self.img = img

    @property
    def real(self):
        return self._real

    @real.setter
    @check_types_parts_of_complex_numbers
    def real(self, value):
        self._real = value

    @property
    def img(self):
        return self._img

    @img.setter
    @check_types_parts_of_complex_numbers
    def img(self, value):
        self._img = value

    def __abs__(self):
        return math.sqrt(self.img ** 2 + self.real ** 2)


cmp = Complex(7, 8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
