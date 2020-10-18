class PettingZoo:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "cute n cuddly SLOTHTIME HIGS AND KISSES"
        self.animals = list() # like declaring an empty array in JS

class SnakePit:
    def __init__(self, name):
        self.attraction_name = name
        self.description = "HSSSSSSS"
        self.animals = list()
    def __str__(self):
        animalStrings = list()
        for animal in self.animals:
            animalStrings.append(f"{animal.name} the {animal.species}")   
        return f"{self.attraction_name} is where you'll find {self.description} like {str(animalStrings).strip('[]')}"

class Wetlands: 
    def __init__(self, name):
        self.attraction_name = name
        self.description = "Get in da swamp yo"
        self.animals = list()