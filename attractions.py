class Attraction:
    def __init__(self, name):
        self.attraction_name = name
        self.description = None
        self.animals = list()
    def __str__(self):
        animalStrings = list()
        for animal in self.animals:
            animalStrings.append(f" * {animal.name} the {animal.species}")
        animalList = ('\n'.join(animalStrings))       
        return f"{self.attraction_name} is where you'll find {self.description} like \n{animalList}"

class PettingZoo(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "cute n cuddly SLOTHTIME HUGS AND KISSES"

class SnakePit(Attraction):
    def __init__(self, name):
        super().__init__(name)
        self.description = "slithery serpentine sneakyboys"

class Wetlands: 
    def __init__(self, name):
        super().__init__(name)
        self.description = "Get in da swamp yo"
