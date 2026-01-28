from multiprocessing import Process, Pipe
import random
import time

def generar_ips(conn):
    for _ in range(10):
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        conn.send(ip)
    conn.send(None)
    conn.close()

def filtrar_clases(conn_in, conn_out):
    while True:
        ip = conn_in.recv()
        if ip is None:
            conn_out.send(None)
            break

        primer = int(ip.split(".")[0])

        if 1 <= primer <= 126:
            clase = "A"
        elif 128 <= primer <= 191:
            clase = "B"
        elif 192 <= primer <= 223:
            clase = "C"
        else:
            continue

        conn_out.send((ip, clase))

    conn_out.close()

def imprimir_ips(conn):
    while True:
        datos = conn.recv()
        if datos is None:
            break
        ip, clase = datos
        print(f"{ip} → Clase {clase}")

if __name__ == "__main__":
    inicio = time.time()
    c1a, c1b = Pipe()
    c2a, c2b = Pipe()

    p1 = Process(target=generar_ips, args=(c1a,))
    p2 = Process(target=filtrar_clases, args=(c1b, c2a))
    p3 = Process(target=imprimir_ips, args=(c2b,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Procesos finiquitaos")
    fin = time.time() 
    print(f"Tiempo total: {fin - inicio:.4f} segundos")