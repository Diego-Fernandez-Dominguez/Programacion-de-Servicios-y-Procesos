class Libro:

    def __init__(self, titulo, autor, ejemplares, ejemplaresPrestados):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.ejemplaresPrestados = ejemplaresPrestados

    def prestamo(self, num):
        possible=False

        if num <= self.ejemplares:
            possible=True
            self.ejemplares-=num
            self.ejemplaresPrestados+=num

        return possible
    
    def devolucion(self, num):
        possible=False

        if num <= self.ejemplaresPrestados:
            possible=True
            self.ejemplaresPrestados-=num
            self.ejemplares+=num

        return possible
    
    def __str__(self):
        cadena="Título:", self.titulo, "- Autor:", self.autor, "- Ejemplares:", str(self.ejemplares), "- Prestados:", str(self.ejemplaresPrestados)
        return cadena

    def __eq__(self, libro):
        equals = False
        if self.titulo == libro.titulo and self.autor == libro.autor:
            equals = True
        return equals

    def __lt__(self, libro):
        menor = False
        if self.autor < libro.autor:
            menor = True
        return menor

