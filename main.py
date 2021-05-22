#aqui se ejecuta todo
import sys
from menu import menu
from funciones import ingresar, modificar, eliminar, mostrar, iniciar_archivo

txt="No puedes hacer esto aún!!"
ctrl=0
archivo = 'registro.txt'
iniciar_archivo(archivo)
while True:
    opciones = menu()
    if opciones == 1:
        ctrl=1
        while True:
            n = input('Cuantos estudiantes va a ingresar:\t')
            if n!='':
                break
        n=int(n)
        for i in range(n):
            ingresar(archivo,i)            
    if opciones == 2:
        # funcion modificar
        if ctrl==1:
            ID = int(input("Ingrese ID del estudiante a modificar:\t"))
            if n >= ID:
                modificar(ID, archivo)
            else:
                print("Estudiante no encontrado")
        else:
            print(txt)      
    if opciones == 3:
        #funcion eliminar
        if ctrl==1:
            ID = int(input("Ingrese ID del estudiante a eliminar:\t"))
            if n >= ID:
                eliminar(ID, archivo)
            else:
                print("Estudiante no encontrado") 
        else:
            print(txt)   
    if opciones == 4:
        if ctrl==1:
        #funcion modificar
            mostrar(archivo)
        else:
            print(txt)   
    if opciones == 5:
        sys.exit()
    if opciones<1 or opciones>5 or opciones==None:
        input("Valor invalido!! Vuelva a intentarlo")
        menu()

