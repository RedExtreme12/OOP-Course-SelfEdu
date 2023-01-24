import sys
from typing import List


class MailItem:

    def __init__(self, mail_from: str, title: str, content: str):
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read: bool):
        self.is_read = fl_read

    def __bool__(self):
        return self.is_read


class MailBox:

    def __init__(self):
        self.inbox_list: List[MailItem] = []

    def receive(self):
        lst_in = (string.split('; ') for string in map(str.strip, sys.stdin.readlines()))
        lst_in = [MailItem(mail_from=mail_string[0], title=mail_string[1], content=mail_string[2])
                  for mail_string in lst_in]
        self.inbox_list.extend(lst_in)


mail = MailBox()
mail.receive()
mail.inbox_list[0].set_read(True)
mail.inbox_list[-1].set_read(True)
inbox_list_filtered = list(filter(bool, mail.inbox_list))
