from models.game_model import GameModel

class GameController:
    def __init__(self):
        self.service = GameModel()

    def start_game(self, nombre_usuario):
        self.service.start_game(nombre_usuario)