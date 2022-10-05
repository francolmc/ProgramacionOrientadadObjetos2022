class Cliente:
    def __init__(self, codigo: str) -> None:
        self.__codigo = codigo
        self.nombres = ''
        self.apellidos = ''
        self.email = ''
        self.direccion = ''
        self.tarjetaCredito = ''
    
    def getCodigo(self) -> str:
        return self.__codigo
    
    def mostrar(self):
        print(f'{self.nombres} {self.apellidos}')