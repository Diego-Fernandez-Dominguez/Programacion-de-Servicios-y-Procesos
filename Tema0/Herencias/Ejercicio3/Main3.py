from Perecedero import Perecedero
from NoPerecedero import NoPerecedero

pere= Perecedero("Manzana Dorada", 50, 2)
no_pere = NoPerecedero("Striker", 409, "Salvadora")

print(pere.__str__())
print(no_pere.__str__())

print(pere.calcular(4))
print(no_pere.calcular(2))