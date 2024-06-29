from tkinter import ttk

class IntroView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
        self.parent.title('Quizapp')
               
        label = ttk.Label(self, text=f'Bienvenido a PythonQuizados', font=("Arial", 20))
        label.pack(pady=20)

        self.username_display = ttk.Label(self, textvariable=self.parent.user_controller.user_model.username, font=("Arial", 20), foreground="lightgreen")
        self.username_display.pack(pady=5)

        intro_label = ttk.Label(self, text="Juego de preguntas y respuestas", font=("Arial", 14))
        intro_label.pack(padx=20)
        intro_label2 = ttk.Label(self, text="sobre el lenguaje Python", font=("Arial", 14))
        intro_label2.pack(padx=5)
    
        start_button = ttk.Button(self, text="Jugar", padding=(20, 10), command = self.start_game)
        start_button.pack(pady=10)

        start_button = ttk.Button(self, text="Perfil", padding=(20, 10), command = self.goto_profile)
        start_button.pack(pady=10)

        exit_button = ttk.Button(self, text="Salir", padding=(20, 10), command = self.salir)
        exit_button.pack(pady=10)
    
    def start_game(self):
        self.parent.game_controller.reset_game()
        self.parent.show_frame('GameView')

    def goto_profile(self):
        self.parent.show_frame('ProfileView')

    def salir(self):
        self.parent.user_controller.logout()
        self.parent.show_frame('LoginView')