import threading

class Contador(threading.Thread):
    cont = 0

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        while Contador.cont < 1000:
            Contador.cont += 1
            print(f"{self.name} - contador: {Contador.cont}")


if __name__ == "__main__":
    hilos = []

    for i in range(10):
        t = Contador(f"Hilo-{i}")
        t.start()
        hilos.append(t)

    for t in hilos:
        t.join()

    print(f"\nContador: {Contador.cont}")
