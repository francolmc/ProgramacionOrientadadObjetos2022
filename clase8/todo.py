class TODOClass:
    def __init__(self, id: int = 0, todo: str = '', completed: str = False) -> None:
        self.__id = id
        self.__todo = todo
        self.__completed = completed

    def getId(self) -> int:
        return self.__id

    def setId(self, value: int):
        self.__id = value

    def getTodo(self) -> str:
        return self.__todo

    def setTodo(self, value: str):
        self.__todo = value

    def getCompleted(self) -> str:
        return self.__completed

    def setCompleted(self, value: str):
        self.__completed = value