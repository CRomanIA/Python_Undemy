#Ficheros formato excel

import pandas as pd

fichero_excel = pd.ExcelFile('/GIT/excel.xlsx')
print(fichero_excel)
misDatosExcel = fichero_excel.parse('Hoja1')
print(misDatosExcel)

##TODO: No me salio correctamente tampoco...
