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
    # Buscar registro unico por nombre
    product = Product()
    product.setProductName(input('Nombre producto a editar: '))
    connection.connect()
    result = connection.getOneRecord(product.selectOneRecordByNameSQL())
    if result == None:
        print('El registro no existe')
    else:
        # Construir objeto producto con los valores de la tabla
        product.setId(result[0])
        product.setProductName(result[1])
        product.setPrice(result[2])
        # Solicitar al usuario los nuevos valores del producto
        productName = input(f'Nombre ({product.getProductName()}): ')
        price = input(f'Precio ({product.getPrice()}): ')
        if productName != '':
            product.setProductName(productName)
        if price != '':
            product.setPrice(price)
        # Guardar el objeto con los nuevos valores en la tabla
        connection.executeQuery(product.updateSQL())
        connection.close()

def eliminarRegistro():
    # Buscar registro unico por nombre
    product = Product()
    product.setProductName(input('Nombre producto a eliminar: '))
    connection.connect()
    result = connection.getOneRecord(product.selectOneRecordByNameSQL())
    if result == None:
        print('El registro no existe')
    else:
        product.setId(result[0])
        # Eliminar el registro de la tabla
        connection.executeQuery(product.deleteSQL())
        connection.close()

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
