import os
import sqlite3


# Obtengo la ruta absoluta del directorio donde se encuentra el archivo database.py
filename = os.path.abspath(__file__)
dbdir = filename.rstrip('database.py')
# construyo la ruta absoluta a las bases de datos, para poder evitar errores de conexión
users_db = os.path.join(dbdir, "usuarios.db")
preguntas_db = os.path.join(dbdir, 'preguntas.db')


def run_query(query: str, db: str, parameters = ()):
    # usando 'with' se cierra automáticamente la conexión luego de ejecutar la consulta
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result 