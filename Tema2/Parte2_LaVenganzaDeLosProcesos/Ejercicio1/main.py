from multiprocessing import Process, Pipe
import time
import os

def contar_vocal(vocal, ruta, conn):
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read().lower()
    conn.send((vocal, texto.count(vocal)))
    conn.close()

if __name__ == "__main__":
    inicio = time.time()

    base = os.path.dirname(os.path.abspath(__file__))
    fichero = os.path.join(base, "palabritasjisjisjis.txt")

    vocales = ["a", "e", "i", "o", "u"]
    procesos = []
    conexiones = []

    for v in vocales:
        c1, c2 = Pipe()
        p = Process(target=contar_vocal, args=(v, fichero, c1))
        procesos.append(p)
        conexiones.append(c2)
        p.start()

    for p in procesos:
        p.join()

    for c in conexiones:
        vocal, cantidad = c.recv()
        print(f"La vocal '{vocal}' aparece {cantidad} veces")

    print("Tiempo:", time.time() - inicio)
