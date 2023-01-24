

class Record:

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __getitem__(self, item: int):
        if not isinstance(item, int) or not (0 <= item < len(self.__dict__)):
            raise IndexError('неверный индекс поля')

        for i, value in enumerate(self.__dict__.values()):
            if i == item:
                return value

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not (0 <= key < len(self.__dict__)):
            raise IndexError('неверный индекс поля')

        for i, items in enumerate(self.__dict__.items()):
            key_, value_ = items

            if i == key:
                setattr(self, key_, value)


r = Record(pk=1, title='Python ООП', author='Балакирев')
# print(r[2])
print(r[1])
r[1] = 'asd'
print(r[1])
