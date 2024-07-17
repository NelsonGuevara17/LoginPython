import psycopg2
from psycopg2 import sql
from tkinter import messagebox

def conectar_db():
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='el nombre de tu base dedatos',
            user='postgres',
            password='tu contraseña'
        )
        return connection
    except Exception as ex:
        messagebox.showerror("Error", f"No se pudo conectar a la base de datos: {ex}")
        return None

def registrar_usuario(nombre, apellido, correo, celular, contrasena):
    connection = conectar_db()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = sql.SQL("INSERT INTO usuarios (nombre, apellido, correo, celular, contrasena) VALUES (%s, %s, %s, %s, %s)")
            cursor.execute(query, (nombre, apellido, correo, celular, contrasena))
            connection.commit()
            cursor.close()
            connection.close()
        except Exception as ex:
            messagebox.showerror("Error", f"No se pudo registrar el usuario: {ex}")
    else:
        messagebox.showerror("Error", "Conexión a la base de datos fallida.")
