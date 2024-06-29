from models.user_model import UserModel
from tkinter import messagebox

class UserController:
    def __init__(self):
        self.user_model = UserModel()
    
    def get_user(self):
        return self.user_model.get_name()


    def register(self, nombre: str, contrasenia: str) -> bool:
        try:
            success, message = self.user_model.registrar_usuario(nombre, contrasenia)
            if success:
                messagebox.showinfo("Bienvenido", message)
                return True
            else:
                messagebox.showerror("Error", message)
                return False
        except Exception as e:
            print(f"Error in UserController.register: {e}")
            messagebox.showerror("Error")
            return False

    def login(self, nombre: str, contrasenia: str) -> bool:
        try:
            success, message = self.user_model.validar_usuario(nombre, contrasenia)
            if success:
                messagebox.showinfo("Bienvenido", message)
                return True
            else:
                messagebox.showerror("Error", message)
                return False
        except Exception as e:
            print(f"Error in UserController.register: {e}")
            messagebox.showerror("Error")
            return False
        
    def guardar_resultado(self, puntos: int):
        try:
            self.user_model.guardar_resultado(puntos)
            return True
        except Exception as e:
            print(f"Error in UserController.guardar_resultado: {e}")
            return False
    
    def get_player_stats(self) -> tuple[int, int] | bool:
        try:
            return self.user_model.get_player_stats()
        except Exception as e:
            print(f"Error in UserController.get_user_stats: {e}")
            return False
    
    def get_historial_partidas(self) -> list[tuple[str, str, int]] | bool:
        try:
            return self.user_model.get_historial_partidas()
        except Exception as e:
            print(f"Error in UserController.get_historial_partidas: {e}")
            return False

    def logout(self):
        try:
            success, message = self.user_model.logout()
            if success:
                messagebox.showinfo("Hasta luego!", message)
                return True
            else:
                messagebox.showerror("Error", message)
                return False
        except Exception as e:
            print(f"Error in UserController.register: {e}")
            messagebox.showerror("Error")
            return False
