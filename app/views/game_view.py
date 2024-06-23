import tkinter as tk
from tkinter import ttk

class GameView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
        self.s = ttk.Style()
        self.s.configure('TRadiobutton', font=('Helvetica', 16))

        self.preguntas = self.parent.game_controller.get_preguntas()
        self.pregunta_actual = 0
        self.selected_option = tk.IntVar()
    
        if self.pregunta_actual > len(self.preguntas):
            self.parent.show_frame("IntroView")
        
        intro_label = ttk.Label(self, text=f'Pregunta {self.pregunta_actual+1}', font=("Arial", 12))
        intro_label.pack(pady=10, padx=20, anchor='w')

        self.pregunta_label = ttk.Label(self, text=self.preguntas[self.pregunta_actual].enunciado, font=("Arial", 18), wraplength=550, anchor='center')
        self.pregunta_label.pack(pady=20, padx=20)

        for i, respuesta in enumerate(self.preguntas[self.pregunta_actual].respuestas):
            respuesta_button = ttk.Radiobutton(self, text=f'{respuesta.texto}', variable=self.selected_option, value=i)
            respuesta_button.pack(pady=10)

        
        self.next_button = ttk.Button(self, text='Siguiente', command= lambda: print(self.selected_option.get()))
        self.next_button.pack(pady=30)
