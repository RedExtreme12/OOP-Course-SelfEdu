import itertools
import random
from pprint import pprint
from typing import List


class Cell:

    def __init__(self):
        self.__is_mine = False
        self.__number = 0
        self.__is_open = False

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: int):
        if not isinstance(value, int) or not 0 <= value <= 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, value):
        if not isinstance(value, bool):
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __bool__(self):
        return not self.__is_open

    def __repr__(self):
        return f'{self.number}'


class GamePole:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, count_of_row: int, count_of_column: int, total_mines: int):
        self.count_of_row = count_of_row
        self.count_of_column = count_of_column
        self.total_mines = total_mines
        self.__pole_cells: List[List[Cell]] or None = None

    @property
    def pole(self):
        return self.__pole_cells

    def check_occurrence_of_indexes(self, row_number: int, column_number: int):
        if 0 <= row_number <= self.count_of_row - 1 and 0 <= column_number <= self.count_of_column - 1:
            return True
        return False

    def _recalculate_numbers_of_mines_in_surrounding_cells(self, row_number: int, column_number: int):
        indices = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (0, 1), (-1, 1))
        for difference_row_number, difference_column_number in indices:
            calculated_index_of_row = row_number + difference_row_number
            calculated_index_of_column = column_number + difference_column_number

            if self.check_occurrence_of_indexes(calculated_index_of_row, calculated_index_of_column):
                self.__pole_cells[calculated_index_of_row][calculated_index_of_column].number += 1

    def _set_up_mine(self, row_number: int, column_number: int):
        self.__pole_cells[row_number][column_number].is_mine = True
        self._recalculate_numbers_of_mines_in_surrounding_cells(row_number, column_number)

    def _set_up_mines(self):
        for _ in range(self.total_mines):
            row_number = random.randint(0, self.count_of_row - 1)
            column_number = random.randint(0, self.count_of_column - 1)
            self._set_up_mine(row_number, column_number)

    def init_pole(self):
        self.__pole_cells = [[Cell() for _ in range(self.count_of_column)] for _ in range(self.count_of_row)]
        pprint(self.__pole_cells)
        self._set_up_mines()

    def open_cell(self, i, j):
        if not self.check_occurrence_of_indexes(i, j):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        for row in self.pole:
            for column in row:
                if not column.number:
                    print('#', end='')
                else:
                    print(column.number, end='')
            print()


p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
    Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1
print(m)