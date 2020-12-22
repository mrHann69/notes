#encoding: UTF-8
"""Descripcion:
esta es la clase main del programa
la cual invoca las clases "Nota()" y la clase "Principal()" """

__author__ = "mrHann69"
__credits__ = "mrHann69"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "mrHann69"
__email__ = "boredhann@gmail.com"
__status__ = "still in development"


from principal import Principal

def main():
    principal = Principal()
    cicle = True
    while cicle:
        print("-------------Menu-------------\n"+"1.crear nota\n"+"2.modificar nota\n"+"3.eliminar nota\n"+"4.listar notas\n"+"0.Salir")
        opcn = int(input("opcion: "))
        if(opcn == 1):
            print("\nCrear Nota \n")
            principal.crearNota()
        elif(opcn == 2):
            print("\nModificar Nota \n")
            principal.modificarNota()
        elif(opcn == 3):
            print("\nEliminar Nota \n")
            principal.eliminarNota()
        elif(opcn == 4):
            print("\nListar Notas \n")
            principal.listarNotas()
        elif(opcn == 0):
            cicle = False

main()
