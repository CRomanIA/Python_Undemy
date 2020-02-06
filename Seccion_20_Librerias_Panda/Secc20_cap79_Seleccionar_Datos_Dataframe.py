#Seleccionar entradas para dataframe

import pandas as pd
import numpy as np

lista_valores = np.arange(25).reshape(5,5)
#print(lista_valores)
lista_indices = ['i1','i2','i3','i4','i5']
lista_columnas = ['c1','c2','c3','c4','c5']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

print(dataframe['c2'])
print(dataframe['c2']['i2'])

print(dataframe[['c3','c4']])

print(dataframe[['c2','c3','c4']])

print(dataframe[dataframe['c2'] > 15])

print(dataframe > 20)

print(dataframe.loc['i3'])

print(dataframe.loc['i3']['c4'])
