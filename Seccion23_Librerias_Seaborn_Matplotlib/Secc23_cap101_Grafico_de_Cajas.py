#Diagrama de Cajas 
#Sirve para representar graficamente una serie de datos númericos a traves de sus cuartiles

#%%
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns

# %%
datos = np.random.randn(100)
datos

# %%
sns.boxplot(datos)

# %%
