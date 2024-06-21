import tkinter as tk
import ttkbootstrap as ttk
from controllers.user_controller import UserController  


class RegisterView:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.controller = UserController()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username").grid(row=0, column=0)
        tk.Label(self.root, text="Password").grid(row=1, column=0)

        self.username_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root, show='*')

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Register", command=self.register).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Back to Login", command=self.show_login).grid(row=3, column=0, columnspan=2)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.register(username, password):
            self.show_login()
            return

    def show_login(self):
        self.root.destroy()
        from views.login_view import LoginView 
        root = ttk.Window(themename='solar')
        LoginView(root)
        root.mainloop()
