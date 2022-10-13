class BuilderQuery:
    def SelectQuery(self, fields: str, tableName: str, condition: str) -> str:
        return f'SELECT {fields} FROM {tableName} WHERE {condition}'

    def UpdateQuery(self, setValues: str, tableName: str, condition: str) -> str:
        return f'UPDATE {tableName} SET {setValues} WHERE {condition}'

    def InsertQuery(self, fields: str, values: str, tableName: str) -> str:
        return f'INSERT INTO {tableName} ({fields}) VALUES {values}'

    def DeleteQuery(self, tableName: str, condition: str) -> str:
        return f'DELETE FROM {tableName} WHERE {condition}'