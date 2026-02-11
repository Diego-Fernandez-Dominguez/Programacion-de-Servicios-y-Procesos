from multiprocessing import Process
import random
import os

def proceso1(dia):
    # Nombre del fichero
    nombre = f"{dia}-12.txt"
    
    # Abrimos el fichero y generamos 24 temperaturas
    with open(nombre, 'w') as f:
        for _ in range(24):
            temp = round(random.uniform(0, 20), 2)
            f.write(f"{temp}\n")

def proceso2(dia):
    # Abrimos el fichero del dia
    nombre = f"{dia}-12.txt"
    with open(nombre, 'r') as f:
        temps = [float(t.strip()) for t in f.readlines()]
    
    # Calculamos la temperatura maxima
    temp_max = max(temps)
    
    # Guardamos el resultado en el fichero
    with open("maximas.txt", 'a') as f:
        f.write(f"{dia}-12:{temp_max}\n")

def proceso3(dia):
    # Abrimos el fichero del dia
    nombre = f"{dia}-12.txt"
    with open(nombre, 'r') as f:
        temps = [float(t.strip()) for t in f.readlines()]
    
    # Calculamos la temperatura minima
    temp_min = min(temps)
    
    # Guardamos el resultado en el fichero
    with open("minimas.txt", 'a') as f:
        f.write(f"{dia}-12:{temp_min}\n")

if __name__ == "__main__":

    # Borramos los ficheros de resultados si existen
    if os.path.exists("maximas.txt"):
        os.remove("maximas.txt")
    if os.path.exists("minimas.txt"):
        os.remove("minimas.txt")

    procesos = []

    # Generamos temperaturas
    for dia in range(1, 32):
        d = f"{dia:02d}"
        p = Process(target=proceso1, args=(d,))
        procesos.append(p)
        p.start()

    # Esperamos a que terminen todos los procesos
    for p in procesos:
        p.join()

    procesos = []

    # Calculamos las maximas y las minimas
    for dia in range(1, 32):
        d = f"{dia:02d}"
        
        # Proceso para maxima
        p1 = Process(target=proceso2, args=(d,))
        procesos.append(p1)
        p1.start()
        
        # Proceso para minima
        p2 = Process(target=proceso3, args=(d,))
        procesos.append(p2)
        p2.start()

    # Esperamos a que terminen todos los procesos
    for p in procesos:
        p.join()

    print("Procesos acabados")
