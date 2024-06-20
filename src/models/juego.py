from models.pregunta import Pregunta
from models.respuesta import Respuesta
from database.run_query import run_query

class Juego:
    def __init__(self):
        self.preguntas = []       
        
    def get_preguntas(self):
        if len(self.preguntas) == 0:
            return False
        else:
            for pregunta in self.preguntas:
                print(pregunta.get_enunciado())
                print(pregunta.get_texto_respuestas())    
                user_choice = input('ingrese su respuesta: ')
            return
        
    def set_preguntas(self):
        query = 'SELECT * FROM Preguntas WHERE nivel_id = 1 ORDER BY RANDOM() LIMIT 3;'
        db = "./database/preguntas.db"
        rows = run_query(query, db)
        for row in rows:  
            # instancio la pregunta
            enunciado, nivel = row[1], row[2]
            nueva_pregunta = Pregunta(nivel, enunciado)
 
            # instancio las respuestas para la pregunta
            query2 = 'SELECT * FROM Respuestas WHERE pregunta_id = ? ORDER BY RANDOM();'
            rows2 = run_query(query2, db,(row[0],))
            respuestas = []
            for row_ in rows2:
                 texto, correcta = row_[1], row_[2]
                 nueva_respuesta = Respuesta(texto, correcta)
                 respuestas.append(nueva_respuesta)
            nueva_pregunta.set_respuestas(respuestas)
            self.preguntas.append(nueva_pregunta)
        return self.preguntas


    def jugar(self):
        self.set_preguntas()
        self.get_preguntas()
        return  