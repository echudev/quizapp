from models.respuesta import Respuesta

class Pregunta:
    def __init__(self, id: int, enunciado: str, nivel: int):
        self.id = id
        self.enunciado = enunciado
        self.nivel = nivel
        self.respuestas = []
    
    def add_respuesta(self, respuesta: Respuesta):
        self.respuestas.append(respuesta)