from multiprocessing import Process, Queue

def leer_fichero(ruta_fichero, cola):
    with open(ruta_fichero, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                try:
                    a, b = map(int, linea.split())
                    cola.put((a, b))
                except ValueError:
                    print(f"Línea inválida ignorada: {linea}")

    cola.put(None)

def sumar_rangos(cola):
    while True:
        datos = cola.get()

        if datos is None:
            break

        a, b = datos
        inicio, fin = sorted((a, b))

        suma = sum(range(inicio, fin + 1))

        print(f"Suma de {inicio} a {fin}: {suma}")

if __name__ == "__main__":

    ficherin = './ficherin.txt'
    cola = Queue()

    p_lector = Process(target=leer_fichero, args=(ficherin, cola))
    p_sumador = Process(target=sumar_rangos, args=(cola,))

    p_lector.start()
    p_sumador.start()

    p_lector.join()
    p_sumador.join()

    print("Todos los procesos han terminado")
