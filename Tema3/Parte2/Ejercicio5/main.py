import threading
import random
import time

class Biblioteca(threading.Thread):
    libros = [False] * 9 
    cond = threading.Condition()

    def __init__(self, nombre):
        threading.Thread.__init__(self, name=nombre)

    def run(self):
        libro1, libro2 = sorted(random.sample(range(9), 2))

        with Biblioteca.cond:
            while Biblioteca.libros[libro1] or Biblioteca.libros[libro2]:
                print(f"{self.name} esperando a que se libren los libros {libro1} y {libro2}...")
                Biblioteca.cond.wait()

            Biblioteca.libros[libro1] = True
            Biblioteca.libros[libro2] = True
            print(f"{self.name} ha cogido los libros {libro1} y {libro2}")

        time.sleep(random.randint(3, 5))

        with Biblioteca.cond:
            Biblioteca.libros[libro1] = False
            Biblioteca.libros[libro2] = False
            print(f"{self.name} ha devuelto los libros {libro1} y {libro2}")
            Biblioteca.cond.notify_all()


if __name__ == "__main__":
    nombres = ["Dario", "Lumberdeoloa", "Garcos", "Manuel"]

    hilos = []
    for nombre in nombres:
        t = Biblioteca(nombre)
        t.start()
        hilos.append(t)

    for t in hilos:
        t.join()

    print("\nLos estudiantes ya se lo han currado, toca: FIESTAAAAAAAA")