import random
from itertools import repeat


# def get_random_password


class RandomPassword:

    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self._psw_chars = psw_chars
        self._min_length = min_length
        self._max_length = max_length

    def __call__(self, *args, **kwargs):
        random_length = random.randint(self._min_length, self._max_length)
        password = (random.choice(self._psw_chars) for _ in range(random_length))

        return ''.join(password)


min_l = 10000000000
max_l = 10000000002
psw_chrs = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

lst_pass = [RandomPassword(psw_chrs, min_l, max_l)() for _ in range(3)]

print(lst_pass)

