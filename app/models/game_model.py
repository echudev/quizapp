import tkinter as tk
from database.database import run_query, preguntas_db
from models.pregunta import Pregunta
from models.respuesta import Respuesta

class GameModel: 
    def __init__(self):
        self.preguntas = []
        self.nivel = 1
        self.puntaje = tk.IntVar(value=0)
        self.pregunta_actual = tk.IntVar(value=0)
        self.contador_preguntas = tk.IntVar(value=1)
    

    def get_puntaje(self):
        return self.puntaje.get()
    
    def get_pregunta_actual(self):
        return self.pregunta_actual.get()
    
    def set_pregunta_actual(self, num: int):
        return self.pregunta_actual.set(num)
    
    def get_contador_preguntas(self):
        return self.contador_preguntas.get()
    
    def set_contador(self, num: int):
        return self.contador_preguntas.set(num)

    def get_preguntas_nivel(self):
        # 1) traigo 3 preguntas de la base de datos, en orden aleatorio, de un nivel determinado
        query_preguntas = 'SELECT * FROM Preguntas WHERE nivel_id = ? ORDER BY RANDOM() LIMIT 3;'
        rows_preguntas = run_query(query_preguntas, preguntas_db,(self.nivel,))
        for row in rows_preguntas:  
            pregunta_id, enunciado, nivel = row[0], row[1], row[2]
            # 2) Creo la pregunta y traigo de la db las respuestas correspondientes
            nueva_pregunta = Pregunta(pregunta_id, enunciado, nivel)
            query_respuestas = 'SELECT * FROM Respuestas WHERE pregunta_id = ? ORDER BY RANDOM();'
            rows_respuestas = run_query(query_respuestas, preguntas_db,(pregunta_id,))
            for row in rows_respuestas:
                id, texto, correcta = row[0], row[1], row[2]
                nueva_pregunta.add_respuesta(Respuesta(id, texto, correcta))
            self.preguntas.append(nueva_pregunta)
        return self.preguntas

    def next_level(self) -> int:
        self.nivel += 1
        self.preguntas = []
        self.respuestas = []
        return self.nivel
    
    def add_puntos(self, puntos: int) -> int:
        self.puntaje.set(self.puntaje.get() + puntos)
        return self.puntaje.get()