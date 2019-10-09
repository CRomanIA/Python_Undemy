#Doctest - Generar pruebas dentro de la documentacion

def sumar(numero1, numero2):
    """
    Esto es la documentacion de este metodo
    Recibe dos numeros como parametros y devuelve su suma
    Se genera la prueba en los comentarios (No olvidar en el mayor que, darle un espacio)
    (suma correcta)
    >>> sumar(4,3)
    7
    (suma correcta)
    >>> sumar(5,4)
    9
    (suma incorrecta)
    >>> sumar(1,3)
    7

    """
    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)
#ir al cmd y dirigirse al directorio donde está este metodo. ejecutarlo por consola y ver el resultado (debiese dar 6)

#Para ejecutar prueba de comentario en la consola del cmd...
import doctest
doctest.testmod()