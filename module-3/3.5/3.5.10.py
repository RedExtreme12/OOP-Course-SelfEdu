from typing import Union


class Thing:

    def __init__(self, name: str, mass: Union[int, float]):
        self.name = name
        self.mass = mass

    def __eq__(self, other: 'Thing'):
        return self.mass == other.mass and self.name.lower() == other.name.lower()

    def __hash__(self):
        return hash(self.name.lower()) + hash(self.mass)


class Box:

    def __init__(self):
        self.things = []

    def add_thing(self, obj: Thing):
        self.things.append(obj)

    def get_things(self):
        return self.things

    def __eq__(self, other: 'Box'):
        if set(self.things) != set(other.things):
            return False
        return True


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True
print(res)
