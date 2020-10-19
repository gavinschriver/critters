from slithering import Rattlesnake, Copperhead
from walking import Billygoat, Sloth, Cougar
from attractions import PettingZoo, SnakePit, Wetlands
from animals import Conrad

Ronnie = Rattlesnake("Ronnie", "Rattleman", "Morning Noon and Night", "Crickets I think")
Coolio = Copperhead("Coolio", "Copperhead", "Late at night", "little childrens' ankles")
Camila = Cougar("Camilla", "Cougar", "Whenever there's FRESH BLOOD", "Those young studs")


SlitherInn = SnakePit("Slither Inn")
CritterTown = PettingZoo("Critter Town")


SlitherInn.animals.append(Ronnie)
SlitherInn.animals.append(Coolio)
CritterTown.animals.append(Conrad)

print(SlitherInn)
print(CritterTown)
