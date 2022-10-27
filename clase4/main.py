from errno import errorcode
import mysql.connector
from mysql.connector import errorcode

try:
    mysqlConnector = mysql.connector.connect( # Crear conexion
        host = 'localhost',
        port = 3306,
        user = 'root',
        password = 'masterdba',
        database = 'pruebas_poo '
    )
    print('Conexion exitosa!!!')

    mysqlCursor = mysqlConnector.cursor() # crear objecto cursos para ejecutar consultas SQL

    mysqlCursor.execute('SHOW TABLES') # ejecutar consulta

    for item in mysqlCursor: # mostrar resultado de la consulta
        print(item)

    mysqlCursor.execute("INSERT INTO user (firstName, lastName, email) VALUES ('Pablo', 'Marmol', 'pablo.marmol@superrito.cl')")

    mysqlConnector.commit()

    mysqlCursor.execute('SELECT * FROM user')

    result = mysqlCursor.fetchall()

    for item in result:
        print(item)
except mysql.connector.Error as err: # manejo de excepcion al conectarnos con la base de datos
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Usuario o contraseña incorrecta.')
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('La base de datos no existe.')
    else:
        print(err.msg)