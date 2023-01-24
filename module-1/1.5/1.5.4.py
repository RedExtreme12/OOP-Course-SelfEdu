import random
import sys


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


figures = (Line, Rect, Ellipse)
elements = [figures[random.randint(0, 2)](1, 2, 3, 4) for _ in range(0, 217)]
for element in elements:
    if isinstance(element, Line):
        element.ep = (0, 0)
        element.sp = (0, 0)

