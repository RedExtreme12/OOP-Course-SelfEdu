from typing import Any, List


def check_is_str(s: Any) -> bool:
    return isinstance(s, str)


def check_is_int(n: Any) -> bool:
    return isinstance(n, int) and n > 0


class LessonItem:

    TYPES = {
        'title': check_is_str,
        'practices': check_is_int,
        'duration': check_is_int,
    }

    def __init__(self, name: str, count_of_practice_lessons: int, total_time_of_lesson: int):
        self.title = name
        self.practices = count_of_practice_lessons
        self.duration = total_time_of_lesson

    def __setattr__(self, key, value):
        is_corrected_type = self.TYPES[key](value)

        if is_corrected_type:
            object.__setattr__(self, key, value)
        else:
            raise TypeError('Неверный тип присваиваемых данных.')

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in self.TYPES.keys():
            object.__delattr__(self, item)


class Module:

    def __init__(self, name: str):
        self.name = name
        self.lessons: List[LessonItem] = []

    def add_lesson(self, lesson: LessonItem):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)


class Course:

    def __init__(self, name: str):
        self.name = name
        self.modules: List[Module] = []

    def add_module(self, module: Module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)

