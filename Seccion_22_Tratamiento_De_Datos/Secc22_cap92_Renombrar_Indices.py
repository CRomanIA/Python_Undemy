#Renombrar Indices

import pandas as pd
import numpy as np

lista_valores = np.arange(9).reshape(3,3)
lista_indices = list('abc')
dataframe = pd.DataFrame(lista_valores, index=lista_indices)
#print(dataframe)
#Cambiar los indices para cambiar las letras de min a MAY
nuevos_indices = dataframe.index.map(str.upper)
dataframe.index = nuevos_indices
#print(dataframe)

#Metodo rename
dataframe = dataframe.rename(index=str.lower)
#print(dataframe)

#Cambiar el nombre por otro
nuevos_indices = {'a':'f','b':'g','c':'h'}
#print(dataframe.rename(index=nuevos_indices))

dataframe = dataframe.rename(index=nuevos_indices)
print(dataframe)

#Otra manera de cambiarlo
nuevos_indices = {'f':'j'}
dataframe.rename(index=nuevos_indices, inplace=True)
print(dataframe)