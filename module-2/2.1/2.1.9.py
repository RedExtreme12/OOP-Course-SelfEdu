class ObjList:

    def __init__(self, data, next_element=None, prev_element=None):
        self.__data = data
        self.__next = next_element
        self.__prev = prev_element

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
        elif self.head and not self.tail:
            self.tail = obj
            self.tail.set_prev(self.head)
            self.head.set_next(self.tail)
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        if self.tail:
            prev: ObjList = self.tail.get_prev()
            self.tail = prev
            self.tail.get_prev().set_prev(self.tail)
        elif self.head:
            self.head = None

    def get_data(self):
        current_obj: ObjList | None = self.head

        result = []
        while current_obj is not None:
            result.append(current_obj.get_data())
            current_obj = current_obj.get_next()

        return result


