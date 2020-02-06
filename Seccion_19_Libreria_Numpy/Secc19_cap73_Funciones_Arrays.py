#Funciones en arrays

import numpy as np

array = np.arange(5)
print(array)
#Para sacar la raiz cuadrada de la raiz
print(np.sqrt(array))
#Crear arrays de forma aleatoria con random
print(np.random.rand(5))
print(np.random.rand(5))

#a partir de una lista, crear un array de la lista
lista = [5,6,7,8,9]
array2 = np.array(lista)
print(array2)

#para sumar arrays (en donde los valores de las celdas se sumen)
print("los valores de la suma son: ",np.add(array,array2))

#calcular el maximo valor de los dos arrays
print("los valores maximo son: ", np.maximum(array,array2))