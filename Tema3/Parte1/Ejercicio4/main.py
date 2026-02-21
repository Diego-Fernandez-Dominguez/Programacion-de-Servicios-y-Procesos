import threading


guion_bee_movie = """
Según todas las leyes conocidas de la aviación, es imposible 
que una abeja pueda volar. Sus alas son demasiado pequeñas para 
levantar su cuerpecito gordo del suelo. La abeja, por supuesto, vuela 
de todos modos porque a las abejas no les importa lo que los humanos consideren 
imposible. Amarillo, negro. Amarillo, negro. Amarillo, negro. Amarillo, negro. 
¡Oh, negro y amarillo! Agitémoslo un poco.
"""

class ContadorVocal(threading.Thread):
    resultados = {}

    def __init__(self, vocal, texto):
        threading.Thread.__init__(self, name=f"Hilo-{vocal.upper()}")
        self.vocal = vocal
        self.texto = texto

    def run(self):
        cantidad = self.texto.lower().count(self.vocal)
        ContadorVocal.resultados[self.vocal] = cantidad
        print(f"{self.name}: encontro {cantidad} '{self.vocal}' en el guion")


if __name__ == "__main__":
    vocales = ['a', 'e', 'i', 'o', 'u']
    hilos = []

    for vocal in vocales:
        t = ContadorVocal(vocal, guion_bee_movie)
        t.start()
        hilos.append(t)

    for t in hilos:
        t.join()

    print(f"\nResultados: {ContadorVocal.resultados}")
    print(f"Vocales totales: {sum(ContadorVocal.resultados.values())}")