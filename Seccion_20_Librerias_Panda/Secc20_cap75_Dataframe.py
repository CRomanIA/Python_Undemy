#DataFrame

import pandas as pd
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
webbrowser.open(website)

dataframe_nba = pd.read_clipboard()
print(dataframe_nba)

print(dataframe_nba['Campeón del Oeste'])

print(dataframe_nba.loc[5])

print(dataframe_nba.head(6))

print(dataframe_nba.tail(2))

lista_asignaturas = ['matematicas' , 'historias','fisica']
lista_notas = [8,7,9]
diccionario = {'Asignaturas' : lista_asignaturas, 'Notas':[8,7,9]}

dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)