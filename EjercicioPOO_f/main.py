def buscarRegistro():
    print('Buscar registro')

def agregarRegistro():
    print('Agregar registro')

def editarRegistro():
    print('Editar registro')

def eliminarRegistro():
    print('Eliminar registro')

# programa principal con ciclo para mostrar el menu hasta que el usuario salga
option = 0
while option != 5:
    print('1) Buscar registro')
    print('2) Agregar registro')
    print('3) Editar registro')
    print('4) Eliminar registro')
    print('5) Salir')
    option = int(input('Ingresar opcion: '))
    if option == 1:
        buscarRegistro()
    elif option == 2:
        agregarRegistro()
    elif option == 3:
        editarRegistro()
    elif option == 4:
        eliminarRegistro()
