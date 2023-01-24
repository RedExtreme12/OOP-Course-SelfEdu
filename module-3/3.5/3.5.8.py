from functools import wraps
from typing import Union


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money: 'Money'):
        money.cb = cls


class Money:

    currency_code = None

    def __init__(self, volume: Union[int, float] = 0):
        self.__cb: CentralBank or None = None
        self.__volume = volume

    @property
    def cb(self):
        return self.__cb

    @cb.setter
    def cb(self, value: CentralBank):
        self.__cb = value

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):
        self.__volume = value

    def convert(self) -> float:
        if isinstance(self, MoneyR):
            return self.volume

        self_to_usd = self.volume * self.cb.rates[self.currency_code]
        usd_to_rub = self_to_usd * self.cb.rates['rub']

        return usd_to_rub

    # @staticmethod
    # def _check_is_registered(func):
    #     @wraps(func)
    #     def wrapper(self: 'Money', other: 'Money'):
    #         if self.cb is None:
    #             raise ValueError('Неизвестен курс валют.')
    #         return func(self, other)
    #     return wrapper

    def check_is_registered(self, other):
        if self.cb is None or other.cb is None:
            raise ValueError('Неизвестен курс валют.')

    # @_check_is_registered
    def __gt__(self, other: 'Money'):
        self.check_is_registered(other)
        return self.convert() > other.convert()

    # @_check_is_registered
    def __ge__(self, other):
        self.check_is_registered(other)
        return self.convert() >= other.convert()

    # @_check_is_registered
    def __eq__(self, other):
        self.check_is_registered(other)
        return 0 <= abs(self.convert() - other.convert()) <= 0.1


class MoneyR(Money):
    currency_code = 'rub'


class MoneyD(Money):
    currency_code = 'dollar'


class MoneyE(Money):
    currency_code = 'euro'


CentralBank.rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

r = MoneyR(45000)
d = MoneyD(500)

CentralBank.register(r)
CentralBank.register(d)

if r > d:
    print("неплохо")
else:
    print("нужно поднажать")
