class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        object_copy = super().__new__(type(self))  # type(self) – will return the class from
        # which the self object was created
        object_copy.__dict__.update(self.__dict__)
        return object_copy


pt = Point(1, 5)
pt_clone = pt.clone()
