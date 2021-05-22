
#funcion para modificar las notas, del estudiante seleccionado (ID)
def modificar(id,archivo):
    linea = buscar(id,archivo)
    f = open(archivo,'r')
    lineas = f.readlines()
    f.close()
    n = int(input("""Seleccione nota a modificar:
        1. Modificar primer nota
        2. Modificar segunda nota
        """))
    if n == 1:
        cambio = ingreso('c1')
        cambio = comprobar(cambio,'c1')
        pos = linea.index('*')
    if n == 2:
        cambio = ingreso('c2')
        cambio = comprobar(cambio,'c2')
        pos = linea.rindex('*')
    f = open(archivo,'w')
    for l in lineas:
        if linea == l:          
            if cambio!=10:
                temp = linea.replace(linea[pos+1:pos+3],f"0{cambio}",1)  
            else:
                temp = linea.replace(linea[pos+1:pos+3],f"{cambio}",1) 
            f.write(temp)
        else:
            f.write(l)
    f.close()
    print("Calificaciones actualizadas correctamente!\n")
    

def comprobar(n,v):
    while n < 0 or n>10:
        n = ingreso(v)
    return n

#funcion para eliminar el registro del estudiante y sus notas
def eliminar(id,archivo):
    linea = buscar(id,archivo)
    f = open(archivo,'r')
    lineas = f.readlines()
    f.close()
    f = open(archivo,'w')
    for l in lineas:
        if linea != l:
            f.write(l)
    f.close()
    print("Estudiante eliminado correctamente!")

#funcion para inicializar el archivo de texto
def iniciar_archivo(archivo):
    file = open(archivo,'w')    
    file.write("ID\t")
    file.write("Nombres\t\t")
    file.write("1er parcial\t")
    file.write("2do parcial\t\n")
    file.close()

#funcion agregar datos al archivo registro.txt
def agregar(archivo,id,name,n1,n2):
    file = open(archivo,'a')
    file.write(f"{id}\t")
    file.write(f"{name}\t")
    if n1 < 10:
        file.write(f"\t*0{n1}\t")
    else:
        file.write(f"\t*{n1}\t")
    if n2 < 10:
        file.write(f"\t*0{n2}\t\n")
    else:
        file.write(f"\t*{n2}\t\n")
    file.close()

def ingresar(archivo, i):
    name = ingreso('n')
    nota1 = int(ingreso('c1'))
    nota1 = comprobar(nota1,'c1')        
    nota2 = int(ingreso('c2'))
    nota2 = comprobar(nota2,'c2')
    agregar(archivo,i+1,name,nota1,nota2)

#funcion para pedir datos
def ingreso(str):
    msj = "Oops!  Este no es un valor valido.  Intentélo otra tez..."
    if str == 'c1':
        while True:
            try:
                valor = int(input('Ingrese la calificación del primer parcial:\t'))
                break
            except ValueError:
                print(msj)
    if str == 'c2':
        while True:
            try:
                valor = int(input('Ingrese la calificación del segundo parcial:\t'))
                break
            except ValueError:
                print(msj)
                      
    if str == 'n':
        while True:
            valor = input('Ingrese nombre del estudiante :\t')
            if valor!='':
                break
            print("No puede dejar este campo vacío!!")
        
    return valor

#función que mostrará al usuario el contenido del archivo de texto
def mostrar(archivo):
    f = open(archivo,'r')
    lineas = f.read()
    f.close()
    print(lineas)
    
#funcion que permite escojer la linea del archivo de texto con el id seleccionado por el usuario
def buscar(id,archivo):
    with open(archivo) as temp_f:
        datafile = temp_f.readlines()
    temp_f.close()
    for line in datafile:
        if line.find(str(id), 0, 3) != -1:
            return line
    print('Estudiante no encontrado')
    
   
    
