class Pregunta:
    def __init__(self, id: int, enunciado: str, nivel: int):
        self.id = id
        self.nivel = nivel
        self.enunciado = enunciado


class Respuesta:
    def __init__(self, texto: str, correcta: int):
            self.text = texto
            self.correcta = correcta


class User:
    def __init__(self, nombre: str, contrasenia: str):
        self.nombre = nombre
        self.contrasenia = contrasenia
