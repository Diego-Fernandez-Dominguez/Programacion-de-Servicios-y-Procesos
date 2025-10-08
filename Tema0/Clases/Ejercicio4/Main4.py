from Ejercicio4 import *

prod1 = Articulo("Llamas sombrias", 300, 5)

prod2 = Articulo("Agujolin", 50, 27)

print(prod1.__str__())

print(prod1.getPVP())

prod1.venderArticulo(3)

print("Despues de vender: " + prod1.__str__())

prod1.almacenarArticulo(124)

print("Despues de comprar: " + prod1.__str__())

print(prod2.__str__())

print("Son iguales: " + str(prod1.__eq__(prod2)))