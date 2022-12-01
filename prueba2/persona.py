class Persona:
    def __init__(self, email:str = '', nombres:str = '', apellidos:str = '', password:str = '') -> None:
        self.__email = email
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__password = password

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, value:str):
        self.__email = value

    # Propiedades con decoradores
    # @property
    # def email(self) -> str:
    #     return self.__email
    
    # @email.setter
    # def email(self, value:str):
    #     self.__email = value

    def getNombres(self) -> str:
        return self.__nombres

    def setNombres(self, value:str):
        self.__nombres = value

    def getApellidos(self) -> str:
        return self.__apellidos

    def setApellidos(self, value:str):
        self.__apellidos = value

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, value:str):
        self.__password = value

    def insertUser(self) -> str:
        return f"INSERT INTO Persona (email, nombres, apellidos, password) VALUES ('{self.__email}', '{self.__nombres}', '{self.__apellidos}', '{self.__password}')"

    def deleteUser(self) -> str:
        return f"DELETE FROM Persona WHERE email = '{self.__email}'"

    def updateUser(self) -> str:
        return f"UPDATE Persona SET nombres='{self.__nombres}', apellidos='{self.__apellidos}', password='{self.__password}' WHERE email='{self.__email}'"

    def selectByEmail(self) -> str:
        return f"SELECT email, nombres, apellidos, password FROM Persona WHERE email = '{self.__email}'"

    