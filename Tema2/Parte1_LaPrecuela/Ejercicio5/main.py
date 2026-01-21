from multiprocessing import Process

def sumar_rango(a, b):
    inicio = min(a, b)
    fin = max(a, b)

    suma = 0
    for i in range(inicio, fin + 1):
        suma += i

    print(f"Suma de {inicio} a {fin}: {suma}")

if __name__ == "__main__":

    procesos = []

    rangos = [
        (1, 10),
        (20, 5),
        (100, 200),
        (50, 50)
    ]

    for a, b in rangos:
        p = Process(target=sumar_rango, args=(a, b))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Todos los procesos han terminado")
