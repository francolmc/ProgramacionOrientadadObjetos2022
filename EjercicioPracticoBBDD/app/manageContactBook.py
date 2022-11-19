from database.mysqlConnection import MySQLConnection
from models.contact import Contact
from models.contactBook import ContactBook

# Clase que nos permitira administrar la agenda de contactos
class ManageContactBook:
    def __init__(self, connection: MySQLConnection) -> None:
        self.__connection = connection
        self.__contactBook = None

    def createContactBook(self, name: str):
        self.__connection.connect()
        # este objeto es solo para crear.
        contactBook = ContactBook(name)
        result = self.__connection.executeQuery(contactBook.getInsertQuery())
        self.__connection.close()
        if result > 0:
            print('Agenda creada.')
        else:
            print('Error: La agenda no pudo ser creada.')

    def deleteContactBook(self):
        if (self.__contactBook == None):
            print('Debe seleccionar una agenda.')
        else:
            self.__connection.connect()
            contact = Contact(contactBookId=self.__contactBook.getId())
            resultContacts = self.__connection.getRecords(contact.getSelectAllByContactBookId())
            for item in resultContacts:
                contact.setEmail(item[0])
                self.__connection.executeQuery(contact.getDeleteQuery())
            result = self.__connection.executeQuery(self.__contactBook.getDeleteQuery())
            if result > 0:
                self.__contactBook = None
                print('Agenda fue eliminada.')
            else:
                print('Error: La agenda no pudo ser eliminada.')
            self.__connection.close()

    def selectContactBook(self, name: str):
        self.__connection.connect()
        # este objeto es solo para la busqueda.
        contactBook = ContactBook(name)
        result = self.__connection.getOneRecord(contactBook.getSelectByName())
        if result == None:
            print('La agenda con este nombre no existe.')
        else:
            # este objecto es global para luego administrar los contactos de esta agenda seleccionada
            self.__contactBook = ContactBook(result[1]) # se asgina el nombre por el constructor
            self.__contactBook.setId(result[0]) # se asgina el id por este medio ya que el constructor no lo permite
            print('Agenda seleccionada.')
        self.__connection.close()

    def showAllContactBooks(self):
        self.__connection.connect()
        # este objeto es solo para la busqueda.
        contactBook = ContactBook()
        result = self.__connection.getRecords(contactBook.getSelectAll())
        if result.__len__() <= 0:
            print(f'No existen agendas registradas.')
        else:
            for item in result:
                print(f'id: {item[0]}, nombre: {item[1]}')
        self.__connection.close()

    def getAllContacts(self):
        self.__connection.connect()
        if self.__contactBook == None:
            print('Debe seleccionar una agenda')
        else:
            contact = Contact(contactBookId=self.__contactBook.getId())
            result = self.__connection.getRecords(contact.getSelectAllByContactBookId())
            if result.__len__() <= 0:
                print(f'La agenda "{self.__contactBook.getName()}" no tiene contactos.')
            else:
                for item in result:
                    print(f'email: {item[0]}, nombres: {item[1]}, apellidos: {item[2]}')
        self.__connection.close()

    def getSearchContactByName(self, name: str):
        if (self.__contactBook == None):
            print('Debe seleccionar una agenda.')
        else:
            self.__connection.connect()
            contact = Contact(firstName=name, lastName=name, contactBookId=self.__contactBook.getId())
            result = self.__connection.getRecords(contact.getSelectByName())
            if result.__len__() <= 0: 
                print('No existen contactos con este nombre')
            else:
                for item in result:
                    print(f'email: {item[0]}, nombres: {item[1]}, apellidos: {item[2]}, telefono: {item[3]}, celular: {item[4]}, direccion: {item[5]}')
            self.__connection.close()

    def deleteContactByEmail(self, email: str):
        if (self.__contactBook == None):
            print('Debe seleccionar una agenda.')
        else:
            self.__connection.connect()
            contact = Contact(email=email)
            result = self.__connection.executeQuery(contact.getDeleteQuery())
            if result <= 0: 
                print('Error: no fue posible eliminar el contacto.')
            else:
                print('Contacto eliminado.')
            self.__connection.close()

    def addContact(self, email: str, firstName: str, lastName: str, phone: str, cellPhone: str, address: str):
        if (self.__contactBook == None):
            print('Debe seleccionar una agenda.')
        else:
            self.__connection.connect()
            contact = Contact(
                email=email,
                firstName=firstName,
                lastName=lastName,
                phone=phone,
                cellPhone=cellPhone,
                address=address,
                contactBookId=self.__contactBook.getId()
            )
            result = self.__connection.executeQuery(contact.getInsertQuery())
            if result <= 0: 
                print('Error: no fue posible agregar el contacto.')
            else:
                print('Contacto agregado.')
            self.__connection.close()