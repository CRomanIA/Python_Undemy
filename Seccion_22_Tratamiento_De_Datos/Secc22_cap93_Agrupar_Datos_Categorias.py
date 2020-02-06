#Agrupar datos en categoria

import pandas as pd
import numpy as np

precios = [42,55,48,23,5,21,88,34,26]
rango = [10,20,30,40,50,60,70,80,90,100]
rango_precios = pd.cut(precios, rango)
print(rango_precios)

#Para contar los valores del rango de precios
print(pd.value_counts(rango_precios))