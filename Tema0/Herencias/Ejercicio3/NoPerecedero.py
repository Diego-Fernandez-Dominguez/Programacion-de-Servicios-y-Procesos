from Producto import Producto

class NoPerecedero(Producto):

    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo=tipo

    def calcular(self, cantidad):
        return super().calcular(cantidad)
    
    def __str__(self):
        return super().__str__() + f" - {self.tipo}"