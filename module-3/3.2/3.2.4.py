class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name
        self.validators = validators
        self.login = ""
        self.password = ""

    def post(self, request):
        self.login = request.get('login', "")
        self.password = request.get('password', "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:

    def __init__(self, min_length, max_length):
        self._min_length = min_length
        self._max_length = max_length

    def __call__(self, string):
        if self._min_length <= len(string) <= self._max_length:
            return True
        return False


class CharsValidator:

    def __init__(self, chars):
        self._chars = set(chars)

    def __call__(self, string):
        if set(string) <= self._chars:
            return True
        return False

