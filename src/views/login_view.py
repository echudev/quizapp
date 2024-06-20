import tkinter as tk
from controllers.user_controller import UserController
from views.register_view import RegisterView  

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.controller = UserController()
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Username").grid(row=0, column=0)
        tk.Label(self.root, text="Password").grid(row=1, column=0)

        self.username_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root, show='*')

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.root, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)
        tk.Button(self.root, text="Register", command=self.show_register).grid(row=3, column=0, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.login(username, password)

    def show_register(self):
        self.root.destroy()
        root = tk.Tk()
        RegisterView(root)
        root.mainloop()
