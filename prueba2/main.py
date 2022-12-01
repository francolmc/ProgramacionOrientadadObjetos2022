import bcrypt
from mysqlconnection import MySQLConnection
from persona import Persona

connection = MySQLConnection('localhost', 3306, 'root', 'masterdba', 'prueba3poo')

salt = b'$2b$12$pK6gdgo3uxSpX524yJenee'

def ingresaUsuario():
    persona = Persona()
    persona.setEmail(input('Ingresar email: '))
    persona.setNombres(input('Ingresar nombres: '))
    persona.setApellidos(input('Ingresar apellidos: '))
    pwd = input('Ingresar password: ')
    encryptpwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
    print(encryptpwd)
    persona.setPassword(encryptpwd.decode('utf-8'))
    connection.connect()
    connection.executeQuery(persona.insertUser())
    connection.close()
def buscarUsuario():
    persona = Persona()
    persona.setEmail(input('Ingresar email: '))
    connection.connect()
    print(connection.getOneRecord(persona.selectByEmail()))
    connection.close()
def validarUsuario():
    persona = Persona()
    persona.setEmail(input('Ingresar email: '))
    pwd = input('Ingresar password: ')
    connection.connect()
    usuario = connection.getOneRecord(persona.selectByEmail())
    connection.close()
    if usuario == None:
        print('El usuario no existe.')
    else:
        if(bcrypt.checkpw(pwd.encode('utf-8'), usuario[3].encode('utf-8'))):
            print('Validacion correcta.')
        else:
            print('Los datos no corresponden.')

opcion = 0
while opcion != 4:
    print('1- Ingresar usuario')
    print('2- Buscar usuario')
    print('3- Validar usuario')
    print('4- Salir')
    opcion = int(input('Ingrese su opcion: '))
    if opcion == 1:
        ingresaUsuario()
    elif opcion == 2:
        buscarUsuario()
    elif opcion == 3:
        validarUsuario()