import threading
import random
import time

class Cliente(threading.Thread):
    sem_carniceria = threading.Semaphore(4)   
    sem_charcuteria = threading.Semaphore(2)

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def ir_carniceria(self):
        print(f"{self.name} esperando para entrar en carniceria...")
        Cliente.sem_carniceria.acquire()
        print(f"{self.name} está siendo atendido en carniceria")
        time.sleep(random.randint(1, 5))
        print(f"{self.name} ha terminado en carniceria")
        Cliente.sem_carniceria.release()

    def ir_charcuteria(self):
        print(f"{self.name} esperando para entrar en charcuteria...")
        Cliente.sem_charcuteria.acquire()
        print(f"{self.name} está siendo atendido en charcuteria")
        time.sleep(random.randint(1, 5))
        print(f"{self.name} ha terminado en charcuteria")
        Cliente.sem_charcuteria.release()

    def run(self):
        secciones = [self.ir_carniceria, self.ir_charcuteria]
        random.shuffle(secciones)

        for seccion in secciones:
            seccion()

        print(f"{self.name} ha terminado la compra completa y se ha pirado.")


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

    print("\nTodo el mercado esta finiquitado")