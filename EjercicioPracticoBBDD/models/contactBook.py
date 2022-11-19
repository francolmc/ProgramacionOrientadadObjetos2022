from models.contact import Contact

class ContactBook:
    def __init__(self, name: str = '') -> None:
        self.__id = 0
        self.__name = name
    
    def getId(self) -> int:
        return self.__id
    
    def setId(self, id: int):
        self.__id = id

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def setContactBookId(self, contactBookId: str):
        self.__contactBookId = contactBookId

    def getInsertQuery(self) -> str:
        return f"INSERT INTO contact_book (name) VALUES ('{self.__name}')"

    def getUpdateQuery(self) -> str:
        return f"UPDATE contact_book SET name='{self.__name}' WHERE id='{self.__id}'"

    def getDeleteQuery(self) -> str:
        return f"DELETE FROM contact_book WHERE id='{self.__id}'"

    def getSelectById(self) -> str:
        return f"SELECT id, name FROM contact_book WHERE id='{self.__id}'"

    def getSelectByName(self) -> str:
        return f"SELECT id, name FROM contact_book WHERE name='{self.__name}'"

    def getSelectAll(self) -> str:
        return f"SELECT id, name FROM contact_book"