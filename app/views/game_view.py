from tkinter import ttk
from controllers.game_controller import GameController
  

class GameView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = ttk.Label(self, text="PythonQuizados", font=("Arial", 20))
        label.pack(pady=20)