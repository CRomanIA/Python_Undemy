#Mapas de calor (heatmap)
#Es una representacion grafica de datos, en donde los valores tomados de la matriz, se reprensentan en colores

#%%
import pandas as pd
import numpy as np
import seaborn as sns

#%%
vuelos = sns.load_dataset('flights')
vuelos.head()

# %%
vuelos = vuelos.pivot('month','year','passengers')

#para hacer mapa de calor
#%%
sns.heatmap(vuelos)
#el mismo mapa de calor, pero con los valores
#%%
sns.heatmap(vuelos, annot=True, fmt='d')
#Para tomar un valor sacado del mapa de calor, para tomarlo como valor central
#%%
vuelos.loc['May'][1956]
#Ahora asignar el valor central para que de ahí, la taabla tome la gama de colores.
valor_central = vuelos.loc['May'][1956]
valor_central
#Creacion de la tabla con el valor central para la gama de colores
#%%
sns.heatmap(vuelos, center=valor_central, annot=True, fmt='d')
#Para que el valor de la tabla se represente de manera horizontal
#%%
sns.heatmap(vuelos, center=valor_central, annot=True, fmt='d', cbar_kws={'orientation':'horizontal'})
