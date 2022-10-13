class ConnectionDB: 
    def __init__(self, port: int, server: str, user: str, password: str, database: str) -> None:
        self.port = port
        self.server = server
        self.user = user
        self.passwor = password
        self.database = database

    def openConnection(self) -> None: 
        pass

    def closeConnection(self) -> None:
        pass

    def executeQuery(self, query: str) -> int:
        pass

    def getData(self, query: str):
        pass