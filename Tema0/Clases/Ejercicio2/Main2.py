from Ejercicio2 import *


book1 = Libro("LenguaParaTontos", "Euseboi", 10, 2)
print(book1.__str__())

book1.prestamo(3)
print(book1.__str__())

book1.devolucion(2)
print(book1.__str__())

book2 = Libro("LenguaParaTontos", "Euseboi", 5, 1)
print(book1.__eq__(book2))

book3 = Libro("GuiaParaSerUnMaestroDelHvsF", "Adrian Diaz Sanchez", 7, 0)
print(book3.__lt__(book1))

