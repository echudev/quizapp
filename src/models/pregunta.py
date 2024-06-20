from models.respuesta import Respuesta

class Pregunta:
    def __init__(self, nivel: int, enunciado: str):
        self.__nivel = nivel
        self.__enunciado = enunciado
        self.__respuestas: list[Respuesta] = []
        self.preguntas = []

    def get_enunciado(self):
            return self.__enunciado
    
    def set_respuestas(self, respuestas):
            self.__respuestas = respuestas
            
    def get_texto_respuestas(self):
            lista: list[str] = []
            for respuesta in self.__respuestas:
                 lista.append(respuesta.get_texto())
            return lista
            
    def get_nivel(self):
            return self.__nivel