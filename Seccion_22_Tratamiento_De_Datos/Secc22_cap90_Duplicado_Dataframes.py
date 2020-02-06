#Eliminar Duplicados en Dataframe
import pandas as pd

lista_valores = [[1,2], [1,2], [5,6], [5,8]]
lista_indices = list('mnop')
lista_columnas = ['valor1','valor2']

dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)

#Eliminar de la lista los valores duplicados
dataframe2 = dataframe.drop_duplicates()
print(dataframe2)

#Eliminar los duplicados de la misma columna
print(dataframe2.drop_duplicates('valor1'))
#Eliminar los duplicados de la misma columna, pero mantiene un valor en especifico
print(dataframe2.drop_duplicates(['valor1'], keep='last'))


