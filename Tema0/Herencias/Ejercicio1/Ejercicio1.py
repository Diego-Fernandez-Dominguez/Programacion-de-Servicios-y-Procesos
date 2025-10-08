class Animal:

    def __init__(self, nombre, patas):

        self.nombre=nombre
        self.patas=patas

    def habla():
        return ""
    
    def __str__(self):
        cadena = "me llamo " + self.nombre  + ", tengo "+  str(self.patas) +" patas y sueno así: " + self.habla()
        return cadena

class Gato(Animal):

    def __init__(self, nombre, patas):
        super().__init__(nombre, patas)
    
    def habla(self):
        cadena = "Miau miau soy tu dueño, dame comida, miau"
        return cadena
    
    def __str__(self):
        return "Soy un gato " + super().__str__()
    
class Perrete(Animal):

    def __init__(self, nombre, patas):
        super().__init__(nombre, patas)
    
    def habla(self):
        cadena = "Guau guau mucho, ladro mucho guau"
        return cadena
    
    def __str__(self):
        return "Soy un perro " + super().__str__()