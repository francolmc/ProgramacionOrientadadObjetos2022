from Celular import Celular
from Juego import Juego
from Cliente import Cliente
from Carro import Carro

iphone = Celular('iphone00013')
iphone.setValor(800000)
print(iphone.getCodigo())
iphone.nombre = 'Iphone 13'
iphone.agregarStock()
iphone.agregarStock()
print(iphone.mostrar())

COD = Juego('juego000cod001')
COD.setValor(13000)
COD.nombre = 'Call of dutty'
COD.agregarStock()
print(COD.mostrar())

pedro = Cliente('cli00001')
pedro.nombres = 'Pedro'
pedro.apellidos = 'Rojas'
pedro.email = 'pedro@sucorreo.cl'
print(pedro.mostrar())

carro = Carro('carro0001')
carro.agregarProducto(iphone)
print(carro.getCantidad())
print(carro.getTotal())
carro.agregarProducto(COD)
print(carro.getCantidad())
print(carro.getTotal())