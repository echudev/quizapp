import tkinter as tk
import ttkbootstrap as ttk
from views.login_view import LoginView

if __name__ == "__main__":
    root = ttk.Window(themename='solar')
    LoginView(root)
    root.mainloop()