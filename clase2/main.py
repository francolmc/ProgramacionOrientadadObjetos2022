from MySQLConnection import MySQLConnection
from ProcessQuery import ProcessQuery

# Con esto podemos crear el objeto de conexion
# totalmente libres de la base de datos
mysqlConnection = MySQLConnection(3306, 'localhost', 'root', '123456', 'contratos_db')

# Ahora creamos el objeto que usaremos para poder ejecutar las consultas
# este objeto jamas cambiara, ya que el solo recibe el objeto de conexion
# y su codigo se adatara
processQuery = ProcessQuery(mysqlConnection)

# por ahora esto retornara los textos de la clase MySQLConnection
processQuery.getOneRecord('nombre, apellidos', 'usuarios_tbl', 'id = 12')