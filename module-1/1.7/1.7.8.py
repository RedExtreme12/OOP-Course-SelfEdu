import re


class CardCheck:

    pattern_card_number = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    pattern_name = r'^[A-Z]+\s[A-Z]+$'

    @classmethod
    def check_card_number(cls, number):
        pattern = re.compile(cls.pattern_card_number)
        return bool(re.search(pattern, number))

    @classmethod
    def check_name(cls, name):
        pattern = re.compile(cls.pattern_name)
        return bool(re.search(pattern, name))


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
