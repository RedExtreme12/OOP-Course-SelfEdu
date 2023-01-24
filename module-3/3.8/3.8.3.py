from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    speed: float


class Track:

    def __init__(self, start_x: float, start_y: float):
        self.start_x = start_x
        self.start_y = start_y
        self.points: list[Point] = []

    def check_indices(self, index: int):
        if not isinstance(index, int) or not (0 <= index < len(self.points)):
            raise IndexError('некорректный индекс')

    def add_point(self, x, y, speed):
        self.points.append(Point(x, y, speed))

    def __getitem__(self, item: int):
        self.check_indices(item)
        point = self.points[item]
        return (point.x, point.y), point.speed

    def __setitem__(self, key: int, speed: float):
        self.check_indices(key)
        self.points[key].speed = speed


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)
