from angler import Angler
from bass import Bass
from cougar import Cougar
from copperhead import Copperhead
from pufferfish import Pufferfish
from rattlesnake import Rattlesnake
from sloth import Sloth
# from boa import Boa
from attractions import PettingZoo, SnakePit, Wetlands

SlitherInn = SnakePit("Slither Inn")
Ronnie = Rattlesnake("Ronnie", "Rattleman", "Morning Noon and Night", "Crickets I think")
SlitherInn.animals.append(Ronnie)
print(SlitherInn)