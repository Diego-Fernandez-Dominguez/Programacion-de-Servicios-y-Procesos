import subprocess
import random
import sys
import os

# Función que ejecuta el Proceso 1: generar temperaturas
def proceso1(dia):
    
    nombre_fichero = f"{dia}-12.txt"
    
    # Abrimos el fichero en modo escritura
    with open(nombre_fichero, 'w') as fichero:
        # Generamos 24 temperaturas (una por cada hora del día)
        for i in range(24):
            # Temperatura aleatoria entre 0 y 20 con 2 decimales
            temperatura = round(random.uniform(0, 20), 2)
            # Escribimos la temperatura en el fichero (una por línea)
            fichero.write(f"{temperatura}\n")
    
    print(f"Fichero {nombre_fichero} creado correctamente")

# Función que ejecuta el Proceso 2: calcular temperatura máxima
def proceso2(dia):
    # El fichero a leer será dia-12.txt
    nombre_fichero = f"{dia}-12.txt"
    
    # Leemos todas las temperaturas del fichero
    with open(nombre_fichero, 'r') as fichero:
        temperaturas = fichero.readlines()
    
    # Convertimos las temperaturas a float y buscamos la máxima
    temp_max = max([float(temp.strip()) for temp in temperaturas])
    
    # Escribimos en maximas.txt la fecha y la temperatura máxima
    # Usamos 'a' para añadir al final del fichero (append)
    with open("maximas.txt", 'a') as fichero_max:
        fichero_max.write(f"{dia}-12:{temp_max}\n")
    
    print(f"Temperatura máxima del día {dia}-12: {temp_max}")

# Función que ejecuta el Proceso 3: calcular temperatura mínima
def proceso3(dia):
    # El fichero a leer será dia-12.txt
    nombre_fichero = f"{dia}-12.txt"
    
    # Leemos todas las temperaturas del fichero
    with open(nombre_fichero, 'r') as fichero:
        temperaturas = fichero.readlines()
    
    # Convertimos las temperaturas a float y buscamos la mínima
    temp_min = min([float(temp.strip()) for temp in temperaturas])
    
    # Escribimos en minimas.txt la fecha y la temperatura mínima
    # Usamos 'a' para añadir al final del fichero (append)
    with open("minimas.txt", 'a') as fichero_min:
        fichero_min.write(f"{dia}-12:{temp_min}\n")
    
    print(f"Temperatura mínima del día {dia}-12: {temp_min}")

# Programa principal
if __name__ == "__main__":
    # Si recibimos argumentos, ejecutamos el proceso correspondiente
    if len(sys.argv) > 1:
        proceso_tipo = sys.argv[1]
        dia = sys.argv[2]
        
        if proceso_tipo == "generar":
            proceso1(dia)
        elif proceso_tipo == "maxima":
            proceso2(dia)
        elif proceso_tipo == "minima":
            proceso3(dia)
    else:
        
        # Borramos los ficheros de resultados si existen (para empezar limpio)
        if os.path.exists("maximas.txt"):
            os.remove("maximas.txt")
        if os.path.exists("minimas.txt"):
            os.remove("minimas.txt")
        
        print("=== EJERCICIO 1 ===\n")
        
        # FASE 1: Generar las temperaturas de los 31 días de diciembre
        print("Generando temperaturas para los 31 días de diciembre...")
        
        procesos_fase1 = []
        
        # Lanzamos 31 procesos simultáneos (uno por cada día de diciembre)
        for dia in range(1, 32):
            # Formateamos el día con dos dígitos (01, 02, ..., 31)
            dia_formateado = f"{dia:02d}"
            
            # Lanzamos este mismo script con argumentos para ejecutar el proceso1
            proceso = subprocess.Popen(['python3', __file__, 'generar', dia_formateado])
            procesos_fase1.append(proceso)
        
        # Esperamos a que terminen todos los procesos de la fase 1
        for proceso in procesos_fase1:
            proceso.wait()
        
        print("¡Temperaturas generadas!\n")
        
        # FASE 2: Calcular máximas y mínimas de los 31 días
        print("Calculando temperaturas máximas y mínimas...")
        
        procesos_fase2 = []
        
        # Lanzamos 62 procesos simultáneos (31 del proceso2 y 31 del proceso3)
        for dia in range(1, 32):
            dia_formateado = f"{dia:02d}"
            
            # Lanzamos el proceso2 (máximas)
            proceso_max = subprocess.Popen(['python3', __file__, 'maxima', dia_formateado])
            procesos_fase2.append(proceso_max)
            
            # Lanzamos el proceso3 (mínimas)
            proceso_min = subprocess.Popen(['python3', __file__, 'minima', dia_formateado])
            procesos_fase2.append(proceso_min)
        
        # Esperamos a que terminen todos los procesos de la fase 2
        for proceso in procesos_fase2:
            proceso.wait()
        
        print("Se han creado los ficheros maximas.txt y minimas.txt")
        print("También se han creado 31 ficheros con las temperaturas diarias")