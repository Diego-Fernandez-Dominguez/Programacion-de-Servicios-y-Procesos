import subprocess
import sys

# Función que ejecuta el Proceso 1: filtra por departamento
def proceso_filtro1(departamento):
    # Abrimos el fichero salarios.txt
    with open("salarios.txt", 'r') as fichero:
        # Leemos todas las líneas
        lineas = fichero.readlines()
        
        # Procesamos cada línea
        for linea in lineas:
            # Quitamos saltos de línea y espacios
            linea = linea.strip()
            
            # Separamos los campos por comas
            campos = linea.split(',')
            
            # Los campos son: apellido, nombre, departamento, salario
            apellido = campos[0]
            nombre = campos[1]
            dept = campos[2]
            salario = campos[3]
            
            # Si el departamento coincide, enviamos la línea sin el departamento
            if dept == departamento:
                # Enviamos: apellido,nombre,salario
                print(f"{apellido},{nombre},{salario}")

# Función que ejecuta el Proceso 2: filtra por salario mínimo
def proceso_filtro2(salario_minimo):
    # Leemos las líneas que nos llegan del proceso anterior por stdin
    for linea in sys.stdin:
        # Quitamos saltos de línea y espacios
        linea = linea.strip()
        
        # Separamos los campos por comas
        campos = linea.split(',')
        
        # Los campos que nos llegan son: apellido, nombre, salario
        apellido = campos[0]
        nombre = campos[1]
        salario = float(campos[2])
        
        # Si el salario es mayor o igual que el mínimo, enviamos la línea
        if salario >= salario_minimo:
            print(f"{apellido},{nombre},{salario}")

# Función que ejecuta el Proceso 3: escribe el resultado final
def proceso_filtro3():
    # Abrimos el fichero empleados.txt en modo escritura
    with open("empleados.txt", 'w') as fichero:
        # Leemos las líneas que nos llegan del proceso anterior por stdin
        for linea in sys.stdin:
            # Quitamos saltos de línea y espacios
            linea = linea.strip()
            
            # Separamos los campos por comas
            campos = linea.split(',')
            
            # Los campos que nos llegan son: apellido, nombre, salario
            apellido = campos[0]
            nombre = campos[1]
            salario = campos[2]
            
            # Escribimos en el formato solicitado: Apellido Nombre, Salario
            fichero.write(f"{apellido} {nombre}, {salario}\n")
    
    print("Fichero empleados.txt creado correctamente")

# Programa principal
if __name__ == "__main__":
    # Si recibimos argumentos, ejecutamos el proceso correspondiente
    if len(sys.argv) > 1:
        proceso_tipo = sys.argv[1]
        
        if proceso_tipo == "filtro1":
            departamento = sys.argv[2]
            proceso_filtro1(departamento)
        elif proceso_tipo == "filtro2":
            salario_minimo = float(sys.argv[2])
            proceso_filtro2(salario_minimo)
        elif proceso_tipo == "filtro3":
            proceso_filtro3()
    else:
        # Si no hay argumentos, ejecutamos el Main
        
        print("=== EJERCICIO 2 ===\n")
        
        # Pedimos al usuario el departamento y el salario mínimo
        departamento = input("Introduce el nombre del departamento: ")
        salario_minimo = input("Introduce el salario mínimo: ")
        
        print(f"\nBuscando empleados del departamento '{departamento}' con salario >= {salario_minimo}...\n")
        
        # Creamos una cadena de procesos conectados por tuberías (pipes)
        # Proceso 1: Filtra por departamento
        proceso1 = subprocess.Popen(
            ['python3', __file__, 'filtro1', departamento],
            stdout=subprocess.PIPE  # La salida del proceso1 irá al proceso2
        )
        
        # Proceso 2: Filtra por salario mínimo
        # La entrada (stdin) viene del proceso1
        proceso2 = subprocess.Popen(
            ['python3', __file__, 'filtro2', salario_minimo],
            stdin=proceso1.stdout,  # Recibe la salida del proceso1
            stdout=subprocess.PIPE  # La salida del proceso2 irá al proceso3
        )
        
        # Cerramos la salida del proceso1 en el main para que el proceso2 reciba el EOF
        proceso1.stdout.close()
        
        # Proceso 3: Escribe el resultado en empleados.txt
        # La entrada (stdin) viene del proceso2
        proceso3 = subprocess.Popen(
            ['python3', __file__, 'filtro3'],
            stdin=proceso2.stdout  # Recibe la salida del proceso2
        )
        
        # Cerramos la salida del proceso2 en el main
        proceso2.stdout.close()
        
        # Esperamos a que terminen todos los procesos
        proceso1.wait()
        proceso2.wait()
        proceso3.wait()
        
        print("\n¡Proceso completado!")
        print("Revisa el fichero empleados.txt para ver los resultados")