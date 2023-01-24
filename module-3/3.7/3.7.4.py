import sys


class Player:

    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0

    def __str__(self):
        return str(self.score)


lst_in = [string.split('; ') for string in (map(str.strip, sys.stdin.readlines()))]
players = [Player(person_string[0], int(person_string[1]), int(person_string[2])) for person_string in lst_in]
players_filtered = list(filter(bool, players))