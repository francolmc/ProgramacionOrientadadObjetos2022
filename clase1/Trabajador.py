class Trabajador:
    codigo = ''
    nombres = ''
    apellidoPaterno = ''
    apellidoMaterno = ''

    def __init__(self, codigo: str) -> None:
        self.codigo = codigo
        self.__edad = 0
    
    def __str__(self) -> str:
        return f'nombres: {self.nombres} a. paterno: {self.apellidoPaterno} a. materno: {self.apellidoMaterno}'

    def setEdad(self, valor: int) -> None:
        if valor < 0:
            print('ERROR: Solo valores positivos')
        else:
            self.__edad = valor
    
    def getEdad(self) -> int:
        return self.__edad