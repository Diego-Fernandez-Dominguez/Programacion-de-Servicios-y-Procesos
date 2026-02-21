import threading
import random

class Adivinador(threading.Thread):
    secretito = random.randint(0, 100)
    acertado = False

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        intentos = 0
        while True:
            intento = random.randint(0, 100)
            intentos += 1

            if intento == Adivinador.secretito:
                Adivinador.acertado = True
                print(f"{self.name} ha tenido una potra con el numero: {Adivinador.secretito} "
                      f"en {intentos} tries!")
                return
            else:
                if Adivinador.acertado:
                    print(f"{self.name} se desflipa porque otro hilo ya se ha flipado.")
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