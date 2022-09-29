class Negocio:
    RUT = ''
    nombre = ''
    direccion = ''
    representante = ''
    nombreComercial = ''
    giro = ''

    def __init__(self, RUT: str, nombre: str, direccion: str = '') -> None:
        self.RUT = RUT
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self) -> str:
        return f'Nombre: {self.nombre} Direccion: {self.direccion}'
