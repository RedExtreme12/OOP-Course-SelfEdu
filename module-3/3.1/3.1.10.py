import time


class Mechanical:

    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return None

    def __setattr__(self, key, value):
        if getattr(self, key) is None:
            object.__setattr__(self, key, value)


class Aragon:

    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return None

    def __setattr__(self, key, value):
        if getattr(self, key) is None:
            object.__setattr__(self, key, value)


class Calcium:

    def __init__(self, date):
        self.date = date

    def __getattr__(self, item):
        return None

    def __setattr__(self, key, value):
        if getattr(self, key) is None:
            object.__setattr__(self, key, value)


class GeyserClassic:

    MAX_DATE_FILTER = 100

    SLOTS_TYPES = {
        1: (Mechanical, ),
        2: (Aragon, ),
        3: (Calcium, ),
    }

    SLOTS = {
        1: 'slot_1',
        2: 'slot_2',
        3: 'slot_3',
    }

    def __init__(self):
        self.slot_1 = None
        self.slot_2 = None
        self.slot_3 = None

    def add_filter(self, slot_num: int, _filter):
        filter_type = self.SLOTS_TYPES[slot_num]

        slot = getattr(self, self.SLOTS[slot_num])

        if not slot and isinstance(_filter, filter_type):
            setattr(self, self.SLOTS[slot_num], _filter)

    def remove_filter(self, slot_num):
        setattr(self, self.SLOTS[slot_num], None)

    def get_filters(self):
        return self.slot_1, self.slot_2, self.slot_3

    def water_on(self):
        if all((self.slot_1, self.slot_2, self.slot_3)) and \
                all(map(lambda x: (time.time() - x.date) < self.MAX_DATE_FILTER,
                        (self.slot_1, self.slot_2, self.slot_3))):
            return True
        return False
