import threading
import random
import time

palillos = [threading.Lock() for _ in range(5)]

class Filosofo(threading.Thread):
    def __init__(self, numero):
        threading.Thread.__init__(self, name=f"Filosofo-{numero}")
        self.numero = numero
        self.palillo_izq = palillos[numero]
        self.palillo_der = palillos[(numero + 1) % 5]

    def run(self):
        for _ in range(3): 
            self.pensar()
            self.comer()
        print(f"{self.name} se ha ido a mimir.")

    def pensar(self):
        print(f"{self.name} esta filosofeando...")
        time.sleep(random.uniform(1, 3))

    def comer(self):
        if self.numero % 2 == 0:
            primero, segundo = self.palillo_izq, self.palillo_der
        else:
            primero, segundo = self.palillo_der, self.palillo_izq

        primero.acquire()
        print(f"{self.name} ha cogido los palillos")
        segundo.acquire()

        print(f"{self.name} esta comiendo espaguetis")
        time.sleep(random.uniform(1, 3))
        print(f"{self.name} ha terminado de comer y suelta los palillos.")

        primero.release()
        segundo.release()


if __name__ == "__main__":
    filosofos = [Filosofo(i) for i in range(5)]

    for f in filosofos:
        f.start()

    for f in filosofos:
        f.join()

    print("\nTodos los filosofos han terminado de zampar")
