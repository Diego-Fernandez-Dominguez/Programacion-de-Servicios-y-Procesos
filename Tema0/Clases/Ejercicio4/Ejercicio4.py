class Articulo:

    IVA=0.21

    def __init__(self, nombre, precio, stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    
    def getPVP(self):
        return self.precio-(self.precio*Articulo.IVA)
    
    def getPVPDescuento(self, descuento):
        descTot=descuento/100
        return self.precio-(self.precio*descTot)
    
    def venderArticulo(self, ventas):

        possible=False

        if ventas <= self.stock:
            self.stock-=ventas
            possible=True
        
        return possible
    
    def almacenarArticulo(self, cantidad):

        possible=False

        if cantidad > 0:
            self.stock+=cantidad
            possible=True
        
        return possible
    
    def __eq__(self, articulo):
        equals=False

        if self.nombre == articulo.nombre:
             equals=True

        return equals
    
    def __lt__(self, libro):
        menor = False
        if self.nombre < libro.nombre:
            menor = True
        return menor

    def __str__(self):
        cadena= self.nombre + " - " + str(self.precio) + "€ - Stock: " + str(self.stock)

        return cadena