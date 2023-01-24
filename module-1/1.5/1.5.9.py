import sys


class ListObject:

    amount = 0

    def __init__(self, data, next_obj=None):
        self.data: str = data
        self.next_obj = next_obj

    def link(self, obj):
        ListObject.amount += 1
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])
current_obj = head_obj

for lst_element in lst_in[1:]:
    current_obj.link(ListObject(
        lst_element
    ))
    current_obj = current_obj.next_obj

print(ListObject.amount)
