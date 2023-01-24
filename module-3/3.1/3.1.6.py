class Picture:

    def __init__(self, name: str, author: str, descr: str):
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:

    def __init__(self, name: str, location: str, descr: str):
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:

    def __init__(self, name: str, date: str, descr: str):
        self.name = name
        self.date = date
        self.descr = descr


class Museum:

    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        obj = self.exhibits[indx]
        return f'Описание экспоната {obj.name}: {obj.descr}'

