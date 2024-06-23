from models.game_model import GameModel
from models.pregunta import Pregunta

class GameController:
    def __init__(self):
        self.model = GameModel()


    def get_preguntas(self) -> list[Pregunta]:
        return self.model.get_preguntas_nivel()
      
    def next_level(self) -> int:
        return self.model.next_level()
    
    def get_puntos(self):
        return self.model.puntos
    
    def add_puntos(self, puntos: int) -> int:
        return self.model.add_puntos(puntos)