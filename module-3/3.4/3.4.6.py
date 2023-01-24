from typing import Any, List


class StackObj:
    def __init__(self, data: Any, _next: 'StackObj' = None):
        self.__data = data
        self.__next = _next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, _next):
        self.__next = _next

    @property
    def data(self):
        return self.__data


class Stack:

    def __init__(self):
        self.top: StackObj | None = None
        self.prev_obj: StackObj | None = None

    def get_last_element(self):
        current = self.top
        if not current:
            return None

        while current.next:
            current = current.next

        return current

    def push_back(self, obj: StackObj):
        if not self.top:
            self.top = obj
        else:
            last_element = self.get_last_element()
            last_element.next = obj

            self.prev_obj = last_element

    def pop_back(self):
        self.prev_obj.next = None

    def __add__(self, obj: StackObj):
        self.push_back(obj)
        return self

    def __mul__(self, datas: List[Any]):
        for data in datas:
            self.push_back(StackObj(data))
        return self


st = Stack()

st.push_back(StackObj(1))

print(st.get_last_element().data)
st.pop_back()
print(st.get_last_element().data)
