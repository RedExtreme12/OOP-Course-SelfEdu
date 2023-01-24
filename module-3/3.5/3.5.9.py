from typing import Union


class Body:

    def __init__(self, name: str, ro: Union[int, float], volume: Union[int, float]):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_mass(self):
        return self.volume * self.ro

    def __gt__(self, other: Union['Body', int, float]):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() > other

    def __lt__(self, other):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() < other

    def __eq__(self, other: Union['Body', int, float]):
        if isinstance(other, Body):
            other = other.get_mass()
        return self.get_mass() == other


body1 = Body('body1', 10, 10)
print(body1 < 10)
