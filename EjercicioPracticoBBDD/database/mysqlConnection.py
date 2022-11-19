import mysql.connector
from mysql.connector import errorcode

class MySQLConnection:
    def __init__(self, host: str, port: int, user: str, pwd: str, database: str) -> None:
        self.__host = host
        self.__port = port
        self.__user = user
        self.__password = pwd
        self.__database = database
        self.__connection = None
        self.__cursor = None

    def connect(self):
        try:
            self.__connection = mysql.connector.connect(
                host = self.__host,
                port = self.__port,
                user = self.__user,
                password = self.__password,
                database = self.__database
            )
            self.__cursor = self.__connection.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Usuario o contrasena incorrecta.')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('La base de datos no existe.')
            else:
                print(err.msg)
    
    def close(self):
        self.__connection.close()
    
    def executeQuery(self, sql: str) -> int:
        self.__cursor.execute(sql)
        result = self.__cursor._affected_rows
        self.__connection.commit()
        return result
    
    def getOneRecord(self, sql: str):
        self.__cursor.execute(sql)
        return self.__cursor.fetchone()

    def getRecords(self, sql: str):
        self.__cursor.execute(sql)
        return self.__cursor.fetchall()