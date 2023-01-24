from random import randint


class Cell:
    """Клетка"""
    def __init__(self, mine: bool, fl_open: bool, around_mines: int = 0):
        self.around_mines = around_mines  # количество мин вокруг
        self.mine = mine  # есть ли мина
        self.fl_open = fl_open  # открыта ли клетка

    def __repr__(self):
        return str(self.around_mines)


class GamePole:
    def __init__(self, n, m):
        """
        :param n: size of map – NxN matrix
        :param m: amount of mines on map
        """
        self.pole = self.init_default_pole(n)  # n x n matrix
        self.size_of_pole = len(self.pole)
        self.init(m)

    def _recalculate_numbers_of_mines_in_surrounding_cells(self, row_number, column_number):
        indexes = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (0, 1), (-1, 1))

        for difference_row_number, difference_column_number in indexes:
            calculated_index_of_row = row_number + difference_row_number
            calculated_index_of_column = column_number + difference_column_number

            if (0 <= calculated_index_of_row <= self.size_of_pole - 1) and \
                    (0 <= calculated_index_of_column <= self.size_of_pole - 1):
                self.pole[calculated_index_of_row][calculated_index_of_column].around_mines += 1

    def _set_up_mine_on_pole(self, x, y) -> bool:
        if not self.pole[x][y].mine:
            self.pole[x][y].mine = True
            return True

        return False

    @staticmethod
    def init_default_pole(pole_size):
        return [[Cell(False, False) for _ in range(pole_size)] for _ in range(pole_size)]

    def init(self, mines_count):
        count_of_set_up_mines = 0

        while count_of_set_up_mines != mines_count:
            row_number, column_number = randint(0, self.size_of_pole - 1), randint(0, self.size_of_pole - 1)

            if self._set_up_mine_on_pole(row_number, column_number):
                count_of_set_up_mines += 1
                self._recalculate_numbers_of_mines_in_surrounding_cells(row_number, column_number)

    def show(self):
        for row in self.pole:
            for column in row:
                if not column.fl_open:
                    print('#', end='')
                else:
                    print(column.around_mines, end='')
            print()


pole_game = GamePole(10, 12)
