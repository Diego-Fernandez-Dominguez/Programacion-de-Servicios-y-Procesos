f = open('Tema0\\Ficheros\\Ejercicio3\\datos.txt', 'a')

nombre = input("Dime tu nombrecillo: ")
edad = input("Cuantos telediarios llevas (años): ")

f.write(nombre + " " + edad + "\n")

f.close()