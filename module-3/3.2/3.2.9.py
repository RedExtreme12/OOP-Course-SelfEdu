class InputDigits:

    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        result = self.__func()
        return list(map(int, result.split(' ')))


@InputDigits
def input_dg():
    return input()


res = input_dg()
