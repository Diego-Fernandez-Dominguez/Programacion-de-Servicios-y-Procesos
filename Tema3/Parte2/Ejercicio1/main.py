import threading
import random

class Adivinador(threading.Thread):
    secretito = random.randint(0, 100)
    acertado = False
    candado = threading.Lock()

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        intentos = 0
        while True:
            intento = random.randint(0, 100)
            intentos += 1

            if intento == Adivinador.secretito:
                Adivinador.candado.acquire()
                if not Adivinador.acertado:
                    Adivinador.acertado = True
                    print(f"{self.name} ha tenido una potra con el numero: {Adivinador.secretito} "
                          f"en {intentos} tries")
                Adivinador.candado.release()
                return
            else:
                Adivinador.candado.acquire()
                ya_acerto = Adivinador.acertado
                Adivinador.candado.release()
                if ya_acerto:
                    print(f"{self.name} se rinde porque alguien ya lo pillo.")
                    return


if __name__ == "__main__":
    print(f"Numerin secretito: {Adivinador.secretito}\n")

    hilos = []
    for i in range(10):
        t = Adivinador(f"Hilo-{i}")
        t.start()
        hilos.append(t)

    for t in hilos:
        t.join()

    print("\nFiniquitao.")