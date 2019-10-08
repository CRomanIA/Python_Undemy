#Docstring - Cadenas para documentacion
def saludar(nombre):
    """
    Esto sera un comentario del metodo saludar
    Esta funcion recibira como parametro una cadena con el nombre e
    imprimira por pantalla el saludo con el nombre concatenado
    """
    print ("buenos dias "+ nombre)
saludar("Luigi Ql")

help(saludar)

class Saludos: 
    """
    Esta clase tiene la funcion de buenos dias buenas tardes
    recibira como parametro un nombre
    """
    def buenos_dias(self, nombre):
        """Esta funcion sirve para decir buenos dias"""
        print("Buenos dias {}" .format(nombre))
    def adios(self, nombre):
        """ Esta funcion sirve para decir adios"""
        print("Adios {} ".format(nombre))

saludo = Saludos()
saludo.buenos_dias("Luigi ql gay")
help(Saludos)

#Para ver ayuda de otros metodos
help(print)
help(len)