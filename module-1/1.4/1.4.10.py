class Translator:

    vocabulary = {}

    def add(self, eng, rus):
        if eng not in self.vocabulary:
            self.vocabulary[eng] = [rus]
        else:
            self.vocabulary[eng].append(rus)

    def remove(self, eng):
        del self.vocabulary[eng]

    def translate(self, eng):
        return self.vocabulary.get(eng)


tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')

print(tr.__dict__)

print(' '.join(tr.translate('go')))
print(getattr(tr, 'vocabulary'))
print(hasattr(tr, 'vocabulary'))
