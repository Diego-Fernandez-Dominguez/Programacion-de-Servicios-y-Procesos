from multiprocessing import Process, Pipe
import os

# Carpeta donde está este script
BASE = os.path.dirname(os.path.abspath(__file__))

def proceso1_filtrar(ruta_relativa, year, conn):
    # Ruta absoluta del fichero de entrada
    ruta = os.path.join(BASE, ruta_relativa)

    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue

            nombre, estreno = linea.split(";")

            if estreno == str(year):
                conn.send(nombre)

    conn.send(None)
    conn.close()


def proceso2_guardar(year, conn):
    # Ruta absoluta del fichero de salida
    salida = os.path.join(BASE, f"peliculas{year}.txt")

    with open(salida, "w", encoding="utf-8") as f:
        while True:
            peli = conn.recv()
            if peli is None:
                break
            f.write(peli + "\n")


if __name__ == "__main__":
    year = int(input("Introduce un año menor al actual: "))
    ruta_fichero = input("Introduce la ruta del fichero de películas: ")

    # Crear Pipe
    c1, c2 = Pipe()

    # Crear procesos
    p1 = Process(target=proceso1_filtrar, args=(ruta_fichero, year, c1))
    p2 = Process(target=proceso2_guardar, args=(year, c2))

    # Ejecutar
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Películas del año {year} guardadas en peliculas{year}.txt dentro de la carpeta del script.")
