import sqlite3
import json
import bcrypt

DB_FILE = "colaboradores.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS colaboradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            correo TEXT,
            contraseña TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(correo, contrasena):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    cursor.execute('INSERT INTO colaboradores (correo, contraseña) VALUES (?, ?)', (correo, hashed_password.decode('utf-8')))
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT correo, contraseña FROM colaboradores')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
