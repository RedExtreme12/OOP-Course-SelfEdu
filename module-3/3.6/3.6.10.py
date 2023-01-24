import math


class TriangleDescriptor:

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError('длины сторон треугольника должны быть положительными числами')
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Triangle:

    a = TriangleDescriptor()
    b = TriangleDescriptor()
    c = TriangleDescriptor()

    def __init__(self, a, b, c):
        self.is_correct_sided(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_correct_sided(a, b, c):
        if not (a < b + c) and (b < a + c) and (c < a + b):
            raise ValueError('с указанными длинами нельзя образовать треугольник')

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
print(tr())

