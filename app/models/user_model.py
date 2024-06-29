import sqlite3
import bcrypt
from datetime import datetime
import tkinter as tk
from database.database import run_query, users_db

class UserModel:
    def __init__(self):
        self.username = None
        self.user_id = None
        self.mejor_puntaje = None
        self.partidas_jugadas = None
        self.historial_partidas = []

    def get_name(self):
        return self.username

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
            self.username = nombre
            row = run_query('SELECT id FROM Usuarios WHERE nombre = ?', users_db, (nombre,))
            user = row.fetchone()
            self.user_id = user[0]
            return True, f'Bienvenid@ {self.username}, te registraste correctamente'
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
                    self.username = nombre
                    self.user_id = id
                    self.set_player_stats()
                    self.set_historial_partidas()
                    return True, f'Bienvenid@ {self.username}!'
                else:
                    return False, "Contraseña incorrecta"
        except Exception as e:
            print(e)
            return False, "Error en la conexión con la base de datos"
    
    def guardar_resultado(self, puntaje: int) -> bool:
        # Guardo el resultado de la partida en la base de datos
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now().strftime("%H:%M:%S")
        id = self.user_id
        query = 'INSERT INTO HistorialPartidas (fecha, hora, usuarios_id, puntaje) VALUES (?, ?, ?, ?)'
        try:
            run_query(query, users_db, (current_date, current_time, id, puntaje))
            #Actualizo el puntaje y partidas jugadas del usuario, en la sesión actual
            self.set_player_stats()
            self.set_historial_partidas()
            return True
        except Exception as e:
            print(f"Unexpected error in Usuario.guardar_resultado: {e}")
            return False
    
    def set_player_stats(self):
        query = 'SELECT MAX(puntaje), COUNT(puntaje) FROM HistorialPartidas WHERE usuarios_id = ?'
        id = self.user_id
        response = run_query(query, users_db, (id,))
        row = response.fetchone()
        max_puntaje, partidas_jugadas = row[0], row[1]

        self.partidas_jugadas = partidas_jugadas
        self.mejor_puntaje = max_puntaje

    def get_mejor_puntaje(self) -> int | None:
        return self.mejor_puntaje
    
    def get_partidas_jugadas(self) -> int | None:
        return self.partidas_jugadas

    
    def set_historial_partidas(self):
        query = 'SELECT fecha, hora, puntaje FROM HistorialPartidas WHERE usuarios_id = ?'
        id = self.user_id
        response = run_query(query, users_db, (id,))
        rows = response.fetchall()
        self.historial_partidas = rows
    
    def get_historial_partidas(self) -> list:
        return self.historial_partidas
    

    def logout(self):
        self.username = None
        self.user_id = None
        return True, "Hasta luego!"