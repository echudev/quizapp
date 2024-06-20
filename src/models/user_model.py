import sqlite3
import bcrypt
from database.run_query import run_query

class User:
    def __init__(self):
        self.__nombre = None
        self.__puntaje = 0
        self.__historial = []

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    
    def set_puntaje(self, puntaje):
        self.__puntaje += puntaje
    
    def get_puntaje(self):
        return self.__puntaje
    
    def set_historial(self):
        pass

    def get_historial(self):
        return self.__historial


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
        db = "./database/usuarios.db"
        hashed_password = bcrypt.hashpw(contrasenia.encode('utf-8'), bcrypt.gensalt())


        try:
            run_query(query, db, (nombre, hashed_password))
            return True, "Usuario registrado correctamente"
        except sqlite3.IntegrityError as e:
            print(f"SQLite IntegrityError: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error in Usuario.registrar_usuario: {e}")
            return False


    def validar_usuario(self, nombre, contrasenia):

        query = 'SELECT contrasenia FROM Usuarios WHERE nombre = ?'
        db = "./database/usuarios.db"

        try:
            # primero chequeo que haya un password para el nombre de usuario
            response = run_query(query, db, (nombre,))
            password = response.fetchone()
            
            # si no encuentra nada, es porque el nombre de usuario no existe
            if password is None:
                return False, "Nombre de usuario incorrecto"
            # si encuentra un password, lo des-hasheo y verifico que sea igual al que ingresó el usuario
            else: 

                stored_hashed_password = password[0]
                result = bcrypt.checkpw(contrasenia.encode('utf-8'), stored_hashed_password)
                if result:
                    return True, f'Bienvenido {nombre}'
                else:
                    return False, "Contraseña incorrecta"
                
        except Exception as e:
            print(e)
            return False