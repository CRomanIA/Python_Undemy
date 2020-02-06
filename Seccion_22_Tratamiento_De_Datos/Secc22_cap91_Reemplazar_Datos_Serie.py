#Reemplazar datos en serie
import pandas as pd

serie = pd.Series([1,2,3,4,5], index=list('abcde'))
print(serie)
#Para reemplazar
print(serie.replace(1,6))
#Para dejar el reemplazo en la serie
serie = serie.replace(1,6)
print(serie)
#Para dejar el reemplazo en la serie, pero como diccionario
serie = serie.replace({2:8,3:9})
print(serie)