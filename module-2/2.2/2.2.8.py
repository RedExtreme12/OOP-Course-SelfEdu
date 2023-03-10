class TreeObj:

    def __init__(self, indx, value=None):
        self.indx = indx  # индекса массива x
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, new_node: 'TreeObj'):
        self.__left = new_node

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, new_node: 'TreeObj'):
        self.__right = new_node


class DecisionTree:

    @classmethod
    def predict(cls, root, x):
        obj = root
        while obj:
            obj_next = cls.get_next(obj, x)
            if not obj_next:
                break
            obj = obj_next

        return obj.value

    @classmethod
    def add_obj(cls, obj, node=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj

        return obj

    @classmethod
    def get_next(cls, obj, x):
        if x[obj.indx] == 1:
            return obj.left
        return obj.right

