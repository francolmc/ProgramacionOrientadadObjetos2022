from Trabajador import Trabajador

class Administrativo(Trabajador):
    supervisor = False
    
    def __init__(self, codigo: str) -> None:
        super().__init__(codigo)
    