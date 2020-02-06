#Jerarquia Indices

import pandas as pd
import numpy as np

lista_valores = np.random.rand(6)
#print(lista_valores)

lista_indices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]

series = pd.Series(lista_valores, index=lista_indices)
print(series)

print(series[1])
print(series[1]['b'])

dataframe = series.unstack()
print(dataframe)

lista_valores2 = np.arange(16).reshape(4,4)
#print(lista_valores2)

lista_indices = list('1234')
#print(lista_indices)

lista_columnas = list('abcd')
#print(lista_columnas)

dataframe2 = pd.DataFrame(lista_valores2, index=lista_indices, columns=lista_columnas)
print(dataframe2)

serie2 = dataframe2.stack
print(serie2)