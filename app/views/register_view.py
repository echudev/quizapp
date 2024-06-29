import tkinter as tk
from tkinter import ttk

class RegisterView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title('Quizapp - Registro')
        self.username_entry = tk.StringVar()
        self.password_entry = tk.StringVar()
        self.password2_entry = tk.StringVar()
        
        register_label = ttk.Label(self, text="Registrate con tus datos", font=("Arial", 16))
        register_label.pack(pady=10)
        
        input_frame1 = ttk.Frame(self)
        input_frame2 = ttk.Frame(self)
        input_frame3 = ttk.Frame(self)       
        input_frame4 = ttk.Frame(self)  

        username_label = ttk.Label(master=input_frame1, text="Nombre de usuario")
        username_label.pack(side='top', padx=5)
        username_entry = ttk.Entry(master=input_frame1, textvariable=self.username_entry)
        username_entry.pack(side='left')
        password_label = ttk.Label(master=input_frame2, text="Contraseña")
        password_label.pack(side='top', padx=5)
        password_entry = ttk.Entry(master=input_frame2, textvariable=self.password_entry, show='*')
        password_entry.pack(side='left')
        password2_label = ttk.Label(master=input_frame4, text="Repita la contraseña")
        password2_label.pack(side='top', padx=5)
        password2_entry = ttk.Entry(master=input_frame4, textvariable=self.password2_entry, show='*')
        password2_entry.pack(side='left')
        input_frame1.pack(pady=5)
        input_frame2.pack(pady=5)
        input_frame4.pack(pady=5)
        
        register_button = ttk.Button(self, text='Registrarme', command=self.register)
        register_button.pack(pady=2)

        ttk.Label(master=input_frame3, text="Si ya tienes cuenta:", font=("Arial", 11)).pack()
        login_button = ttk.Button(master=input_frame3, text='Volver a Login', command=self.ir_a_login)
        login_button.pack(pady=5)
        input_frame3.pack(side='bottom', pady=20)

        self.pack()


    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.parent.user_controller.register(username, password):
            self.parent.show_frame("IntroView")

    def ir_a_login(self):
        self.parent.show_frame("LoginView")
