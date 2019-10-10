#Funciones avanzadas
##Funciones Generadoras - Genera valores sobre la marcha

#range
"""
def sec18cap65():
    range(0, 11)

    for numero in range(0, 11):
        print(numero)


    def pares(maximo):
        for numero in range(maximo):
            if(numero % 2 == 0):
                #yield : devuelve el numero (TODO:no se si solo numeros o cualquier valor)
                yield numero
    maximo = 11
    for numero in pares(maximo):
        print(numero)     
#sec18cap65()            

#Funcion Filter - 
def sec18cap66():
    def positivo(numero):
        if(numero > 0):
            return True
        else:
            return False
    print(positivo(5))
    print(positivo(-3))

    numeros = [4,-2,8,-3,-5,-7,1,9]
    filtro = filter(positivo, numeros)
    result = list(filtro)
    print(result)
#sec18cap66()   
"""

#Funcion Map
def multiplicar(numero):
    return numero * 2

print(multiplicar(2))

numeros = [2,4,6]

mapping = map(multiplicar, numeros)
print(mapping)

resultado = list(mapping)

print(resultado)
#TODO: Todo eso, en una línea de codigo xd
lista_resultado = list(map(multiplicar, numeros))
print(lista_resultado)
#Utilizando funcion lamba: donde asigna una variable vacía y le da como contenido ella misma X4

lista_resultado2 = list(map(lambda numero: numero * 4, numeros))

print(lista_resultado2)