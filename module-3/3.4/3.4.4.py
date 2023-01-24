import copy


class NewList:

    def __init__(self, lst=None):
        self.lst = lst[:] if lst else []

    @staticmethod
    def _delete_all_equal_elements(lst_1, lst_2):
        for element in lst_2:
            try:
                index_of_element = lst_1.index(element)
            except ValueError:
                continue

            if type(lst_1[index_of_element]) == type(element):
                lst_1.pop(index_of_element)

    def __sub__(self, other):
        other_lst = other

        if isinstance(other, NewList):
            other_lst = other_lst.lst

        other_lst = ((element, type(element)) for element in copy.deepcopy(other_lst))
        self_lst_copied = [(element, type(element)) for element in copy.deepcopy(self.lst)]

        self._delete_all_equal_elements(self_lst_copied, other_lst)
        self_lst_copied = [pair[0] for pair in self_lst_copied]

        return NewList(self_lst_copied)

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        return self.lst


# # lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# # res_1 = lst1 - lst2 # NewList: [-4, 6, 10, 11, 15, False]
# # print(res_1.get_list())
#
# # lst1 -= lst2 # NewList: [-4, 6, 10, 11, 15, False]
# # print(lst1.get_list())
#
# res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
# print(lst2.lst, res_2.get_list())
# #
# # res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# # print(res_3.get_list())
# #
# # a = NewList([2, 3])
# # res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# # print(res_4.get_list())
