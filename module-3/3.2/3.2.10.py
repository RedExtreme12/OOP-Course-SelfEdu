
class RenderDigit:

    def __call__(self, string_data):
        if '-' in string_data and string_data[1:].isdigit():
            return int(string_data)
        elif string_data.isdigit():
            return int(string_data)
        return None


class InputValues:

    def __init__(self, render):
        self.__render = render

    def __call__(self, func):
        def wrapper():
            inputed_value = func()
            result = list(map(self.__render, inputed_value.split(' ')))

            return result
        return wrapper


r1 = RenderDigit()


@InputValues(render=r1)
def input_dg():
    return input()


res = input_dg()
