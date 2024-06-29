import sqlite3
import bcrypt
from datetime import datetime
import tkinter as tk
from database.database import run_query, users_db

class UserModel:
    def __init__(self):
        self.username = tk.StringVar(value="")
        self.user_id = tk.IntVar(value=0)

    def get_name(self):
        print(self.username.get())
        return self.username.get()

    def usuario_existe(self, nombre: str) -> bool:
        query = 'SELECT * FROM Usuarios WHERE nombre = ?'
        response = run_query(query, users_db, (nombre,))
        row = response.fetchone()
        return row is not None
    
    def registrar_usuario(self, nombre: str, contrasenia: str) -> tuple[bool, str]:
        if self.usuario_existe(nombre):
            return False, "El nombre de usaurio ya existe!!"
        
        query = 'INSERT INTO Usuarios (nombre, contrasenia) VALUES (?, ?)'
        hashed_password = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

        try:
            run_query(query, users_db, (nombre, hashed_password))
            self.username.set(nombre)
            row = run_query('SELECT id FROM Usuarios WHERE nombre = ?', users_db, (nombre,))
            user = row.fetchone()
            self.user_id.set(user[0])
            return True, f'Bienvenid@ {self.username.get()}, te registraste correctamente'
        except sqlite3.IntegrityError as e:
            print(f"SQLite IntegrityError: {e}")
            return False, "Error al registrar usuario"
        except Exception as e: 
            print(f"Unexpected error in Usuario.registrar_usuario: {e}")
            return False, "Error inesperado"


    def validar_usuario(self, nombre: str, contrasenia:str) -> tuple[bool, str]:
        query = 'SELECT id, contrasenia FROM Usuarios WHERE nombre = ?'

        try:
            # primero busco id y password que coincidan con el nombre ingresado por el usuario
            response = run_query(query, users_db, (nombre,))
            row = response.fetchone()
    
            # si response.fetchone() devuelve None, significa que no está registrado el nombre de usuario en la bd
            if row is None:
                return False, "Nombre de usuario incorrecto"
            # si encuentra el nombre, devuelve id y password
            else: 
                id, hashed_password = row[0], row[1]
                # Si coincide password db con el que ingresó el usuario, se loguea, sinó devuelve contraseña incorrecta
                coinciden_passwords = bcrypt.checkpw(contrasenia.encode('utf-8'), hashed_password)
                if coinciden_passwords:
                    self.username.set(nombre)
                    self.user_id.set(id)
                    return True, f'Bienvenid@ {self.username.get()}!'
                else:
                    return False, "Contraseña incorrecta"
        except Exception as e:
            print(e)
            return False, "Error en la conexión con la base de datos"
    
    def guardar_resultado(self, puntaje: int) -> bool:
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        id = self.user_id.get()
        query = 'INSERT INTO HistorialPartidas (fecha, hora, usuarios_id, puntaje) VALUES (?, ?, ?, ?)'
        try:
            run_query(query, users_db, (current_date, current_time, id, puntaje))
            return True
        except Exception as e:
            print(f"Unexpected error in Usuario.guardar_resultado: {e}")
            return False

        
    def logout(self):
        self.username.set("")
        self.user_id.set(0)
        return True, "Hasta luego!"