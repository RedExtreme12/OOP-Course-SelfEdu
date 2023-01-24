from typing import Tuple


class Point:

    def __init__(self, x, y):
        self.__x = x if self.__check_coord(x) else 0
        self.__y = y if self.__check_coord(y) else 0

    @classmethod
    def __check_coord(cls, x) -> bool:
        if type(x) in (int, float):
            return True
        return False

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:

    POINTS_OBJECT_ARGS_LEN = 2
    POINTS_NUMBERS_ARGS_LEN = 4

    def __init__(self, *args):
        point_1, point_2 = self.__transform_to_points_objects(*args)
        self.__sp: Point = point_1
        self.__ep: Point = point_2

    @classmethod
    def __check_is_numbers_types(cls, points):
        is_numbers_objects = all(tuple(map(lambda x: type(x) in (int, float), points)))
        return is_numbers_objects

    @classmethod
    def __check_is_point_types(cls, points):
        is_points_objects = all(tuple(map(lambda x: type(x) is Point, points)))
        return is_points_objects

    @classmethod
    def __transform_to_points_objects(cls, *args) -> Tuple[Point, Point]:
        if len(args) == cls.POINTS_OBJECT_ARGS_LEN and cls.__check_is_point_types(args):
            point_1, point_2 = args

            return point_1, point_2
        elif len(args) == cls.POINTS_NUMBERS_ARGS_LEN and cls.__check_is_numbers_types(args):
            x1, y1, x2, y2 = args
            point_1 = Point(x1, y1)
            point_2 = Point(x2, y2)

            return point_1, point_2
        else:
            raise ValueError('Incorrect count or type of points')

    def set_coords(self, sp, ep):
        point_1, point_2 = self.__transform_to_points_objects(sp, ep)
        self.__sp = point_1
        self.__ep = point_2

    def get_coords(self) -> Tuple[Point, Point]:
        return self.__sp, self.__ep

    def draw(self):
        point_1, point_2 = self.get_coords()
        result = 'Прямоугольник с координатами: {0} {1}'.format(point_1.get_coords(), point_2.get_coords())
        print(result)


rect = Rectangle(0, 0, 20, 34)
