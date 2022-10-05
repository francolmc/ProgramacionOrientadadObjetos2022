from math import prod
from Cliente import Cliente
from Producto import Producto

class Carro:
    def __init__(self, codigo: str) -> None:
        self.__codigo = codigo
        self.__cliente: Cliente = None
        self.__listaProductos = []

    def getCodigo(self) -> str:
        return self.__codigo

    def setCliente(self, cliente: Cliente):
        self.__cliente = cliente

    def getCliente(self) -> Cliente:
        return self.__cliente
    
    def agregarProducto(self, producto: Producto):
        self.__listaProductos.append(producto)
        producto.descontarStock()

    def getTotal(self) -> int:
        suma = 0
        for producto in self.__listaProductos:
            suma = suma + producto.getValor()
        return suma
    
    def getCantidad(self) -> int:
        return len(self.__listaProductos)