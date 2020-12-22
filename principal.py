"""Descripcion:
esta es la clase PRINCIPAL
la cual tiene la funcion de ejecutar las funciones CRUD
(create, read, update, delete) de las notas """

from nota import Nota
from datetime import datetime

class Principal():
    def __init__(self):
        self.__NotesArray = []

##create a note asking user for params
    def crearNota(self):
        nota = Nota()
        nota.set_titulo(input("ingrese un titulo: "))
        nota.set_fecha(input("ingrese la fecha: "))
        nota.set_contenido(input("contenido: "))
        self.__NotesArray.append(nota)
##modify a note by it's tittle
    def modificarNota(self):
        if (self.__NotesArray is None):
            print("No hay notas para modificar")
        elif(self.__NotesArray == []):
            print("Nada que modificar, lista vacia")
        else:
            bsq = input("ingrese el titulo que desea modificar ")
            for i in self.__NotesArray:
                if(i.get_titulo() == bsq):
                    print("seleccione que desea modificar")
                    print("1. titulo")
                    print("2. contenido")
                    print("3. fecha")
                    ind = int(input("opcion: "))
                    if(ind == 1):
                        i.set_titulo(input("ingrese nuevo titulo: "))
                    elif(ind == 2):
                        i.set_contenido(input("nuevo contenido: "))
                    elif(ind == 3):
                        i.set_fecha(input("nueva fecha: "))

##delete a note from the array of notes by it's tittle
    def eliminarNota(self):
        if(self.__NotesArray is None):
            print("Nada que eliminar")
        elif(self.__NotesArray == []):
            print("Nada que eliminar, lista vacia")
        else:
            bsq = input("ingrese el titulo a eliminar ")
            for i in self.__NotesArray:
                if(i.get_titulo() == bsq):
                    self.__NotesArray.remove(i)

##shows all the notes in the array
    def listarNotas(self):
        if(self.__NotesArray is None):
            print("Nada que mostrar")
        elif(self.__NotesArray == []):
            print("Nada que mostrar, lista vacia")
        else:
            for i in self.__NotesArray:
                print("__________________________"+i.get_titulo()+"\n"+i.get_fecha()+"\n"+i.get_contenido()+"__________________________")
