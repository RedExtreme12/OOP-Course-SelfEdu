class DigitRetrieve:

    def __call__(self, number_string: str):
        if '-' in number_string:
            if number_string[1:].isdigit():
                return int(number_string)
        else:
            if number_string.isdigit():
                return int(number_string)
        return None
