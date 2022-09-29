from Trabajador import Trabajador

class Contrato:
    codigo = ''
    fecha = ''
    remuneracion = 0
    jornada = ''
    __trabajador = None

    def __init__(self) -> None:
        pass

    def setTrabajador(self, trabajador: Trabajador):
        self.__trabajador = trabajador
    
    def getTrabajador(self):
        return self.__trabajador