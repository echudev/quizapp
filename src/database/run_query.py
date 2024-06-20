import sqlite3

def run_query(query: str, db: str, parameters = ()):
    # usando 'with' se cierra automáticamente la conexión luego de ejecutar la consulta
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result 