import ttkbootstrap as ttk
from views.login_view import LoginView
from views.game_view import GameView
from views.register_view import RegisterView

class App(ttk.Window):
    def __init__(self, *args, **kwargs):
        ttk.Window.__init__(self, *args, **kwargs)
        self.title('QuizApp')
        self.geometry('600x600')
        self.frames = {
            'LoginView': LoginView(self),
            'RegisterView': RegisterView(self),
            'GameView': GameView(self)
            }
    
        self.show_frame('LoginView')

    def show_frame(self, frame_name):
        for frame in self.frames.keys():
            if frame == frame_name:
                self.frames[frame].pack(fill='both', expand=True)
            else:
                self.frames[frame].forget()

    
    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = App(themename='solar')
    app.run()