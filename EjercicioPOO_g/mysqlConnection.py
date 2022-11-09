from errno import errorcode
import mysql.connector
from mysql.connector import errorcode

class MySQLConnection:
    def __init__(self, host: str, port: int, user: str, pwd: str, database: str) -> None:
        self._host = host
        self._port = port
        self._user = user
        self._password = pwd
        self._database = database
        self._connection = None
        self._cursor = None

    def connect(self):
        try:
            self._connection = mysql.connector.connect( # Crear conexion
                host = self._host,
                port = self._port,
                user = self._user,
                password = self._password,
                database = self._database
            )
            self._cursor = self._connection.cursor()
        except mysql.connector.Error as err: # manejo de excepcion al conectarnos con la base de datos
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Usuario o contraseña incorrecta.')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('La base de datos no existe.')
            else:
                print(err.msg)
    
    def close(self):
        self._connection.close()

    def executeQuery(self, sql: str) -> int:
        self._cursor.execute(sql)
        result = self._cursor._affected_rows
        self._connection.commit()
        return result
    
    def getOneRecord(self, sql: str):
        self._cursor.execute(sql)
        return self._cursor.fetchone()

    def getRecords(self, sql: str):
        self._cursor.execute(sql)
        return self._cursor.fetchall()