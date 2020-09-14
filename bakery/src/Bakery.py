from src.Baker import Baker
from src.Pastry import Pastry


class Bakery:
    """Class bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Class constructor."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.recipes = {}
        self.bakers = []
        self.pastries = []

    def add_baker(self, baker: Baker) -> Baker:
        """Add baker."""
        if baker.experience_level >= self.min_experience_level:
            self.bakers.append(baker)
            return baker

    def remove_baker(self, baker: Baker):
        """Remove baker."""
        self.bakers.remove(baker)

    def add_recipe(self, name: str):
        """Add recipe."""
        complexity = abs(len(name) *
                         len(self.bakers) - self.min_experience_level)
        self.recipes[name] = complexity
        self.budget -= len(name)

    def make_order(self, name: str) -> Pastry:
        """Make order."""
        complexity = abs(len(name) *
                         len(self.bakers) - self.min_experience_level)
        if name in self.recipes:
            for bakers in self.bakers:
                b = [bakers for bakers in self.bakers]
            baker = b[0]
            baker1 = b[1]
            if baker.experience_level < complexity:
                baker = baker1
            # print(baker.experience_level)
            baker.experience_level += len(name)
            self.budget += len(name) * 2
            baker.money += len(name) * 2
            self.pastries.append(Pastry(name, len(name)))
            return self.pastries

    def get_recipes(self) -> dict:
        """Get recipes."""
        for x, y in self.recipes.items():
            print(x, y)

    def get_pastries(self) -> list:
        """Get pastries."""
        return self.pastries

    def get_bakers(self) -> list:
        """Get baker."""
        return self.bakers

    def __str__(self):
        """Represent object in string format."""
        return "Bakery {}: {} baker(s)".format(self.name, len(self.bakers))
