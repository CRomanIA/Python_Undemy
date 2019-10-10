#Librerias Numpy TODO: Es importante esto
import numpy as np

#arrays con condicion cero(donde toma 4 valores)
print(np.zeros(4))

#arrays con condicion uno(donde toma 4 valores)
print(np.ones(4))

#arrays con condicion de rango [igual a range] (donde toma 5 valores, en orden secuencial desde el cero)
print(np.arange(5))

#arrays con condicion de rango [igual a range] (donde toma 10 valores, en orden secuencial desde el cero)
print(np.arange(10))

#arrays con condicion de rango [igual a range] (donde toma valores donde inicia en el 2, hasta el 20 de 3 en 3)
print(np.arange(2,20,3))

#Construir un array a traves de una lista
lista1 = [1,2,3,4]
array1 = np.array(lista1)

print(lista1)
print(array1)

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

lista_doble = lista1,  lista2
print(lista_doble)

array_doble = np.array(lista_doble)
print(array_doble)

#ver forma que tiene el array
print(array_doble.shape)
print(array_doble.dtype)

