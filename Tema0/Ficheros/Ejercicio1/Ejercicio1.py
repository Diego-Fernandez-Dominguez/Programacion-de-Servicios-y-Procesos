edades=0
estaturas=0
cont=0

f = open('Tema0\\Ficheros\\Ejercicio1\\alumnos.txt', 'rt')

for linea in f.readlines():
    datos=linea.split(" ")
    edades= edades + int(datos[1])
    estaturas=estaturas+ float(datos[2])
    print(datos[0])
    cont=cont+1

print("Edad medias: " + str(edades/cont))
print("Estaturas medias: " + str(estaturas/cont))