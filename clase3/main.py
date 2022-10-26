from errno import errorcode
import mysql.connector
from mysql.connector import errorcode

try:
    mysqlConnector = mysql.connector.connect( # Crear conexion
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'masterdba',
        database = 'andes'
    )
    print('Conexion exitosa!!!')

    mysqlCursor = mysqlConnector.cursor() # crear objecto cursos para ejecutar consultas SQL

    mysqlCursor.execute('SHOW TABLES') # ejecutar consulta

    for item in mysqlCursor: # mostrar resultado de la consulta
        print(item)

except mysql.connector.Error as err: # manejo de excepcion al conectarnos con la base de datos
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario o contraseña incorrecta.')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('La base de datos no existe.')
    else:
        print('Error en la conexion.')