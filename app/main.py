import ttkbootstrap as ttk
from views.user_view import UserView

if __name__ == "__main__":
    root = ttk.Window(themename='solar')
    UserView(root)
    root.mainloop()