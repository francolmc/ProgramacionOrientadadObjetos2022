from MySQLConnection import MySQLConnection
from ProcessQuery import ProcessQuery
from MSSQLConnection import MSSQLConnection

# Con esto podemos crear el objeto de conexion
# totalmente libres de la base de datos
# mysqlConnection = MySQLConnection(3306, 'localhost', 'root', '123456', 'contratos_db')
mssqlConnection = MSSQLConnection(443, 'localhost', 'sa', '123456', 'contratos_db2')

# Ahora creamos el objeto que usaremos para poder ejecutar las consultas
# este objeto jamas cambiara, ya que el solo recibe el objeto de conexion
# y su codigo se adatara
processQuery = ProcessQuery(mssqlConnection)

# por ahora esto retornara los textos de la clase MySQLConnection
datos = processQuery.getOneRecord('nombre, apellidos', 'usuarios_tbl', 'id = 12')