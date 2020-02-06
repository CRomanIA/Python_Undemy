#Concatenacion de Arrays, Series y Dataframes
import pandas as pd
import numpy as np

array1 = np.arange(9).reshape(3,3)
#print(array1)

print(np.concatenate([array1,array1]))

#Para concatenar hacia la derecha
print(np.concatenate([array1,array1],axis=1))

#Como concatenar una serie
serie1 = pd.Series([1,2,3], index=['a','b','c'])
serie2 = pd.Series([1,2,3], index=['d','e','f'])
print(serie1)
print(serie2)

print(pd.concat([serie1,serie2]))

#Para que en la concatenacion, te muestre el valor de cada serie
print(pd.concat([serie1,serie2], keys=['serie1','serie2']))

#Para concatenar dataframes
dataframe1 = pd.DataFrame(np.random.rand(3,3), columns=['a','b','c'])
print(dataframe1)

dataframe2 = pd.DataFrame(np.random.rand(2,3), columns=['a','b','c'])
print(dataframe2)

print(pd.concat([dataframe1,dataframe2]))

#Para enmumerar correctamente el index, que por la concatenacion se encuentra con los valores de las dos tablas
print(pd.concat([dataframe1,dataframe2], ignore_index=True))



