from string import ascii_lowercase, digits


class TextInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name: str, size: int = 10):
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError('некорректное поле name')
        self.size = size

    @classmethod
    def check_name(cls, name):
        len_name_condition = 3 <= len(name) <= 50
        character_validity = [True if char in cls.CHARS_CORRECT else False for char in name]

        if all((len_name_condition, *character_validity)):
            return True
        else:
            return False

    def get_html(self):
        html_string = "<p class='login'>{name}: <input type='text' size={size} />"
        return html_string.format(name=self.name, size=self.size)


class PasswordInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self, name: str, size: int = 10):
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError('некорректное поле name')
        self.size = size

    @classmethod
    def check_name(cls, name):
        len_name_condition = 3 <= len(name) <= 50
        character_validity = [True if char in cls.CHARS_CORRECT else False for char in name]

        if all((len_name_condition, *character_validity)):
            return True
        else:
            return False

    def get_html(self):
        html_string = "<p class='password'>{name}: <input type='text' size=<{size}> />"
        return html_string.format(name=self.name, size=self.size)


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)
