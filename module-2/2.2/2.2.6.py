from typing import Union, Tuple, Any


class StackObj:

    def __init__(self, data, next_element=None):
        self.__data = data
        self.__next = next_element

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj: 'StackObj'):
        if isinstance(obj, (self.__class__, type(None))):
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class Stack:

    def __init__(self, first_element: StackObj = None):
        self.top = first_element

    def _get_last_element(self) -> Union[StackObj, None]:
        current_obj = self.top

        if not current_obj:
            return None

        while current_obj.next is not None:
            current_obj = current_obj.next

        return current_obj

    def _get_pair_from_last_and_previous_element(self) -> Tuple[StackObj, StackObj] or None:
        current_obj = self.top

        if current_obj is None:
            return None

        previous_element = None
        while True:
            if current_obj.next is None:
                return current_obj, previous_element

            previous_element = current_obj
            current_obj = current_obj.next

    def push(self, obj: StackObj):
        if not self.top:
            self.top = obj
        else:
            previous_element = self._get_last_element()
            if previous_element:
                previous_element.next = obj

    def pop(self):
        last_element, previous_of_last_element = self._get_pair_from_last_and_previous_element()

        if last_element is self.top:
            self.top = None
            return last_element
        else:
            previous_of_last_element.next = None
            return last_element

    def get_data(self):
        current_obj = self.top

        result = []
        while current_obj:
            result.append(current_obj.data)
            current_obj = current_obj.next

        return result
