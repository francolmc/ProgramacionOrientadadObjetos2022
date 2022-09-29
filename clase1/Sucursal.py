from Negocio import Negocio
from Contrato import Contrato

class Sucursal:
    def __init__(self) -> None:
        self.__negocio = None
        self.__contratos = []
        self.codigo = ''
        self.direccion = ''
    
    def setNegocio(self, negocio: Negocio):
        self.__negocio = negocio

    def getNegocio(self) -> Negocio:
        return self.__negocio

    def setContrato(self, contrato: Contrato):
        self.__contratos.append(contrato)

    def getContratos(self):
        return self.__contratos