from models.user_model import UserModel
from tkinter import messagebox

class UserController:
    def __init__(self):
        self.model = UserModel()

    def register(self, nombre: str, contrasenia: str) -> bool:
        try:
            success, message = self.model.registrar_usuario(nombre, contrasenia)
            if success:
                messagebox.showinfo("Success", message)
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
            success, message = self.model.validar_usuario(nombre, contrasenia)
            if success:
                messagebox.showinfo("Success", message)
                return True
            else:
                messagebox.showerror("Error", message)
                return False
        except Exception as e:
            print(f"Error in UserController.register: {e}")
            messagebox.showerror("Error")
            return False
