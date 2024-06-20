from models.db import Pregunta, Respuesta
from database.run_query import run_query

class GameModel:
    def __init__(self):
        self.preguntas = []     
 
        
    def set_preguntas(self):
        query = 'SELECT * FROM Preguntas WHERE nivel_id = 1 ORDER BY RANDOM() LIMIT 3;'
        path_db = "./database/preguntas.db"
        rows = run_query(query, path_db)
        for row in rows:  
            # instancio la pregunta
            enunciado, nivel = row[1], row[2]
            nueva_pregunta = Pregunta(nivel, enunciado)
 
            # instancio las respuestas para la pregunta
            query2 = 'SELECT * FROM Respuestas WHERE pregunta_id = ? ORDER BY RANDOM();'
            rows2 = run_query(query2, path_db,(row[0],))
            respuestas = []
            for row_ in rows2:
                 texto, correcta = row_[1], row_[2]
                 nueva_respuesta = Respuesta(texto, correcta)
                 respuestas.append(nueva_respuesta)
            nueva_pregunta.set_respuestas(respuestas)
            self.preguntas.append(nueva_pregunta)
        return self.preguntas