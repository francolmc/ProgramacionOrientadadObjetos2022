
from Negocio import Negocio
from Administrativo import Administrativo
from Sucursal import Sucursal
from Trabajador import Trabajador

negocio = Negocio('Mi negocio', 'Su casa 1234')
negocio.giro = 'Venta de PCs'
sucursal = Sucursal()
sucursal.codigo = '000001'
sucursal.direccion = 'Su negocio 123'
sucursal.setNegocio(negocio)
print(sucursal.getNegocio().giro)