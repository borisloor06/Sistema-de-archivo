#menu inicial
def menu():
    opc = int(input(
        """--- Bienvenido al sistema ---
        Seleccione la opcion deseada:
        1. Añadir Estudiantes
        2. Modificar calificaciones
        3. Eliminar Estudiante
        4. Mostrar Estudiantes
        5. Salir
        """ 
    ))
    return opc
