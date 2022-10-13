from ConnectionDB import ConnectionDB
from BuilderQuery import BuilderQuery

class ProcessQuery:
    def __init__(self, connectionDB: ConnectionDB) -> None:
        self.__connection = connectionDB

    def getOneRecord(self, fields: str, tableName: str, where: str):
        # Procesar consulta y retornar un solo registro
        builderQuery = BuilderQuery()
        self.__connection.openConnection()
        firstRecord = self.__connection.getData(builderQuery.SelectQuery(fields, tableName, where))
        self.__connection.closeConnection()
        return firstRecord

    def getRecords(self, fields: str, tableName: str, where: str):
        # Procesar consulta y retornar todos los registros
        builderQuery = BuilderQuery()
        self.__connection.openConnection()
        allRecords = self.__connection.getData(builderQuery.SelectQuery(fields, tableName, where))
        self.__connection.closeConnection()
        return allRecords

    def updateRecord(self, setValues: str, tableName: str, where: str):
        # Procesar consulta y retornar la cantidad de registros actualizados
        builderQuery = BuilderQuery()
        self.__connection.openConnection()
        recordsAffected = self.__connection.executeQuery(builderQuery.UpdateQuery(setValues, tableName, where))
        self.__connection.closeConnection()
        return recordsAffected

    def insertRecord(self, fields: str, values: str, tableName: str):
        # Procesar consulta y retornar la cantidad de registros actualizados
        builderQuery = BuilderQuery()
        self.__connection.openConnection()
        recordsAffected = self.__connection.executeQuery(builderQuery.InsertQuery(fields, values, tableName))
        self.__connection.closeConnection()
        return recordsAffected

    def deleteRecord(self, tableName: str, where: str):
        # Procesar consulta y retornar la cantidad de registros actualizados
        builderQuery = BuilderQuery()
        self.__connection.openConnection()
        recordsAffected = self.__connection.executeQuery(builderQuery.DeleteQuery(tableName, where))
        self.__connection.closeConnection()
        return recordsAffected
