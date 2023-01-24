import random


min_l = 5
max_l = 20
psw_chrs = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"


def get_random_number(psw_chars: str, min_length: int, max_length: int):
    def wrapper():
        random_length = random.randint(min_length, max_length)
        password = (random.choice(psw_chars) for _ in range(random_length))

        return ''.join(password)

    return wrapper


lst_pass = [get_random_number(psw_chrs, min_l, max_l)() for _ in range(3)]

print(lst_pass)
