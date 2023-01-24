class Dimensions:

    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def check_dimension(cls, value) -> bool:
        if isinstance(value, (int, float)) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION:
            return True
        return False

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.check_dimension(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.check_dimension(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.check_dimension(value):
            self.__c = value

    def __setattr__(self, key, value):
        if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
            raise AttributeError('Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.')
        else:
            object.__setattr__(self, key, value)

