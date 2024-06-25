import tkinter as tk
from tkinter import ttk

class GameView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
        self.s = ttk.Style()
        self.s.configure('TRadiobutton', font=('Helvetica', 16))

        self.preguntas = self.parent.game_controller.get_preguntas()
        self.pregunta_actual = tk.IntVar(value=0)
        self.contador_preguntas = tk.IntVar(value=1)
        self.selected_option = tk.IntVar()

        self.mostrar_pregunta_en_pantalla()

    def mostrar_pregunta_en_pantalla(self):
        self.intro_label = ttk.Label(self, text=f'Pregunta {self.contador_preguntas.get()}', font=("Arial", 12))
        self.intro_label.pack(pady=10, padx=20, anchor='w')

        self.enunciado = ttk.Label(self, text=self.preguntas[self.pregunta_actual.get()].enunciado, font=("Arial", 18), wraplength=550, anchor='center')
        self.enunciado.pack(pady=20, padx=20)

        self.respuesta_buttons = []
        for i, respuesta in enumerate(self.preguntas[self.pregunta_actual.get()].respuestas):
            respuesta = ttk.Radiobutton(self, text=f'{respuesta.texto}', variable=self.selected_option, value=i)
            respuesta.pack(pady=10)
            self.respuesta_buttons.append(respuesta)


        self.next_button = ttk.Button(self, text='Siguiente', command=self.siguiente_pregunta)
        self.next_button.pack(pady=30, side="bottom")

    
    def actualizar_pregunta_en_pantalla(self):
        self.intro_label.config(text=f'Pregunta {self.contador_preguntas.get()}')
        self.enunciado.config(text=self.preguntas[self.pregunta_actual.get()].enunciado)
        self.next_button.pack_forget()

        for button in self.respuesta_buttons:
            button.pack_forget()

        self.respuesta_buttons = []
        for i, respuesta in enumerate(self.preguntas[self.pregunta_actual.get()].respuestas):
            respuesta_button = ttk.Radiobutton(self, text=f'{respuesta.texto}', variable=self.selected_option, value=i, style='TRadiobutton')
            respuesta_button.pack(pady=10)
            self.respuesta_buttons.append(respuesta_button)
        self.next_button.pack(pady=30, side="bottom")



    def siguiente_pregunta(self):
        if self.pregunta_actual.get() >= len(self.preguntas)-1:
            self.siguiente_nivel()
        else:
            self.pregunta_actual.set(self.pregunta_actual.get() +1)  
            self.contador_preguntas.set(self.contador_preguntas.get() +1)
            self.actualizar_pregunta_en_pantalla()  
       
    
    def siguiente_nivel(self):
        # si alcanza nivel 5, muestra la pantalla de resultados (solo hay preguntas hasta nivel 4)
        if self.parent.game_controller.next_level() == 5:
            self.parent.show_frame('EndView')
            return 
        # sino, vuelve a generar preguntas con el nuevo nivel 
        self.preguntas = self.parent.game_controller.get_preguntas()
        self.pregunta_actual.set(0)
        self.contador_preguntas.set(self.contador_preguntas.get() +1)
        self.actualizar_pregunta_en_pantalla()