from ConnectionDB import ConnectionDB

class MySQLConnection(ConnectionDB):
    def __init__(self, port: int, server: str, user: str, password: str, database: str) -> None:
        super().__init__(port, server, user, password, database)

    def openConnection(self) -> None: 
        print('Configurar conexion con libreria de MySQL Server')

    def closeConnection(self) -> None:
        print('Programar cierre de conexion')

    def executeQuery(self, query: str) -> int:
        print('Ejecutar consulta y retornar el numero de filas afectdas')

    def getData(self, query: str):
        print('Ejecutar consulta y retornar la data obtenida de la consulta')