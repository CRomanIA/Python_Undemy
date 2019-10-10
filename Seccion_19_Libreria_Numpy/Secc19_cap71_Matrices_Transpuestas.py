#Arrays o matrices transpuestas (cambiar ordenadamente las filas por las columnas)

import numpy as np

#se crea un array, arange(para dar rango de 0 a 14) reshape(fila,columna) para organizar
array = np.arange(15).reshape((3,5))
print(array)

print(array[1][1])

#TODO Transponer: cambiar las filas de las columnas
array_trans = array.T 
print(array_trans)