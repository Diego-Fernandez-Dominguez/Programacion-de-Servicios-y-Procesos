import threading
import random
import time

class Cliente(threading.Thread):
    dependiente = threading.Semaphore(1)  

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        print(f"{self.name} está esperando en la cola...")
        Cliente.dependiente.acquire()
        print(f"{self.name} está siendo atendido.")
        time.sleep(random.randint(1, 5))
        print(f"{self.name} ha pillado su pan y se ha pirado.")
        Cliente.dependiente.release()


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

    print("\nLa panaderia esta closed")