import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data) -> None:
        for row in data:
            record_id, name, old, salary = row.split(' ')
            self.lst_data.append(
                {
                    self.FIELDS[0]: record_id,
                    self.FIELDS[1]: name,
                    self.FIELDS[2]: old,
                    self.FIELDS[3]: salary,
                }
            )

    def select(self, a, b):
        return self.lst_data[a:b + 1]


db = DataBase()
db.insert(lst_in)
print(db.select(1, 10))
