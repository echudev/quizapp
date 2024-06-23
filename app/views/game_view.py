from tkinter import ttk  

class GameView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
        label = ttk.Label(self, text="Bienvenido a PythonQuizados", font=("Arial", 20))
        label.pack(pady=20)
        self.preguntas = self.parent.game_controller.get_preguntas()
        
       
        intro_label = ttk.Label(self, text=f'Estás Jugando!', font=("Arial", 24))
        intro_label.pack(pady=2, padx=20)

    