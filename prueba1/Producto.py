class Producto:
    def __init__(self, codigo: str) -> None:
        self.__codigo = codigo
        self.__valor = 0
        self.nombre = ''
        self.__cantidad = 0

    def getCodigo(self) -> str:
        return self.__codigo

    def setValor(self, valor: int):
        if valor > 0:
            self.__valor = valor
        else:
            print('ERROR: Solo valores positivos.')

    def getValor(self) -> int:
        return self.__valor

    def agregarStock(self):
        self.__cantidad += 1
    
    def descontarStock(self):
        self.__cantidad -= 1

    def getCantidad(self) -> int:
        return self.__cantidad

    def mostrar(self):
        print(f'{self.nombre}: {self.__cantidad}')

