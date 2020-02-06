#Regresion Lineal
#En estadisticas, el analisis de regresion es un proceso estadistico para estimar entre variables,
#es decir entender como varia el valor de una variable en funcion del valor de otras variables
#TODO: Utilizar este codigo en jupyter notebook (Navegador o descargar)

#%%
#Regresion Lineal
import pandas as pd
import numpy as np
import seaborn as sns

%matplotlib inline
#Cargar Datasets para hacer pruebas
propinas = sns.load_dataset('tips')
propinas.head()

#crear un grafico de regresion linear con seaborn
#lmplot(eje x, eje y, el dataset que cargaste)

#sns.lmplot(x="total_bill",y="tip", data=propinas)
sns.lmplot(x='total_bill',y='tip', data=propinas, scatter_kws={'marker':'o','color':'green'}, line_kws={'color':'blue'})

#Para Sacarle la linea
sns.lmplot('total_bill','tip',propinas,fit_reg=False)

#Para crear porcentaje en base a dos columnas
propinas['porcentaje'] = 100 * propinas['tip'] /propinas['total_bill']
propinas.head()
#Crear grafica de regresion linear con el porcentaje de propina
sns.lmplot('size', 'porcentaje', propinas)
#Grafica de regresion linear en donde muestra el porcentaje de la gente que dio la propina total, dependiendo del sexo
sns.lmplot('total_bill', 'porcentaje', propinas,hue='sex', markers=['x','o'])
#En vez de compara por sexo, comparar por dias de la semana
sns.lmplot('total_bill', 'porcentaje', propinas, hue='day')

# %%
