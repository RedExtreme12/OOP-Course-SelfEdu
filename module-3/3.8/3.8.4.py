from abc import ABC, abstractmethod


class Cell(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class Integer(Cell):

    datatype = int

    def __init__(self, start_value: int = 0):
        self.__value = None
        self.value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        if not isinstance(value, int):
            raise ValueError('должно быть целое число')
        self.__value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)


class Array:

    def __init__(self, max_length: int, cell: Integer.__class__):
        self.max_length = max_length
        self.cell = cell
        self.cells: list[Integer] = [cell(0) for _ in range(max_length)]

    def check_index(self, index):
        if not isinstance(index, int) or not (0 <= index < self.max_length):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def check_cell_value(self, value):
        if not isinstance(value, self.cell.datatype):
            raise ValueError()

    def __getitem__(self, key: int):
        self.check_index(key)

        return self.cells[key].value

    def __setitem__(self, key, value):
        self.check_index(key)
        self.check_cell_value(value)

        self.cells[key].value = value

    def __str__(self):
        return ' '.join(map(str, self.cells))
