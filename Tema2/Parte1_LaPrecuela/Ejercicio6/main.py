from multiprocessing import Pool

def sumar_rango(a, b):
    inicio = min(a, b)
    fin = max(a, b)

    suma = 0
    for i in range(inicio, fin + 1):
        suma += i

    print(f"Suma de {inicio} a {fin}: {suma}")

if __name__ == "__main__":

    rangos = [
        (1, 10),
        (20, 5),
        (100, 200),
        (50, 50)
    ]

    with Pool() as pool:
        pool.starmap(sumar_rango, rangos)

    print("Todos los procesos han terminado")
