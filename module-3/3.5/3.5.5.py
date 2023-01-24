from typing import List


class StringText:

    def __init__(self, words_list):
        self.words_list = words_list

    def __len__(self):
        return len(self.words_list)

    def __ge__(self, other: 'StringText'):
        return len(self) >= len(other)

    def __gt__(self, other: 'StringText'):
        return len(self) > len(other)

    def join(self):
        return ' '.join(self.words_list)


class StringSeparator:

    def __init__(self, strings: List[str]):
        self._strings = strings

    @classmethod
    def _separate_string(cls, string: str, symbols: str = None) -> List[str]:
        return string.split(symbols)

    @classmethod
    def _clean_word(cls, word, symbols) -> str:
        return word.strip(symbols)

    def _clean_words_in_string(self, string, symbols) -> StringText:
        return StringText([cleaned_word for word in string if (cleaned_word := self._clean_word(word, symbols)) != ''])

    def separate_strings(self, symbols_for_strip: str = None) -> List[StringText]:
        separated_strings = (self._separate_string(string) for string in self._strings)
        cleaned_separated_strings = [self._clean_words_in_string(string, symbols_for_strip)
                                     for string in separated_strings]
        return cleaned_separated_strings


if __name__ == '__main__':
    stich = ['Я к вам пишу – чего же боле?',
             'Что я могу еще сказать?',
             'Теперь, я знаю, в вашей воле',
             'Меня презреньем наказать.',
             'Но вы, к моей несчастной доле',
             'Хоть каплю жалости храня,',
             'Вы не оставите меня.']

    ss = StringSeparator(stich)
    lst_text = ss.separate_strings('–?!,.;')
    lst_text_sorted = sorted(lst_text, key=lambda obj: obj, reverse=True)
    lst_text_sorted = [string.join() for string in lst_text_sorted]
