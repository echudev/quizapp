import tkinter as tk
from tkinter import ttk

class LoginView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.username_entry = tk.StringVar()
        self.password_entry = tk.StringVar()
        self.password2_entry = tk.StringVar()
       
        login_label = ttk.Label(self, text="Ingresa con tu nombre de usuario", font=("Arial", 16))
        login_label.pack(pady=10)
        
        input_frame1 = ttk.Frame(self)
        input_frame2 = ttk.Frame(self)
        input_frame3 = ttk.Frame(self)       

        username_label = ttk.Label(master=input_frame1, text="Nombre de usuario")
        username_label.pack(side='top', padx=5)
        username_entry = ttk.Entry(master=input_frame1, textvariable=self.username_entry)
        username_entry.pack(side='left')
        password_label = ttk.Label(master=input_frame2, text="Contraseña")
        password_label.pack(side='top', padx=5)
        password_entry = ttk.Entry(master=input_frame2, textvariable=self.password_entry, show='*')
        password_entry.pack(side='left')
        input_frame1.pack(pady=5)
        input_frame2.pack(pady=5)
        
        login_button = ttk.Button(self, text='Ingresar', command=self.login_handler)
        login_button.pack(pady=2)

        ttk.Label(master=input_frame3, text="¿Todavía no tenés cuenta?", font=("Arial", 11)).pack()
        register_button = ttk.Button(master=input_frame3, text='¡Registrate!', command=self.go_to_register)
        register_button.pack(pady=5)
        input_frame3.pack(side='bottom', pady=20)
        
        self.pack()

    def login_handler(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # le paso usuario y contraseña al UserController, si la respuesta es True, muestro la pantalla de juego
        if self.parent.user_controller.login(username, password):
            self.parent.show_frame("IntroView")

    def go_to_register(self):
        # vuelve a pantalla de registro
        self.parent.show_frame("RegisterView")