class Empleado:

    def __init__(self, nombre="Anonimo"):
        self.nombre=nombre

    def setNombre(self, nombre):
        
        possible=False
        
        if nombre != "":
            self.nombre=nombre
            possible=True

        return possible
    
    def getNombre(self):
        return self.nombre
    
    def __str__(self):
        cadena= "Empleado: " + self.nombre
        return cadena

class Directivo(Empleado):

    def __init__(self, nombre="Anonimo"):
        super().__init__(nombre)

    def __str__(self):
        cadena= super().__str__() + " -> Directivo"
        return cadena
    

class Operario(Empleado):

    def __init__(self, nombre="Anonimo"):
        super().__init__(nombre)

    def __str__(self):
        cadena= super().__str__() + " -> Operario"
        return cadena


class Oficial(Empleado):

    def __init__(self, nombre="Anonimo"):
        super().__init__(nombre)

    def __str__(self):
        cadena= super().__str__() + " -> Oficial"
        return cadena
    
class Tecnico(Empleado):

    def __init__(self, nombre="Anonimo"):
        super().__init__(nombre)

    def __str__(self):
        cadena= super().__str__() + " -> Tecnico"
        return cadena