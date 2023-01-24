class ObjListDescriptor:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__name'

    def __set__(self, instance, value):
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class ObjList:

    data = ObjListDescriptor()
    prev = ObjListDescriptor()
    next = ObjListDescriptor()

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head: ObjList | None = None
        self.tail: ObjList | None = None
        self.__length: int = 0

    def add_obj(self, obj: ObjList):
        if not self.head:
            self.head = obj
        elif self.head and not self.tail:
            self.tail = obj
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            prev_tail = self.tail

            self.tail = obj
            self.tail.prev = prev_tail
            prev_tail.next = self.tail

        self.__length += 1

    def _find_node_by_index(self, indx: int) -> ObjList:
        current_obj = self.head

        for i in range(indx):
            current_obj = current_obj.next

        return current_obj

    def remove_obj(self, indx: int):
        obj_to_remove = self._find_node_by_index(indx)

        if self.__length == 1:
            self.tail = self.head = None
        elif obj_to_remove is self.head:
            next_element = self.head.next
            if next_element:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
        elif obj_to_remove is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev_obj: ObjList = obj_to_remove.prev
            next_obj: ObjList = obj_to_remove.next

            prev_obj.next = next_obj

            if next_obj:
                next_obj.prev = prev_obj

        self.__length -= 1

    def __call__(self, indx: int):
        return self._find_node_by_index(indx).data

    def __len__(self):
        return self.__length


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(0)
ln.remove_obj(0)
ln.remove_obj(0)
