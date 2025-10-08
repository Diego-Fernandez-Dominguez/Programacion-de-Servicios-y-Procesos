class Producto:
    
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def calcular(self, cantidad):
        return self.precio*cantidad
    
    def __lt__(self, producto):
        menor=False
        if self.nombre < producto.nombre:
              menor=True
        return menor
    
    def __str__(self):
        cadena= f"{self.nombre} - {self.precio}€" #como no me he acordado de esta barbaridad
        return cadena