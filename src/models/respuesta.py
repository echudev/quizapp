class Respuesta:
    def __init__(self, texto: str, correcta: int):
            self.__texto = texto
            self.__correcta = correcta
    
    def get_texto(self):
            return self.__texto
    def get_correcta(self):
            return self.__correcta