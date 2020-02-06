#Series
#Para importar libreria de panda: pip install pandas, luego reiniciar el vscode

import pandas as pd

#Metodo serie de libreria pandas
serie1 = pd.Series([3,5,7])
print(serie1)

asignaturas = ["matematicas","historia","fisica","literatura"]
notas = [8,6,9,7]
series_notas_daniel =pd.Series(notas,index=asignaturas)
print(series_notas_daniel)

print(series_notas_daniel['fisica'])

print(series_notas_daniel[series_notas_daniel >= 8])

series_notas_daniel.name = 'Notas de Daniel'
print(series_notas_daniel)

series_notas_daniel.index.name = 'Asignaturas de Daniel'
print(series_notas_daniel)

diccionario = series_notas_daniel.to_dict()
print(diccionario)

serie = pd.Series(diccionario)
print(serie)

asignaturas = ["matematicas","historia","fisica","literatura"]
notas_ana = [4,5,2,6]
series_notas_ana =pd.Series(notas_ana,index=asignaturas)
series_notas_ana.name = 'Asignaturas de Ana'
series_notas_ana.index.name = 'Notas de Ana'
print(series_notas_ana)

serie_notas_clase = (series_notas_daniel + series_notas_ana) /2
print(serie_notas_clase) 
