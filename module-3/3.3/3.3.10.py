class PolyLine:

    def __init__(self, *args):
        self.coords = [*args]

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def get_coords(self):
        return self.coords

    def remove_coord(self, indx):
        self.coords.pop(indx)
