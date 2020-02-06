#Seleccionar datos en las series

import pandas as pd
import numpy as np

lista_valores =np.arange(3)
lista_indices = ['i1','i2','i3']

serie = pd.Series(lista_valores, index=lista_indices)
print(serie)

serie = serie * 2
print(serie)

print(serie['i2'])
print(serie[2])
print(serie[0:2])
print(serie['i1':'i3'])

print(serie[serie > 3])
serie[serie > 3] = 6
print(serie) 




