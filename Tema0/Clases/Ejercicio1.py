class CuentaCorriente:

    def __init__(self, DNI, saldo):
            self.DNI=DNI
            self.nombre=""
            self.saldo=saldo

    def __init__(self, DNI, nombre, saldo):
        self.DNI=DNI
        self.nombre=nombre
        self.saldo=saldo

    def sacar_dinero(self, saldo):
        if saldo > 0:
             self.saldo-=saldo
             print("Saldo actualizado")
        else:
             print("El saldo debe ser positivo")

    def ingresar_dinero(self, saldo):
        if saldo > 0:
             self.saldo-=saldo
             print("Saldo actualizado")
        else:
             print("El saldo debe ser positivo")

    def __str__(self):
        print("DNI: ", self.DNI, " - Nombre: ", self.nombre, " - Saldo: ", self.saldo)

    def __eq__(self, cuenta):
        equals=False

        if self.DNI==cuenta.DNI:
              equals=True

        return equals
    
    def __lt__(self, cuenta):
        menor=False
        if self.saldo < cuenta.saldo:
              menor=True
        return menor