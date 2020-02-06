#Valores nulos - NaN

import pandas as pd
import numpy as np

lista_valores = ['1','2',np.nan,'4']
print(lista_valores)

serie = pd.Series(lista_valores, index=list('abdc'))

print(serie.isnull())

print(serie.dropna())

serie = serie.dropna()
print(serie)

lista_valores2 = [ [1,2,3], [4,np.nan,5], [6,7,np.nan]]
#print(lista_valores2)
lista_indices = list('123')
#print(lista_indices)
lista_columas = list('abc')

dataframe = pd.DataFrame(lista_valores2, index=lista_indices, columns=lista_columas)
print(dataframe)
print(dataframe.isnull())

print(dataframe.dropna())

print(dataframe.fillna(0))
