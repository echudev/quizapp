import tkinter as tk
import ttkbootstrap as ttk
from controllers.user_controller import UserController

class UserView:
    def __init__(self, root):
        self.root = root
        self.root.title("Bienvenido")
        self.root.geometry("400x400")
        self.username_entry = tk.StringVar()
        self.password_entry = tk.StringVar()
        self.login_frame = ttk.Frame(self.root)
        self.register_frame = ttk.Frame(self.root)
        self.controller = UserController()
        self.create_login_widgets()

    def create_login_widgets(self):
       # Limpiar el frame antes de agregar nuevos widgets
        for widget in self.login_frame.winfo_children():
            widget.destroy()
        
        # Ocultar el frame de registro si está mapeado
        if self.register_frame.winfo_ismapped():
            self.register_frame.pack_forget()

        login_label = ttk.Label(self.login_frame, text="Ingresa con tu nombre de usuario", font=("Arial", 16))
        login_label.pack(pady=10)
        
        # Creo 2 contenedores para los input de username y contraseña y 1 para el botón registrarse
        input_frame1 = ttk.Frame(master = self.login_frame)
        input_frame2 = ttk.Frame(master = self.login_frame)
        input_frame3 = ttk.Frame(master = self.login_frame)       

        # Inputs username y contraseña
        username_label = ttk.Label(master = input_frame1, text="Nombre de usuario")
        username_label.pack(side= 'top', padx=5)
        username_entry = ttk.Entry(master = input_frame1, textvariable= self.username_entry)
        username_entry.pack(side= 'left')
        password_label = ttk.Label(master = input_frame2, text="Contraseña")
        password_label.pack(side= 'top', padx=5)
        password_entry = ttk.Entry(master = input_frame2, textvariable= self.password_entry, show='*')
        password_entry.pack(side= 'left')
        input_frame1.pack(pady=5)
        input_frame2.pack(pady=5)
        
        # Boton para ingresar
        login_button = ttk.Button(master = self.login_frame, text = 'Ingresar', command = self.login)
        login_button.pack(pady=2)

        # Boton para ir a registrarse
        ttk.Label(master = input_frame3, text="¿Todavía no tenés cuenta?", font=("Arial", 11)).pack()
        register_button = ttk.Button(master = input_frame3, text = '¡Registrate!', command = self.create_register_widgets)
        register_button.pack(pady=5)
        input_frame3.pack(side= 'bottom' ,pady=20)
        
        self.login_frame.pack()
    
    def create_register_widgets(self):
        # Limpiar el frame antes de agregar nuevos widgets
        for widget in self.register_frame.winfo_children():
            widget.destroy()
        
        # Ocultar el frame de login si está mapeado
        if self.login_frame.winfo_ismapped():
            self.login_frame.pack_forget()

        register_label = ttk.Label(self.register_frame, text="Registrate con tus datos", font=("Arial", 16))
        register_label.pack(pady=10)
        
        # Creo 2 contenedores para los input de username y contraseña y 1 para el botón registrarse
        input_frame1 = ttk.Frame(master = self.register_frame)
        input_frame2 = ttk.Frame(master = self.register_frame)
        input_frame3 = ttk.Frame(master = self.register_frame)       
        input_frame4 = ttk.Frame(master = self.register_frame)  

        password2_entry = tk.StringVar()
        # Inputs username y contraseña
        username_label = ttk.Label(master = input_frame1, text="Nombre de usuario")
        username_label.pack(side= 'top', padx=5)
        username_entry = ttk.Entry(master = input_frame1, textvariable= self.username_entry)
        username_entry.pack(side= 'left')
        password_label = ttk.Label(master = input_frame2, text="Contraseña")
        password_label.pack(side= 'top', padx=5)
        password_entry = ttk.Entry(master = input_frame2, textvariable= self.password_entry, show='*')
        password_entry.pack(side= 'left')
        password2_label = ttk.Label(master = input_frame4, text="Repita la contraseña")
        password2_label.pack(side= 'top', padx=5)
        password2_entry = ttk.Entry(master = input_frame4, textvariable= password2_entry, show='*')
        password2_entry.pack(side= 'left')
        input_frame1.pack(pady=5)
        input_frame2.pack(pady=5)
        input_frame4.pack(pady=5)
        
        # Boton para ingresar
        login_button = ttk.Button(master = self.register_frame, text = 'Registrarme', command = self.register)
        login_button.pack(pady=2)

        # Boton para ir a RegisterView
        ttk.Label(master = input_frame3, text="Si ya tienes cuenta:", font=("Arial", 11)).pack()
        register_button = ttk.Button(master = input_frame3, text = 'volver a Login', command = self.create_login_widgets)
        register_button.pack(pady=5)
        input_frame3.pack(side= 'bottom' ,pady=20)

        
        self.register_frame.pack()
        
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.login(username, password):
            self.start_game()
            return

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.register(username, password):
            self.start_game()
            return

    def start_game(self):
        self.root.destroy()
        from views.game_view import GameView
        game_root = ttk.Window(themename='solar')
        GameView(game_root)
        game_root.mainloop()
