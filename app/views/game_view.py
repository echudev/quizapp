from tkinter import ttk
from controllers.game_controller import GameController
  

class GameView:
    def __init__(self, root):
        self.root = root
        self.root.title("QuizGame")
        self.root.geometry("400x400")
        self.controller = GameController()
        self.create_game_widgets()

    def create_game_widgets(self):
         welcome_label = ttk.Label(self.root, text="Bienvenido al juego de preguntas y respuestas", font=("Arial", 16))
         welcome_label.pack(pady=10)