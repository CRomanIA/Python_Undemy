#Operaciones con arrays (+,-,*,/,**)
import numpy as np

array1 = np.array([1,2,3,4])

print (array1)

#Division
array2 = array1 / 2
print(array2)

#Sumando
array3 = array1 + 4
print(array3)

#Array de dos dimensiones
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = lista1,lista2
array_doble = np.array(lista_doble)
print(array_doble)

#suma de un arrays doble
array_doble2 = array_doble + 5

print(array_doble2)

print(array_doble.dtype)
print(array_doble.shape)

#Operaciones aritmeticas en un array doble
array_doble3 = array_doble2 + 5
print(array_doble3)

array_doble4 = array3 ** 2
print(array_doble4) 

array_doble5 = array_doble4 / 5
print(array_doble5)

array_doble = array_doble + 4
print (array_doble)

array_doble6 = array_doble * 2
print(array_doble6)


