#Histograma
#TODO: Recomendaciones: para trabajar a partir de aca, utilizar 100% jupyter, sino, complementar el vscode con jupyter y a la vez, integrarle la extension de neuron para la lectura de graficos, sino se hace mucho mas dificil trabajar.

#un histograma es una representacion grafica de una varible o de datos en forma de barra, donde la superficie de cada barra es proporcional a la frecuencia de los valores representados

#Librerias
import pandas as pd
import numpy as np
#librerias de representacion grafica
import matplotlib as mpl
#Con matplotlib, utilizar pyplot... npl.pyplot (para sus funciones generales)
import seaborn as sns

#Para ver los graficos en las pruebas
datos1 = np.random.randn(100)
#print(datos1)

#histograma de los datos
#mpl.pyplot.hist(datos1)

#otro color... con alpha, le das atenuacion al color
#mpl.pyplot.hist(datos1, color='grey', alpha=0.5)


#Un histograma diferente, ademas que te muestra curvartura de ascenso en los valores (no utilizar juntos)
#sns.distplot(datos1)

#otro color...
#sns.distplot(datos1, color='green')

#Mezclar Histogramas con Matplotlib
datos2 = np.random.randn(80)
#mpl.pyplot.hist(datos2, color='yellow', alpha=0.4)

#TODO: bins= cantidad de barras que quieras agregar
#TODO: density = para que sea confort para las dos 
#mpl.pyplot.hist(datos1, color='green', alpha=0.3, bins=20, density=True)
#mpl.pyplot.hist(datos2, color='blue', alpha=0.3, bins=20, density=True)

#lo mismo con seaborn

datos3 = np.random.randn(1000)
datos4 = np.random.randn(1000)

#sns.jointplot(datos3,datos4)

sns.jointplot(datos3, datos4, kind='hex')