#Pip : es un gestor de paquetes (Librerias) y modulos para python, un modulo es una libreria de python que puedes incluir en el proyecto
import camelcase

camel = camelcase.CamelCase()
texto = "el luigi Se la come doblada"
print (camel.hump(texto))