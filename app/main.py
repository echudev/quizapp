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
        self.frames = {
            'LoginView': LoginView(self),
            'RegisterView': RegisterView(self),
            'IntroView': IntroView(self),
            'GameView': GameView(self),
            'ProfileView': ProfileView(self),
            'EndView': EndView(self),
            'ScoreTableView': ScoreTableView(self)
            }
    
        self.show_frame('LoginView')

    def show_frame(self, frame_name):
        for frame in self.frames.keys():
            if frame == frame_name:
                if frame == 'GameView':
                    self.frames[frame].destroy() 
                    self.frames[frame] = GameView(self)
                self.frames[frame].pack(fill='both', expand=True)
            else:
                self.frames[frame].forget()

    
    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App(themename='solar')
    app.run()