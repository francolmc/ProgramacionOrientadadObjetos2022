class Contact:
    def __init__(self, email: str = "", firstName: str = "", lastName: str = "", phone: str = "", cellPhone: str = "", address: str = "", contactBookId: int = 0) -> None:
        self.__email = email
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phone = phone
        self.__cellPhone = phone
        self.__address = address
        self.__contactBookId = contactBookId

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str):
        self.__email = email

    def getFirstName(self) -> str:
        return self.__firstName

    def setFirstName(self, firstName: str):
        self.__firstName = firstName
    
    def getLastName(self) -> str:
        return self.__lastName

    def setLastName(self, lastName: str):
        self.__lastName = lastName

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone: str):
        self.__phone = phone
    
    def getCellPhone(self) -> str:
        return self.__cellPhone

    def setCellPhone(self, cellPhone: str):
        self.__cellPhone = cellPhone
    
    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, address: str):
        self.__address = address

    def getContactBookId(self) -> str:
        return self.__contactBookId

    def setContactBookId(self, contactBookId: str):
        self.__contactBookId = contactBookId

    def getInsertQuery(self) -> str:
        return f"INSERT INTO contact (email, first_name, last_name, phone, cell_phone, address, contact_book_id) VALUES ('{self.__email}', '{self.__firstName}', '{self.__lastName}', '{self.__phone}', '{self.__cellPhone}', '{self.__address}', '{self.__contactBookId}')"

    def getUpdateQuery(self) -> str:
        return f"UPDATE contact SET first_name='{self.__firstName}' last_name='{self.__lastName}' phone='{self.__phone}' cell_phone='{self.__cellPhone}' address='{self.__address}' WHERE email='{self.__email}'"

    def getDeleteQuery(self) -> str:
        return f"DELETE FROM contact WHERE email='{self.__email}'"

    def getSelectByEmail(self) -> str:
        return f"SELECT email, first_name, last_name, phone, cell_phone, address, contact_book_id FROM contact WHERE email='{self.__email}'"

    def getSelectByName(self) -> str:
        return f"SELECT email, first_name, last_name, phone, cell_phone, address, contact_book_id FROM contact WHERE (first_name LIKE '%{self.__firstName}%' OR last_name LIKE '%{self.__lastName}%') AND contact_book_id = '{self.__contactBookId}'"

    def getSelectAllByContactBookId(self) -> str:
        return f"SELECT email, first_name, last_name, phone, cell_phone, address, contact_book_id FROM contact WHERE contact_book_id='{self.__contactBookId}'"