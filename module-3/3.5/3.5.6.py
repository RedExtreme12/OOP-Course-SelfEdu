class Morph:

    def __init__(self, *words):
        self._words = list((word.lower() for word in words))

    def add_word(self, word: str):
        self._words.append(word)

    def get_words(self):
        return tuple(self._words)

    def __eq__(self, other: str):
        return other.lower() in self._words


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'
                    ),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'
                    ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                             )]

text = input()
text_for_find = [word.strip('–?!,.;') for word in text.split() if word.strip('–?!,.;') != '']

number_of_occurrences = 0
for word in text_for_find:
    for morph in dict_words:
        if word == morph:
            number_of_occurrences += 1

print(number_of_occurrences)
