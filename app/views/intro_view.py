from tkinter import ttk

class IntroView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
               
        label = ttk.Label(self, text=f'Bienvenido a PythonQuizados', font=("Arial", 20))
        label.pack(pady=20)

        intro_label = ttk.Label(self, text="Cuando estes listo presiona Start", font=("Arial", 14))
        intro_label2 = ttk.Label(self, text="Y empezá a responder!", font=("Arial", 14))
        intro_label.pack(pady=2, padx=20)
        intro_label2.pack(pady=2, padx=20)
        

        start_button = ttk.Button(self, text="Start", padding=(20, 10), command = self.start_game)
        start_button.pack(pady=20)
    
    def start_game(self):
        self.parent.show_frame('GameView')