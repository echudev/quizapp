import sqlite3
import bcrypt
import tkinter as tk
from database.database import run_query, users_db

class UserModel:
    def __init__(self):
        self.username = tk.StringVar(value="guest")

    def get_name(self):
        print(self.username.get())
        return self.username.get()

    def usuario_existe(self, nombre):
        query = 'SELECT * FROM Usuarios WHERE nombre = ?'
        db = "./database/usuarios.db"
        response = run_query(query, db, (nombre,))
        user = response.fetchone()
        return user is not None
    
    def registrar_usuario(self, nombre, contrasenia):
        if self.usuario_existe(nombre):
            return False, "El nombre de usaurio ya existe!!"
        
        query = 'INSERT INTO Usuarios (nombre, contrasenia) VALUES (?, ?)'
        hashed_password = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())

        try:
            run_query(query, users_db, (nombre, hashed_password))
            self.username.set(nombre)
            return True, f'Bienvenid@ {self.username}, te registraste correctamente'
        except sqlite3.IntegrityError as e:
            print(f"SQLite IntegrityError: {e}")
            return False, "Error al registrar usuario"
        except Exception as e:
            print(f"Unexpected error in Usuario.registrar_usuario: {e}")
            return False, "Error inesperado"


    def validar_usuario(self, nombre, contrasenia):
        query = 'SELECT contrasenia FROM Usuarios WHERE nombre = ?'

        try:
            # primero chequeo que haya un password para el nombre de usuario
            response = run_query(query, users_db, (nombre,))
            password = response.fetchone()
            
            # si no encuentra nada, es porque el nombre de usuario no existe
            if password is None:
                return False, "Nombre de usuario incorrecto"
            # si encuentra un password, lo des-hasheo y verifico que sea igual al que ingresó el usuario
            else: 
                # Si coinciden, el usuario está logueado, sinó devuelve contraseña incorrecta
                stored_hashed_password = password[0]
                coinciden_passwords = bcrypt.checkpw(contrasenia.encode('utf-8'), stored_hashed_password)
                if coinciden_passwords:
                    self.username.set(nombre)
                    return True, f'Bienvenid@ {self.username.get()}!'
                else:
                    return False, "Contraseña incorrecta"
                
        except Exception as e:
            print(e)
            return False, "Error en la conexión con la base de datos"