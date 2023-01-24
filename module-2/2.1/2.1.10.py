from random import randint
from string import ascii_lowercase


class EmailValidator:

    VALID_NUMBERS = ''.join([ascii_lowercase, '123456789', '_.'])
    EMAIL_SERVICE = '@gmail.com'
    MAX_SYMBOLS_BEFORE_AT = 100  # before @
    MAX_SYMBOLS_AFTER_AT = 50  # after @

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email: str) -> bool:
        if not cls.__is_email_str(email):
            return False
        elif email.count('@') > 1:
            return False
        elif '..' in email:
            return False
        elif set(cls.VALID_NUMBERS) < set(email):
            return False

        email_before_at, email_after_at = email.split('@')

        if email_after_at.count('.') < 1:
            return False
        elif len(email_before_at) > cls.MAX_SYMBOLS_BEFORE_AT or len(email_after_at) > cls.MAX_SYMBOLS_AFTER_AT:
            return False

        return True

    @classmethod
    def get_random_email(cls) -> str:
        mail_service = cls.EMAIL_SERVICE
        count_of_symbols_before_at = randint(0, cls.MAX_SYMBOLS_BEFORE_AT - len(mail_service))

        symbols_to_at = [cls.VALID_NUMBERS[randint(0, len(cls.VALID_NUMBERS) - 1)]
                         for _ in range(count_of_symbols_before_at)]
        symbols_to_at = ''.join(symbols_to_at)

        return symbols_to_at + mail_service

    @staticmethod
    def __is_email_str(email: str):
        if type(email) is str:
            return True
        return False
