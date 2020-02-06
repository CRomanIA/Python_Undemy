#Indices
import pandas as pd

lista_valores = [1,2,3]
lista_indices = ['a','b','c']
serie = pd.Series(lista_valores, index=lista_indices)

print(serie)

print(serie.index)
#El nombre del indice no soporta cambio
print(serie.index[0])

lista_valores2 = [[6,7,8],[8,9,5],[6,9,7]]
lista_indices2 = ['matematicas','historia','fisica']
lista_nombres = ['Antonio','Maria','Pedro']

dataframe = pd.DataFrame(lista_valores2,index=lista_indices2, columns=lista_nombres)

print(dataframe)

print(dataframe.index[0])
print(dataframe.index[1])