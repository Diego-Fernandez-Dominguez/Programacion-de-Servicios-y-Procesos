from Ejercicio3 import *

coord1=Punto(2, 4)

coord2=Punto(4, 1)

print("Coord1 antes: " + coord1.__str__())

coord1.desplaza(1, -1)

print("Coord1 despues: " + coord1.__str__())

print("Coord2: " + coord2.__str__())

print("Distancia entre coord1 y coord2: " + coord1.distancia(coord2))