from multiprocessing import Process, Pipe
import os

def leer_fichero(ruta_fichero, conn):
    with open(ruta_fichero, 'r') as f:
        for linea in f:
            linea = linea.strip()
            if linea:
                a, b = map(int, linea.split())
                conn.send((a, b))

    conn.send(None)
    conn.close()

def sumar_rangos(conn):
    while True:
        datos = conn.recv()

        if datos is None:
            break

        a, b = datos
        inicio = min(a, b)
        fin = max(a, b)

        suma = 0
        for i in range(inicio, fin + 1):
            suma += i

        print(f"Suma de {inicio} a {fin}: {suma}")

if __name__ == "__main__":

    
    base = os.path.dirname(os.path.abspath(__file__)) 
    fichero = os.path.join(base, "ficherin.txt")

    conn_lector, conn_sumador = Pipe()

    p_lector = Process(
        target=leer_fichero,
        args=(fichero, conn_lector)
    )

    p_sumador = Process(
        target=sumar_rangos,
        args=(conn_sumador,)
    )

    p_lector.start()
    p_sumador.start()

    p_lector.join()
    p_sumador.join()

    print("Todos los procesos han terminado")
