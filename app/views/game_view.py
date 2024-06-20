from controllers.game_controller import GameController
  

class GameView:
    def __init__(self, root):
        self.root = root
        self.root.title("Game")
        self.controller = GameController()
        self.create_widgets()

    def create_widgets(self):
        pass  