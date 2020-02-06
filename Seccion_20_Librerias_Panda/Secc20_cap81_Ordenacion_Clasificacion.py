#Ordenacion y clasificacion
import pandas as pd
import numpy as np

range(4)

lista_valores = range(4)
lista_indices = list('CABD')

serie = pd.Series(lista_valores, index=lista_indices)
print(serie)

print(serie.sort_index())

print(serie.sort_values())

print(serie.rank())

serie2 = pd.Series(np.random.randn(10))
print(serie2)

print(serie2.rank())
print(serie2.sort_values())
print(serie2.sort_index())
