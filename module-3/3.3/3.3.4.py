class WordString:

    def __init__(self, string: str = ''):
        self.__string = None
        self.string = string
        self.words = string

    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, value: str):
        self.__string = value
        self.__words = value.split()

    def __len__(self) -> int:
        return len(self.__words)

    def __call__(self, indx: int) -> str:
        return self.__words[indx]


words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")
