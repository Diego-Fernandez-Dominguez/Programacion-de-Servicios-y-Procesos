from Producto import Producto

class Perecedero(Producto):

    def __init__(self, nombre, precio, dias_caducar):
        super().__init__(nombre, precio)
        self.dias_caducar=dias_caducar

    def calcular(self,cantidad):
        price=self.precio*cantidad

        if self.dias_caducar==1:
            final=price/4
        elif self.dias_caducar==2:
            final=price/3
        elif self.dias_caducar==3:
            final=price/2

        return final
    
    def __str__(self):
        return super().__str__() + f" - {self.dias_caducar} dias para que caduque"