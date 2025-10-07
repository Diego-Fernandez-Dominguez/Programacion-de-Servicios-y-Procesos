class Articulo:

    IVA=0.21

    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        #self.IVA=0.21
    
    def getPVP(self):
        return self.precio*Articulo.IVA