#Eliminar elementos en series y dataframes
import pandas as pd
import numpy as np

np.arange(4)
serie = pd.Series(np.arange(4), index=['a','b','c','d'])
print(serie)
#Si queremos eliminar un elemento (c)
print(serie.drop('c'))

#reshape = que la lista de valores se divide en 3 filas y 3 columnas
print(np.arange(9).reshape(3,3))

lista_valores = np.arange(9).reshape(3,3)
lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

print(dataframe.drop('b'))
print(dataframe.drop('c2',axis=1))

dataframe = dataframe.drop('b')
print(dataframe)

dataframe = dataframe.drop('c2',axis=1)
print(dataframe)