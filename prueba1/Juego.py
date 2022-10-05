from Producto import Producto
class Juego(Producto):
    def __init__(self, codigo: str) -> None:
        super().__init__(codigo)