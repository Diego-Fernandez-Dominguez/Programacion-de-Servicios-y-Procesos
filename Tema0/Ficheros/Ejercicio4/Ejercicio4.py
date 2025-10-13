numeros = []

f = open('Tema0\\Ficheros\\Ejercicio4\\CaosDeNumeros.txt', 'rt')

for linea in f.readlines():
    numeros.append(int(linea))

f.close()

numeros.sort()

print(numeros)

f2 = open('Tema0\\Ficheros\\Ejercicio4\\NumerosBuenos.txt', 'w')

for n in numeros:
    f2.write(str(n)+'\n')

f2.close()