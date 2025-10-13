
f = open('Tema0\\Ficheros\\Ejercicio2\\paranoias.txt', 'w')

linea = input("Escribe una línea: ")

while linea != "fin":
    f.write(linea + "\n")
    linea = input("Escribe una línea: ")

f.close()
