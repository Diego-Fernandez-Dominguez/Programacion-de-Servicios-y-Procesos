import threading
import queue
import random
import time

cola = queue.Queue(maxsize=1)

class Productor(threading.Thread):
    def __init__(self, nombre, num_productos):
        threading.Thread.__init__(self, name=nombre)
        self.num_productos = num_productos

    def run(self):
        for i in range(self.num_productos):
            producto = f"Producto-{i+1} de {self.name}"
            print(f"{self.name} quiere meter: {producto}")
            cola.put(producto) 
            print(f"{self.name} ha metido: {producto} | Tamaño cola: {cola.qsize()}")
            time.sleep(random.uniform(0.5, 2))

        print(f"{self.name} ha terminado de producir.")


class Consumidor(threading.Thread):
    def __init__(self, nombre, num_productos):
        threading.Thread.__init__(self, name=nombre)
        self.num_productos = num_productos

    def run(self):
        for _ in range(self.num_productos):
            print(f"{self.name} intentando sacar algo de la cola...")
            producto = cola.get() 
            print(f"{self.name} ha consumido: {producto}")
            time.sleep(random.uniform(0.5, 2))
            cola.task_done()

        print(f"{self.name} ha terminado de consumir.")


if __name__ == "__main__":
    NUM_PRODUCTOS = 5

    productor = Productor("Josebas-el-Productor", NUM_PRODUCTOS)
    consumidor = Consumidor("Garcos-el-Consumidor", NUM_PRODUCTOS)

    productor.start()
    consumidor.start()

    productor.join()
    consumidor.join()

    print("\nAcabado")