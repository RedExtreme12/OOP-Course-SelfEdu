class ValidateString:

    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string) -> bool:
        if isinstance(string, str) and self.min_length <= len(string) <= self.max_length:
            return True
        return False


class StringValue:

    def __init__(self, validator: ValidateString):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)
        else:
            pass

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class RegisterForm:
    login = StringValue(validator=ValidateString())
    password = StringValue(validator=ValidateString())
    email = StringValue(validator=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def show(self):
        html_string = f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}</form>'

    def get_fields(self):
        return [self.login, self.password, self.email]


rf = RegisterForm('Bo00', 'FooBar', 'BuzFuz')
print(rf.__dict__)
rf.show()
print(rf.get_fields())
rf = RegisterForm('B0', 42, 'BuzFuz')
print(rf.__dict__)
