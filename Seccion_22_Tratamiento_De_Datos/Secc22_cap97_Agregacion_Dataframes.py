#Agregacion de Dataframes (Operaciones que dan un valor, como la media)
import pandas as pd
import numpy as np

lista_valores = [[1,2,3], [4,5,6], [7,8,9], [np.nan, np.nan, np.nan]]
print(lista_valores)
lista_columnas = list('abc')
dataframe = pd.DataFrame(lista_valores, columns=lista_columnas)

print(dataframe)

#Agrupar para obtener un valor
print(dataframe.agg(['sum', 'min']))

#Para hacerlo con el otro eje (en vez de sumar las columnas, lo hace con las filas)
print(dataframe.agg('sum',axis=1))   

