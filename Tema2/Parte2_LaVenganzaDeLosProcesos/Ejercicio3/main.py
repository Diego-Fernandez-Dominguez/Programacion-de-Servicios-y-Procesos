from multiprocessing import Process
import random
import time
import os

# Carpeta donde está este script
BASE = os.path.dirname(os.path.abspath(__file__))

def generar_notas(nombre_archivo):
    ruta = os.path.join(BASE, nombre_archivo)
    with open(ruta, "w") as f:
        for _ in range(6):
            f.write(str(round(random.uniform(1, 10), 2)) + "\n")

def calcular_media(nombre_archivo, alumno):
    ruta = os.path.join(BASE, nombre_archivo)

    with open(ruta, "r") as f:
        notas = [float(x) for x in f.readlines()]
    media = sum(notas) / len(notas)

    ruta_medias = os.path.join(BASE, "medias.txt")
    with open(ruta_medias, "a") as f:
        f.write(f"{media} {alumno}\n")

def mejor_media():
    ruta_medias = os.path.join(BASE, "medias.txt")

    mejor = -1
    nombre = ""

    with open(ruta_medias, "r") as f:
        for linea in f:
            media, alumno = linea.split()
            media = float(media)
            if media > mejor:
                mejor = media
                nombre = alumno

    print(f"Mejor media: {mejor} obtenida por {nombre}")

if __name__ == "__main__":
    inicio = time.time()

    # Proceso 1 (10 veces)
    procesos = []
    for i in range(1, 11):
        archivo = f"Alumno{i}.txt"
        p = Process(target=generar_notas, args=(archivo,))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    # Proceso 2 (10 veces)
    procesos = []
    for i in range(1, 11):
        archivo = f"Alumno{i}.txt"
        p = Process(target=calcular_media, args=(archivo, f"Alumno{i}"))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    # Proceso 3
    p3 = Process(target=mejor_media)
    p3.start()
    p3.join()

    fin = time.time()
    print(f"Tiempo total: {fin - inicio:.4f} segundos")
