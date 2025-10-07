from Ejercicio1 import *

account = CuentaCorriente("12345678A", "Euseboi", 1500)
print(account.__str__())

account.sacar_dinero(1000)
print(account.__str__())

account.ingresar_dinero(500)
print(account.__str__())
