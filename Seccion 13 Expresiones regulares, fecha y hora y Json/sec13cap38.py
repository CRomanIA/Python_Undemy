#Json: es una forma de almacenar o intercambiar datos que estan en formato texto

#convertir datos de un diccionario en python a una estructura json

producto1 = {"nombre":"silla","color":"blanco","precio":80}

#utilizar lib/modulo json

import json

estructura_json = json.dumps(producto1)

print(estructura_json)

#no funca asi: como diccionario
#estructura_json["nombre"]

#si se puede sacar por posición (cadena de caracteres en formato json)
print(estructura_json[0])

#tambien se puede acceder como diccionario en python
print(producto1["nombre"])

#pero asi no funciona
#estructura_json["nombre"]

#Convertir una estructura Json (estructura_json) en un diccionario en python

producto2 = json.loads(estructura_json)

print(producto2)

print(producto2["precio"])
