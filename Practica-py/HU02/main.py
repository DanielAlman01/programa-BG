import database
import visualizarUsuarios

# Crear la base de datos al iniciar la aplicación
database.crear_base_datos()

# Iniciar el servidor web para visualizar usuarios
visualizarUsuarios.iniciar_servidor()
