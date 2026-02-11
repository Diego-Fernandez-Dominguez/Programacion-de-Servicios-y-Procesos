from multiprocessing import Process, Pipe

def proceso_filtro1(departamento, conn):
    # Abrimos el fichero
    with open("salarios.txt", 'r') as f:
        for linea in f:
            linea = linea.strip()
            ape, nom, dep, sal = linea.split(',')
            
            # Si el departamento coincide enviamos apellido, nombre, salario
            if dep == departamento:
                conn.send(f"{ape},{nom},{sal}")
    
    # Indicamos que no hay mas datos
    conn.send(None)
    conn.close()

def proceso_filtro2(salario_minimo, conn_in, conn_out):
    # Leemos los datos que llegan desde el proceso anterior
    while True:
        linea = conn_in.recv()
        if linea is None:
            break
        
        ape, nom, sal = linea.split(',')
        
        # Si el salario cumple la condicion enviamos la linea
        if float(sal) >= salario_minimo:
            conn_out.send(f"{ape},{nom},{sal}")
    
    # Indicamos que no hay mas datos
    conn_out.send(None)
    conn_in.close()
    conn_out.close()

def proceso_filtro3(conn):
    # Abrimos el fichero de salida
    with open("empleados.txt", 'w') as f:
        
        # Leemos los datos que llegan desde el proceso anterior
        while True:
            linea = conn.recv()
            if linea is None:
                break
            
            ape, nom, sal = linea.split(',')
            
            # Escribimos en el formato solicitado
            f.write(f"{ape} {nom}, {sal}\n")
    
    conn.close()

if __name__ == "__main__":

    # Pedimos los datos al usuario
    departamento = input("Introduce el departamento: ")
    salario_minimo = float(input("Introduce el salario minimo: "))

    # Pipe entre filtro1 y filtro2
    c1_out, c1_in = Pipe()
    
    # Pipe entre filtro2 y filtro3
    c2_out, c2_in = Pipe()

    # Creamos los procesos
    p1 = Process(target=proceso_filtro1, args=(departamento, c1_in))
    p2 = Process(target=proceso_filtro2, args=(salario_minimo, c1_out, c2_in))
    p3 = Process(target=proceso_filtro3, args=(c2_out,))

    # Lanzamos los procesos
    p1.start()
    p2.start()
    p3.start()

    # Esperamos a que terminen
    p1.join()
    p2.join()
    p3.join()

    print("Procesos acabados")
