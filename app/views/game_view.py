import tkinter as tk
from tkinter import ttk

class GameView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) 
        self.parent = parent
        self.parent.title('Quizapp')

        self.s = ttk.Style()
        self.s.configure('TRadiobutton', font=('Helvetica', 16))

        self.preguntas = self.parent.game_controller.get_preguntas()
        self.selected_option = tk.IntVar()

        self.mostrar_pregunta_en_pantalla()

    def mostrar_pregunta_en_pantalla(self):
        pregunta_actual = self.parent.game_controller.get_pregunta_actual()
        contador = self.parent.game_controller.get_contador_preguntas()
        
        self.intro_label = ttk.Label(self, text=f'Pregunta {contador}', font=("Arial", 12))
        self.intro_label.pack(pady=10, padx=20, anchor='w')

        self.enunciado = ttk.Label(self, text=self.preguntas[pregunta_actual].enunciado, font=("Arial", 18), wraplength=550, anchor='center')
        self.enunciado.pack(pady=20, padx=20)
        
        self.respuesta_radiobuttons = []
        self.respuestas_frame = ttk.Frame(self)
        self.respuestas_frame.pack(pady=20, padx=20)
        for i, respuesta in enumerate(self.preguntas[pregunta_actual].respuestas):  
            frame = ttk.Frame(self.respuestas_frame)
            texto = ttk.Label(frame, text=respuesta.texto, font=("Arial", 14), wraplength=500)         
            respuesta_btn = ttk.Radiobutton(
                frame, 
                text='', 
                variable=self.selected_option, 
                value=i, 
                style='TRadiobutton'
                )
            respuesta_btn.pack(pady=10, side='left')
            texto.pack(side='left')
            frame.pack(fill='x', pady=5, anchor='w')
            self.respuesta_radiobuttons.append(frame)

        self.next_button = ttk.Button(self, text='Siguiente', command=self.siguiente_pregunta)
        self.next_button.pack(pady=30, side="bottom")

    
    def actualizar_pregunta_en_pantalla(self):
        pregunta_actual = self.parent.game_controller.get_pregunta_actual()
        contador = self.parent.game_controller.get_contador_preguntas()

        self.intro_label.config(text=f'Pregunta {contador}')
        self.enunciado.config(text=self.preguntas[pregunta_actual].enunciado)

        for frames in self.respuesta_radiobuttons:
            frames.destroy()
        
        for i, respuesta in enumerate(self.preguntas[pregunta_actual].respuestas):   
            frame = ttk.Frame(self.respuestas_frame)
            texto = ttk.Label(frame, text=respuesta.texto, font=("Arial", 14), wraplength=500)           
            respuesta_btn = ttk.Radiobutton(
                frame, 
                text='', 
                variable=self.selected_option, 
                value=i, 
                style='TRadiobutton'
                )
            respuesta_btn.pack(pady=10, side='left')
            texto.pack(side='left')
            frame.pack(fill='x', pady=5, anchor='w')
            self.respuesta_radiobuttons.append(frame)



    def siguiente_pregunta(self):
        pregunta_actual = self.parent.game_controller.get_pregunta_actual()
        contador = self.parent.game_controller.get_contador_preguntas()

        puntos = self.preguntas[pregunta_actual].respuestas[self.selected_option.get()].correcta * 10 * self.parent.game_controller.model.nivel
        self.parent.game_controller.add_puntos(puntos)
        if pregunta_actual >= len(self.preguntas)-1:
            self.siguiente_nivel()
        else:
            self.parent.game_controller.set_pregunta_actual(pregunta_actual + 1)
            self.parent.game_controller.set_contador(contador + 1)
            self.actualizar_pregunta_en_pantalla()  
       
    
    def siguiente_nivel(self):
        contador = self.parent.game_controller.get_contador_preguntas()
        puntos = self.parent.game_controller.get_puntos()
        # si alcanza nivel 5, muestra la pantalla de resultados (solo hay preguntas hasta nivel 4)
        if self.parent.game_controller.next_level() == 5:
            self.parent.user_controller.guardar_resultado(puntos)
            self.parent.show_frame('EndView')
            return 
        # sino, vuelve a generar preguntas con el nuevo nivel 
        self.preguntas = self.parent.game_controller.get_preguntas()
        self.parent.game_controller.set_pregunta_actual(0)
        self.parent.game_controller.set_contador(contador +1)
        self.actualizar_pregunta_en_pantalla()