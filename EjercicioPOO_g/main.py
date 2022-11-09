from product import Product
from mysqlConnection import MySQLConnection

connection = MySQLConnection('localhost', 3306, 'root', 'masterdba', 'purchase_db')

def buscarRegistro():
    product = Product()
    connection.connect()
    userValue = input('Ingrese el id del producto: ')
    result = connection.getOneRecord(product.selectOneRecordSQL(userValue))
    connection.close()
    print(result)

def agregarRegistro():
    # creo producto
    product = Product()
    product.setProductName(input('Ingrese nombre producto: '))
    product.setPrice(input('Ingrese valor producto: '))
    # ejecutar consulta
    connection.connect()
    connection.executeQuery(product.insertSQL())
    connection.close()

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
