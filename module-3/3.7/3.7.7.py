class Ellipse:
    point_attrs = ('x1', 'y1', 'x2', 'y2')

    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if all(map(lambda x: x is not None, (x1, y1, x2, y2))):
            for attr, value_to_set in zip(self.point_attrs, (x1, y1, x2, y2)):
                setattr(self, attr, value_to_set)

    def __bool__(self):
        for attr in self.point_attrs:
            if not getattr(self, attr, False):
                return False
        return True

    def get_coords(self):
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        return tuple(getattr(self, attr) for attr in self.point_attrs)


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for ellipse_obj in lst_geom:
    if ellipse_obj:
        ellipse_obj.get_coords()
