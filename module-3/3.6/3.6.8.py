import sys


class BookStudy:

    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name, self.author.lower()))


lst_in = list(map(str.strip, sys.stdin.readlines()))
splitted_records = (record.split('; ') for record in lst_in)
lst_bs = [BookStudy(name=record[0], author=record[1], year=int(record[2])) for record in splitted_records]
unique_books = len({hash(obj) for obj in lst_bs})
