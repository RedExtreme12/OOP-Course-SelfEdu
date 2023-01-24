from typing import List


class Ingredient:

    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:

    def __init__(self, *args: List[Ingredient]):
        self.ingredients = [*args]

    def add_ingredient(self, ing: Ingredient):
        self.ingredients.append(ing)

    def remove_ingredient(self, ing):
        self.ingredients.remove(ing)

    def get_ingredients(self):
        return tuple(self.ingredients)

    def __len__(self):
        return len(self.ingredients)


recipe = Recipe()
recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
ings = recipe.get_ingredients()
n = len(recipe) # n = 3
print(ings, n)

