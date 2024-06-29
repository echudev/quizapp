import tkinter as tk
from database.database import run_query, preguntas_db
from models.pregunta import Pregunta
from models.respuesta import Respuesta

class GameModel: 
    def __init__(self):
        self.preguntas = []
        self.nivel = 1
        self.puntaje = 0
        self.pregunta_actual = 0
        self.contador_preguntas = 1
    

    def get_puntaje(self) -> int:
        return self.puntaje
    
    def get_pregunta_actual(self) -> int:
        return self.pregunta_actual
    
    def set_pregunta_actual(self, num: int) -> int:
        self.pregunta_actual = num
        return self.pregunta_actual
    
    def get_contador_preguntas(self) -> int:
        return self.contador_preguntas
    
    def set_contador(self, num: int):
        self.contador_preguntas = num
        return self.contador_preguntas

    def get_preguntas_nivel(self) -> list[Pregunta]:
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
    
    def reset_game(self):
        self.nivel = 1
        self.preguntas = []
        self.puntaje = 0
        self.pregunta_actual = 0
        self.contador_preguntas = 1

    def next_level(self) -> int:
        self.nivel += 1
        self.preguntas = []
        self.respuestas = []
        return self.nivel
    
    def add_puntos(self, puntos: int) -> int:
        self.puntaje = self.puntaje + puntos
        return self.puntaje