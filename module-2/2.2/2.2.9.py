import math


class LineTo:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PathLines:

    def __init__(self, *args):
        self.__path_lines = []
        if args:
            self.path_lines = args

    @property
    def path_lines(self):
        return self.__path_lines

    @path_lines.setter
    def path_lines(self, args):
        if not self.__path_lines:
            self.__path_lines.append(LineTo(0, 0))
            self.__path_lines.extend(args)
        else:
            self.__path_lines.extend(args)

    def get_path(self):
        return self.path_lines

    def add_line(self, line: LineTo):
        self.path_lines = [line]

    @staticmethod
    def get_euclidian_distance(line_1: LineTo, line_2: LineTo):
        return math.sqrt((line_2.x - line_1.x) ** 2 + (line_2.y - line_1.y) ** 2)

    def get_length(self):
        return sum([self.get_euclidian_distance(line_1, line_2)
                    for line_1, line_2 in zip(self.path_lines[:-1], self.__path_lines[1:])])
