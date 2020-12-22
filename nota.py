"""Descripcion:
CLASE: NOTA
permite la creacion de una nota simple con titulo, fecha y contenido
se usará encapsulamiento"""

class Nota():
    def __init__(self):
        self.__titulo = ""
        self.__fecha = datetime.utcnow()
        self.__contenido = ""

    def set_titulo(self, titulo):
        self.__titulo = titulo
    def get_titulo(self):
        return self.__titulo
"""
    def set_fecha(self, fecha):
        self.__fecha = fecha
    def get_fecha(self):
        return self.__fecha
"""
    def set_contenido(self, contenido):
        self.__contenido = contenido
    def get_contenido(self):
        return self.__contenido
