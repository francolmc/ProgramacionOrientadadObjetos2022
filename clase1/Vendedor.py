from Trabajador import Trabajador

class Vendedor(Trabajador):
    def __init__(self, codigo: str) -> None:
        super().__init__(codigo)