class Telecast:

    def __init__(self, uid, name, duration):
        self.__id = uid
        self.__name = name
        self.__duration = duration

    @property
    def uid(self):
        return self.__id

    @uid.setter
    def uid(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value


class TVProgram:

    def __init__(self, name_of_channel):
        self.name_of_channel = name_of_channel
        self.items = []
        self._items_length = 0
        self._mapped_indexes = {}

    def add_telecast(self, tl: Telecast):
        self.items.append(tl)
        self._mapped_indexes[tl.uid] = self._items_length
        self._items_length += 1

    def remove_telecast(self, indx):
        del self.items[self._mapped_indexes[indx]]
