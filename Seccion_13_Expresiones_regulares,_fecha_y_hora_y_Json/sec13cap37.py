#Expresiones regulares, (Search, findall,split,sub)

texto = "hola, mi nombre es antonio"

import re #regular expression

print(re.search("nombre", texto)) #verifica si encuentra la expresion en el texto
print(re.search("adios", texto)) #verifica que no encuentra la expresion en el texto

#Para validar si la busqueda de la expresion existe o no
resultado = re.search("nombre", texto)
if(resultado):
	print("cadena encontrada")
else:
	print("cadena no encontrada")
print(re.search("antonio$", texto)) #Busca en la cadena texto si hay alguna frase que acanbe en la palabra con el $

print(re.search("^hola",texto)) #Busca en la cadena texto si hay alguna frase que comience en la palabra con el ^

print(re.search("mi.*es",texto)) #Busca para hacer coincidencia en el texto con las palabras relacionadas con el .*

#Findall

texto = """
El coche de luis es rojo,
el coche de antonio es blanco,
y el coche de maria es rojo		
"""

print(re.findall("coche.*rojo",texto))

#Split 

texto = "La silla es blanca y vale 80"

print(re.split("\s",texto)) #\s espacio en blanco, para cortar el texto, dividirá el texto y el caracter de corte es un espacio en blanco

#sub / modifica

texto = "La silla es blanca y vale 80"

print (re.sub("blanca","roja", texto)) #la primera palabra se modifica en base a la palabra que buscas en el texto

