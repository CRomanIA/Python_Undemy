#Indexación con arrays
import numpy as np

array = np.arange(0,11)
print(array)
#Si se quiere hacer un conjunto de arrays
print(array[0:3])
print(array[2:5])
print(array[:])
print(array[0:1])

array_copia = array.copy()

print(array_copia)

array_copia[0:3] = 20

print(array_copia)
print(array)

#crear array con varias dimensiones 
array2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2)

#Tomar la primera fila
print(array2[0])
#Tomar la segunda fila
print(array2[1])
#Tomar la tercera fila
print(array2[2])

#Para tomar un valor de alguna fila ya reconocida[mismo patron, del 0 se inicia]
print(array2[1][0])