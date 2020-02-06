#Union de Dataframes

import pandas as pd

dataframe1 = pd.DataFrame({'c1' :['1','2','3'], 'clave' :['a','b','c']})
print(dataframe1)

dataframe2 = pd.DataFrame({'c2':['4','5','6'], 'clave':['c','b','e']})
print(dataframe2)

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2)
print(dataframe3)

#Para uni por una determinada columna

dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2, on='clave')
print(dataframe3)

#Que prevalezcan los datos que quedan ocultos por la union TODO: how='left' how='right' how='outer'
dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2, on='clave', how='left')
print(dataframe4)