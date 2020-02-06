#Estadisticas en dataframes

import pandas as pd
import numpy as np

array = np.array([[1,8,3],[5,6,7]])
print(array)

dataframe = pd.DataFrame(array, index=['a','b'], columns=list('123'))
print(dataframe)

print(dataframe.sum())
#Calculo por filas
print(dataframe.sum(axis=1))

print(dataframe.min())

print(dataframe.max())
#Calculo por filas
print(dataframe.max(axis=1))

print(dataframe.idxmin())

#Genera estadisticas
print(dataframe.describe())

