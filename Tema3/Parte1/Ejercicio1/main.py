import threading
import random
import time

class Trabajador(threading.Thread):
    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            tiempo = random.randint(1, 10)
            time.sleep(tiempo)
            print(f"Soy {self.name} y he terminado de trabajar")


if __name__ == "__main__":
    nombres = ["Dario", "Lumberdeoloa", "Garcos", "Manuel", "Euseboi"]
    hilos = []

    for nombre in nombres:
        t = Trabajador(nombre)
        t.daemon = True
        t.start()
        hilos.append(t)

    time.sleep(30)
    print("\nFiniquitao")