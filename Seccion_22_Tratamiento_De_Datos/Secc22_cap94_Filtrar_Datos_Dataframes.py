#Filtar datos en dataframes

import pandas as pd
import numpy as np

lista_valores = np.random.rand(10,3)
#print(lista_valores)
dataframe = pd.DataFrame(lista_valores)
print(dataframe)

#Filtrar columna 0 del dataframe
columna0 = dataframe[0]
print(columna0)

#Para filtrar con condicion
print(columna0[columna0 > 0.80])

print(dataframe[dataframe > 0.80])