class Clock:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def convert_time_from_seconds(total_seconds: int):
        minutes = total_seconds // 60 % 60
        hours = total_seconds // 3600
        seconds = total_seconds % 60

        return hours, minutes, seconds

    def __sub__(self, other: 'Clock'):
        difference = self.get_time() - other.get_time()

        if difference < 0:
            return Clock(0, 0, 0)

        hours, minutes, seconds = self.convert_time_from_seconds(difference)

        return Clock(hours, minutes, seconds)


class DeltaClock:

    def __init__(self, clock_1: Clock, clock_2: Clock):
        self.difference_clock_obj: Clock = clock_1 - clock_2

    def __str__(self):
        hours = self.difference_clock_obj.hours
        minutes = self.difference_clock_obj.minutes
        seconds = self.difference_clock_obj.seconds

        return f'{hours:02}: {minutes:02}: {seconds:02}'

    def __len__(self) -> int:
        return self.difference_clock_obj.get_time()
