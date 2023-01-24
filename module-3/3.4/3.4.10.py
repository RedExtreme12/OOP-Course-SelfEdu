from typing import Tuple, List


class TriangularMatrix:

    def __init__(self, matrix: List[List]):
        self._matrix = None
        self.matrix = matrix

    @staticmethod
    def is_matrix_rectangular(matrix: List[List]) -> bool:
        row_lengths = {len(row) for row in matrix}
        if len(row_lengths) > 1:
            return False
        return True

    @staticmethod
    def is_number_matrix(matrix: List[List]) -> bool:
        number_types = (int, float)
        for row in matrix:
            for number in row:
                if not isinstance(number, number_types):
                    return False

        return True

    @classmethod
    def verify_rectangular_matrix(cls, matrix) -> bool:
        if cls.is_matrix_rectangular(matrix) and cls.is_number_matrix(matrix):
            return True
        return False

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix_to_set: List[List]):
        if self.verify_rectangular_matrix(matrix_to_set):
            self._matrix = matrix_to_set[:]
        else:
            raise ValueError('Неверный формат для первого параметра matrix.')

    def get_submatrix(self, start_index: Tuple[int, int], horizontal_size: int, vertical_size: int):
        start_index_y, start_index_x = start_index  # y - number of list, x - element in this list
        submatrix = [self.matrix[list_number][start_index_x: start_index_x + horizontal_size]
                     for list_number in range(start_index_y, start_index_y + vertical_size)]

        return submatrix

    def get_max_element_of_submatrix(self,
                                     start_index: Tuple[int, int],
                                     horizontal_size: int,
                                     vertical_size: int,):
        start_index_y, start_index_x = start_index

        if start_index_y + vertical_size > len(self.matrix):
            return None
        elif start_index_x + horizontal_size > len(self.matrix[start_index_y]):
            return None

        submatrix = self.get_submatrix((start_index_y, start_index_x), horizontal_size, vertical_size)
        max_element_of_submatrix = max(map(max, submatrix))

        return max_element_of_submatrix


class MaxPooling:

    def __init__(self, step: Tuple[int, int] = (2, 2), size: Tuple[int, int] = (2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix: List[List]):
        triangular_matrix = TriangularMatrix(matrix)

        count_of_columns = len(matrix[0])
        count_of_rows = len(matrix)
        horizontal_step, vertical_step = self.step
        horizontal_size, vertical_size = self.size

        result_matrix: List[List] = []

        for i in range(0, count_of_rows, vertical_step):
            result_of_row = [max_e for j in range(0, count_of_columns, horizontal_step)
                             if (max_e := triangular_matrix.get_max_element_of_submatrix((i, j),
                                                                                         horizontal_size,
                                                                                         vertical_size)) is not None]
            if result_of_row:
                result_matrix.append(result_of_row)

        return result_matrix


mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
