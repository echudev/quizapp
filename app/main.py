import ttkbootstrap as ttk
from views.login_view import LoginView
from views.game_view import GameView
from views.register_view import RegisterView
from views.intro_view import IntroView
from views.end_view import EndView
from views.profile_view import ProfileView
from views.scoretable_view import ScoreTableView
from controllers.user_controller import UserController
from controllers.game_controller import GameController

class App(ttk.Window):
    def __init__(self, *args, **kwargs):
        ttk.Window.__init__(self, *args, **kwargs)
        self.user_controller = UserController()
        self.game_controller = GameController()
        self.title('QuizApp')
        self.geometry('600x600')
        self.frames = {}
    
        self.show_frame('LoginView')

    def create_frame(self, frame_name):
        if frame_name == 'LoginView':
            return LoginView(self)
        elif frame_name == 'RegisterView':
            return RegisterView(self)
        elif frame_name == 'IntroView':
            return IntroView(self)
        elif frame_name == 'GameView':
            return GameView(self)
        elif frame_name == 'ProfileView':
            return ProfileView(self)
        elif frame_name == 'EndView':
            return EndView(self)
        elif frame_name == 'ScoreTableView':
            return ScoreTableView(self)
        else:
            raise ValueError(f"Unknown frame name: {frame_name}")

    def show_frame(self, frame_name):
        # Destruyo frames existentes para asegurar que solo uno esté visible
        for frame in self.frames.values():
            frame.destroy()

        # Creo el frame de nuevo cada vez que se llama a show_frame, 
        # para que se cree con los datos de usuario actualizados
        self.frames[frame_name] = self.create_frame(frame_name)
        self.frames[frame_name].pack(fill='both', expand=True, padx=10, pady=10)


    
    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App(themename='solar')
    app.run()