from app.manageContactBook import ManageContactBook
from database.mysqlConnection import MySQLConnection

connection = MySQLConnection(
    host='localhost',
    port=3306,
    user='root',
    pwd='masterdba',
    database='contact_db'
)
manageContactBook = ManageContactBook(connection)

def showContactBooks():
    manageContactBook.showAllContactBooks()

def selectContactBook():
    name = input('Ingrese nombre agenda: ')
    manageContactBook.selectContactBook(name)

def deleteContactBook():
    manageContactBook.deleteContactBook()

def createContactBook():
    name = input('Ingresar nombre agenda: ')
    manageContactBook.createContactBook(name)

def showContacts():
    manageContactBook.getAllContacts()

def searchContactByName():
    name = input('Ingresar nombre contacto: ')
    manageContactBook.getSearchContactByName(name)

def deleteContact():
    email = input('Ingrese email de contacto: ')
    manageContactBook.deleteContactByEmail(email)

def addContact():
    email = input('Ingresar email: ')
    firstName = input('Ingresar nombres: ')
    lastName = input('Ingresar apellidos: ')
    phone = input('Ingresar telefono: ')
    cellPhone = input('Ingresar celular: ')
    address = input('Ingresar direccion: ')
    manageContactBook.addContact(
        email=email,
        firstName=firstName,
        lastName=lastName,
        phone=phone,
        cellPhone=cellPhone,
        address=address
    )

def editContact():
    # implementar el metodo de editar contacto
    pass

option = 0
while option != 10:
    print('1) Mostrar agendas')
    print('2) Seleccionar agenda')
    print('3) Eliminar agenda')
    print('4) Crear agenda')
    print('5) Mostrar todos los contactos')
    print('6) Buscar contacto por nombre')
    print('7) Eliminar contacto')
    print('8) Agregar contact')
    print('9) Modificar contacto')
    print('10) Salir')
    option = int(input('Ingresar opcion: '))
    if option == 1:
        showContactBooks()
    elif option == 2:
        selectContactBook()
    elif option == 3:
        deleteContactBook()
    elif option == 4:
        createContactBook()
    elif option == 5:
        showContacts()
    elif option == 6:
        searchContactByName()
    elif option == 7:
        deleteContact()
    elif option == 8:
        addContact()
    elif option == 9:
        editContact()