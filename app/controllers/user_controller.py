from models.user_model import UserModel
from tkinter import messagebox

class UserController:
    def __init__(self):
        self.model = UserModel()

    def register(self, nombre, contrasenia):
        try:
            success, message = self.model.registrar_usuario(nombre, contrasenia)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        except Exception as e:
            print(f"Error in UserController.register: {e}")
            messagebox.showerror("Error")

    def login(self, nombre, contrasenia):
        try:
            success, message = self.model.validar_usuario(nombre, contrasenia)
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
        except Exception as e:
            print(f"Error in UserController.register: {e}")
            messagebox.showerror("Error")
