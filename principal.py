"""Descripcion:
esta es la clase PRINCIPAL
la cual tiene la funcion de ejecutar las funciones CRUD
(create, read, update, delete) de las notas """

from nota import Nota
from datetime import datetime

class Principal():
    def __init__(self):
        self.__NotesArray[] = None

    def crearNota(self):
        nota = Nota()
        nota.set_titulo(input("ingrese un titulo: "))
        nota.set_fecha(datetime.utcnow())
    def modificarNota(self):

    def eliminarNota(self):

    def listarNotas(self):
