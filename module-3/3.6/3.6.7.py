import sys
from collections import defaultdict


class Record:

    total_records = 0

    def __new__(cls, *args, **kwargs):
        new_records: 'Record' = super().__new__(cls)

        setattr(new_records, 'pk', cls.total_records)
        cls.total_records += 1

        return new_records

    def __init__(self, fio: str, descr: str, old: int):
        self.fio = fio
        self.descr = descr
        self.old = old

    def __members(self):
        return self.fio, self.old

    def __hash__(self):
        return hash(self.__members())

    def __eq__(self, other: 'Record'):
        return hash(self) == hash(other)


class DataBase:

    def __init__(self, path_: str):
        self.dict_db = defaultdict(list)
        self._path = path_

    def write(self, record: Record):
        self.dict_db[record].append(record)

    def read(self, pk: int):
        for record_values in self.dict_db.values():
            for record_value in record_values:
                if record_value.pk == pk:
                    return record_value


db = DataBase('test')
lst_in = list(map(str.strip, sys.stdin.readlines()))
for record_ in lst_in:
    name, prof, age = record_.split('; ')
    db.write(Record(name, prof, int(age)))
