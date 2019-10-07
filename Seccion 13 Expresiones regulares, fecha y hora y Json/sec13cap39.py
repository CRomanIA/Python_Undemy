#Fecha y hora 
from datetime import datetime

fechayhora = datetime.now()

print(fechayhora)

#fecha

año = fechayhora.year
mes = fechayhora.month
dia = fechayhora.day

#hora

hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

print("la hora es {}:{}:{}".format(hora,minutos,segundos))