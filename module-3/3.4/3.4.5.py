from operator import add, sub, mul, truediv


class ListMath:

    def __init__(self, lst_math=None):
        self._lst_math = None
        self.lst_math = lst_math

    @property
    def lst_math(self):
        return self._lst_math

    @lst_math.setter
    def lst_math(self, _lst):
        if _lst is None:
            self._lst_math = []
        else:
            self._lst_math = list(filter(lambda x: type(x) in (float, int), _lst))

    def __add__(self, other):
        return ListMath(list(add(i, other) for i in self.lst_math))

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        for i in range(len(self._lst_math)):
            self._lst_math[i] += other
        return self

    def __sub__(self, other):
        return ListMath(list(sub(i, other) for i in self.lst_math))

    def __rsub__(self, other):
        return ListMath(list(sub(other, i) for i in self.lst_math))

    def __isub__(self, other):
        for i in range(len(self._lst_math)):
            self._lst_math[i] -= other
        return self

    def __mul__(self, other):
        return ListMath(list(mul(other, i) for i in self.lst_math))

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        for i in range(len(self._lst_math)):
            self._lst_math[i] *= other
        return self

    def __truediv__(self, other):
        return ListMath(list(truediv(other, i) for i in self.lst_math))

    def __rtruediv__(self, other):
        return ListMath(list(truediv(i, other) for i in self.lst_math))

    def __itruediv__(self, other):
        for i in range(len(self._lst_math) - 1):
            self._lst_math[i] /= other
        return self


lst1 = ListMath()
lp = [1, False, 2, -5, "abc", 7]
lst2 = ListMath(lp)
lst3 = ListMath(lp)
res1 = lst2 + 76
lst = ListMath([1, 2, 3])
lst += 5
print(lst.lst_math, res1.lst_math)
assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71, 83], "неверные значения, полученные при операциях сложения"

