from typing import Union


class RadiusVector2D:

    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: int = 0, y: int = 0):
        self.__x = self.__y = 0
        self.x = x
        self.y = y

    @classmethod
    def verify(cls, value: Union[int, float]) -> bool:
        if type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD:
            return True
        return False

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if self.verify(value):
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if self.verify(value):
            self.__y = value

    @staticmethod
    def norm2(vector: 'RadiusVector2D') -> float:
        return vector.x ** 2 + vector.y ** 2
