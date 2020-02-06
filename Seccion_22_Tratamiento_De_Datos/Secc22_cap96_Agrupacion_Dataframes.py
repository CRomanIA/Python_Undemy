#Agrupación de Dataframes
import pandas as pd
import numpy as np

lista_valores = {'clave1':['x','x','y','y','z'], 'clave2':['a','b','a','b','a'], 'datos1':np.random.rand(5), 'datos2':np.random.rand(5)}
print(lista_valores)

dataframe = pd.DataFrame(lista_valores)
print(dataframe)

#ordenar de la columna datos1 en funcion de lo que tengan con clave1
grupo1 = dataframe['datos1'].groupby(dataframe['clave1'])
#Toma la media de los valores agrupados para dar el resultado
print(grupo1.mean())
