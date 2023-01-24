class Thing:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__total_weight = 0
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        if thing.weight + self.get_total_weight() <= self.max_weight:
            self.things.append(thing)
            self.__total_weight += thing.weight

    def remove_thing(self, indx):
        del self.things[indx]

    def get_total_weight(self):
        return self.__total_weight

