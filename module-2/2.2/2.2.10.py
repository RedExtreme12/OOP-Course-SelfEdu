import math


def get_count_of_digits_in_int(number: int) -> int:
    return int(math.log10(number)) + 1


class PhoneNumber:

    COUNT_OF_DIGITS_IN_PHONE_NUMBER = 11

    def __init__(self, number, fio):
        self.__number = number
        self.__fio = fio

    @classmethod
    def check_number(cls, number) -> bool:
        if isinstance(number, int) and get_count_of_digits_in_int(number) == cls.COUNT_OF_DIGITS_IN_PHONE_NUMBER:
            return True
        return False

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if self.check_number(value):
            self.__number = value
        else:
            self.__number = None

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, value):
        if isinstance(value, str):
            self.__fio = value


class PhoneBook:

    def __init__(self):
        self.phones = []

    def add_phone(self, number: PhoneNumber):
        self.phones.append(number)

    def remove_phone(self, indx):
        del self.phones[indx]

    def get_phone_list(self):
        return self.phones
