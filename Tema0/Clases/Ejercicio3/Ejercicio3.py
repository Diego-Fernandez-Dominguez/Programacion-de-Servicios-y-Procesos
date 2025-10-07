class Punto:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def setXY(self, x, y):
        self.x=x
        self.y=y

    def desplaza(self, dx, dy):
        self.x+=dx
        self.y+=dy

    def distancia(self, punto):
        disX=self.x - punto.x
        disY=self.y - punto.y

        cadena= str(disX) + ", " + str(disY)
        return cadena

    def __str__(self):
        cadena= str(self.x) + ", " + str(self.y)
        return cadena