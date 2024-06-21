import tkinter as tk
import ttkbootstrap as ttk
from controllers.user_controller import UserController
from views.register_view import RegisterView 

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")
        self.username_entry = tk.StringVar()
        self.password_entry = tk.StringVar()
        self.controller = UserController()
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Ingresa con tu nombre de usuario", font=("Arial", 16)).pack(pady=10)
        
        # Creo 2 contenedores para los input de username y contraseña y 1 para el botón registrarse
        input_frame1 = ttk.Frame(master = self.root)
        input_frame2 = ttk.Frame(master = self.root)
        input_frame3 = ttk.Frame(master = self.root)       

        # Inputs username y contraseña
        username_label = ttk.Label(master = input_frame1, text="Username")
        username_label.pack(side= 'left', padx=5)
        username_entry = ttk.Entry(master = input_frame1, textvariable= self.username_entry)
        username_entry.pack(side= 'left')
        password_label = ttk.Label(master = input_frame2, text="Password")
        password_label.pack(side= 'left', padx=5)
        password_entry = ttk.Entry(master = input_frame2, textvariable= self.password_entry, show='*')
        password_entry.pack(side= 'left')
        input_frame1.pack(pady=5)
        input_frame2.pack(pady=5)
        
        # Boton para ingresar
        login_button = ttk.Button(master = self.root, text = 'Ingresar', command = self.login)
        login_button.pack(pady=2)

        # Boton para ir a RegisterView
        ttk.Label(master = input_frame3, text="¿Todavía no tenés cuenta?", font=("Arial", 11)).pack()
        register_button = ttk.Button(master = input_frame3, text = 'Registrarse', command = self.show_register)
        register_button.pack(pady=5)
        input_frame3.pack(side= 'bottom' ,pady=20)
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.login(username, password):
            self.show_game()
            return

    def show_register(self):
        self.root.destroy()
        root = tk.Tk()
        RegisterView(root)
        root.mainloop()

    def show_game(self):
        self.root.destroy()
        from views.game_view import GameView
        root = tk.Tk()
        GameView(root)
        root.mainloop()
