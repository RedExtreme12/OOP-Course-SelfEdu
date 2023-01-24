class Clock:

    def __init__(self, tm=0):
        self.__time = tm if self.__check_time(tm) else 0

    @classmethod
    def __check_time(cls, tm) -> bool:
        if type(tm) is int and 0 <= tm < 100_000:
            return True
        return False

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock(4530)
