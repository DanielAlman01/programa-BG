import sqlite3

# Crear la base de datos y la tabla de usuarios
def crear_base_datos():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (nombre TEXT, edad INTEGER, extranjero INTEGER)''')
    cursor.close()
    conexion.close()

# Obtener todos los usuarios de la base de datos
def obtener_usuarios():
    conexion = sqlite3.connect('database.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios
