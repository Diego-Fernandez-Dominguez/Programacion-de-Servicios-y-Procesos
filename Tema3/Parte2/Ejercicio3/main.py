import threading
import random
import time

class Cliente(threading.Thread):
    carniceros = threading.Semaphore(4) 

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} está esperando turno...")
        Cliente.carniceros.acquire()
        print(f"El cliente {self.name} esta siendo atendido")
        time.sleep(random.randint(1, 10))
        print(f"El cliente {self.name} ha terminado en la carniceria")
        Cliente.carniceros.release()


if __name__ == "__main__":
    nombres = ["Leon S Kennedy", "Hector", "Euseboi", "William",
               "Lumberdeoloa", "Genji", "Guille", "Peter Parker",
               "Dario", "Adrian"]

    hilos = []
    for nombre in nombres:
        t = Cliente(nombre)
        t.start()
        hilos.append(t)

    for t in hilos:
        t.join()

    print("\nLa carnicería esta closed")