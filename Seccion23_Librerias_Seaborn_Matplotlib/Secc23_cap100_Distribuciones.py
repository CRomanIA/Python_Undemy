#Combinando Estilos
#%%
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

datos = np.random.randn(100)
datos


# %%
sns.distplot(datos, color='green')

# %%
#Para eliminar los rectangulo de valores
sns.distplot(datos,color='green', rug=False, hist=False)


# %%
argumentos_curva = {'color':'black','label':'curva'}
argumentos_histograma = {'color':'grey','label':'histograma'}

sns.distplot(datos, bins=25,kde_kws=argumentos_curva,hist_kws=argumentos_histograma)


# %%
serie = pd.Series(datos)
serie

# %%
sns.distplot(serie, bins=25, color='green')

# %%
