def sec2cap2():
	print ("Hola mundo")
	print ("y Adios")
#sec2cap2() #Fin

#sec2cap3 y sec2cap4
#Despues el entorno donde trabaja es Jupyter,
#no obstante se ouede trabajar por SublimeText
#de igual forma.

#sec3cap5 Variables
def sec3cap5():
	#Variable Numerica 
	numero = 5
	print(numero)
	#Variable de Texto (Cadena o String)
	cadena = "Hola mundijirijillo"
	print (cadena)
	
	#5perro = 5 #Eso tiraria error, no debe comenzar 
	#con numero una declaracion de variable.
	
	#Variables distintas Mayus/Minus
	numero5 = 5
	Numero5 = 99
	print (numero5)
	print (Numero5)
	#Concatenación de string
	cadena1 = "Cabros "
	cadena2 = "Chicos"
	cadenaUnida = cadena1 + cadena2
	print (cadenaUnida)
	#Suma
	numero1 = 5
	numero2 = 4
	suma = numero1 + numero2
	print (suma)
	#Ver Tipos de Variables [int]
	print (type(numero1))
	#Ver Tipos de Variables [string]
	print (type(cadena1))
#sec3cap5() #Fin

#sec3cap6 Numero
def sec3cap6():
	#Tipo int
	numero1 = 5
	print (numero1)
	#Tipo float
	decimal = 3.7
	print (decimal)
	#Sumar Variables
	numero1 = 5
	numero2 = 3
	suma = numero1 + numero2
	print (suma)
	numero1 = 5
	numero2 = 2.3
	sumaDecimal = numero1 + numero2
	print (sumaDecimal)
#sec3cap6() #Fin	

#sec3cap7 Conversiones entre distintos tipos de datos
def sec3cap7():
	#Conversión de dato entero a string
	numero = 5
	cadena = str(numero)
	print (cadena)
	#Conversion de datos de string a entero y suma de ellos.
	cadena = "25"
	numero = int(cadena)
	print(numero)
	numero2 = 4
	suma = numero + numero2
	print(suma)
	#Conversion de datos de string a float y suma de ellos.
	cadena = "25.7"
	decimal = float(cadena)
	print(decimal)
	decimal2 = 11.7
	sumaDecimal = decimal + decimal2
	print (sumaDecimal)
#sec3cap7() #Fin

#sec4cap8 Cadena de Texto
def sec4cap8():
	cadena = "Hola mundo"
	print (cadena)
	print (cadena[4])
	#H o l a   M u n d o
	#0 1 2 3 4 5 6 7 8 9
	print (cadena[0])
	print (cadena[1])
	#Union de parametros de la oración
	print (cadena[2:7])
	print (cadena[7])
	print (cadena[8])
	print (cadena[9])
	print (cadena[4])
	#Tomando un valor hasta el final o viceversa
	print (cadena[0:2])
	print (cadena[2:])
	print (cadena[4])
	#o viceversa
	print (cadena[:9])
	#Tomar el ultimo valor con -1
	print (cadena[-1])
	#Easter Egg
	print (cadena[4])
	print (cadena[5])
	print (cadena[3])
	print (cadena[5])
	print (cadena[3])
	print (cadena[2])
	print (cadena[9])
	print (cadena[4])
	#Se pueden consultar como en los ejemplos, pero no modificar como:
	#print (cadena[9] = 5) #emite error
	#Union de cadenas
	cadena1 = "Hola"
	cadena2 = " "
	cadena3 = "Mundo"
	sumaCadena = cadena3 + cadena2 + cadena1
	print (sumaCadena)
#sec4cap8() #Fin

#sec4cap9 Funciones de Cadena
def sec4cap9():
	cadena = "Hola mundo"
	print (cadena)
	#Ver longitud (cuantos caracteres tiene la cadena)
	print (len(cadena))
	#Imprime en mayuscula, solo imprime. ojo!
	print (cadena.upper())
	#Para que la cadena se encuentre en mayuscula:
	cadena = cadena.upper()
	print (cadena)
	#Muestra cadena en minuscula
	print (cadena.lower())
	#Dividir cadena por palabras
	print (cadena.split())
	#Crear cadena con muchas palabras u dividirlas
	cadena2 = "manzana,pera,uva,guinda,tomame"
	print (cadena2.split(","))
#sec4cap9() #Fin 

#sec4cap10 imprimir variables en una cadena
def sec4cap10():
	#imprimir texto concatenado con variable cadena
	nombre = "Antonio"
	print("Buenos días " + nombre)
	# .format
	nombre = "Antonio"
	edad = 18
	print("Buenos días {}, feliz {} cumpleaños".format(nombre, edad))
	#Otro ejemplo
	resultado = 10/3
	print(resultado)
	print("El resultado es {r}".format(r=resultado))
	#Reduciendo valores
	print("El resultado es {r:1.3f}".format(r=resultado))
	#f-string
	nombre = "Antonio"
	edad = 18
	print(f"Buenos dias {nombre}, feliz {edad} cumpleaños")
#sec4cap10()

#sec4cap11 Entrada por teclado
def sec4cap11():
	#funcion input
	print("Introduce un nombre")
	entrada = input()
	print("Hola ", entrada)
#sec4cap11()
##Para Revisarlo, debemos trabajar con la consola de windows (CMD)
#sec5cap12 Operadores aritmeticos (+,-,*,/,%,**,//)
def sec5cap12():
	#Suma de dos numeros
	numero1 = 10
	numero2 = 5
	suma = numero1 + numero2
	print (suma)
	#Resta
	numero1 = 10
	numero2 = 5
	resta = numero1 - numero2
	print (resta)
	#Multiplicacion
	numero1 = 10
	numero2 = 5
	multiplicacion = numero1 * numero2
	print (multiplicacion)
	#Division
	numero1 = 10
	numero2 = 5
	division = numero1 / numero2
	print (division)
	#Operador de resto de una división
	numero1 = 5
	numero2 = 2
	resto = numero1 % numero2
	print(resto)
	#Valor del Cuociente
	numero1 = 5
	numero2 = 2
	cociente = numero1 // numero2
	print(cociente)
	#Exponente
	exponente = 2 ** 3
	print(exponente)
#sec5cap12() #Fin

#sec5cap13() Operadores de asignacion (=,+=,-=,*=,/=,**=)
def sec5cap13():
	#Operador =
	numero = 5
	print (numero)
	numero = numero + 4
	print (numero)
	#Operador +=
	numero = 5
	print(numero)
	numero +=4	
	print(numero)
	#Operador -=
	numero =numero - 3
	print(numero)
	numero -=3
	print(numero)
	#Operador *=
	numero = numero * 4
	print(numero) 
	numero *=4
	print(numero)
	#Operador /=
	numero /= 4
	print(numero)
	#Operador **=
	numero = 2
	numero = numero ** 3
	print(numero)
	numero = 2
	numero **= 3
	print(numero)
#sec5cap13() #Fin

#sec5cap14 Operadores de comparación (==,!=,>,<,>=,<=)
def sec5cap14():
	# == igualdad
	numero1 = 5
	numero2 = 3
	igualdad = numero1 == numero2
	print(igualdad)
	cadena1 = "Hola"
	cadena2 = "Hola"
	igualdad = cadena1 == cadena2
	print(igualdad)
	cadena1 = "Hola"
	if (cadena1 == "Hola"):
		print("Dijo Hola")
	#!= distinto
	numero1 = 3
	numero2 = 5
	distinto = numero1 != numero2
	print(distinto)
	#> mayor
	numero1 = 3
	numero2 = 5
	mayor = numero1 > numero2
	print(mayor)
	#< menor
	numero1 = 3
	numero2 = 5
	menor = numero1 < numero2
	print(menor)
	#>= mayorigual
	numero1 = 3
	numero2 = 5
	mayigu = numero1 >= numero2
	print(mayigu)
	#<= menorigual
	numero1 = 5
	numero2 = 5
	menigu = numero1 <= numero2
	print(menigu)
#sec5cap14() #Fin

#sec5cap15 Operadores Logicos (and, or, not)
def sec5cap15():
	numero1 = 10
	numero2 = 5
	numero3 = 7
	numero4 = 8
	#Operador and
	cond = numero1 > numero2
	print(cond)
	cond2 = numero3 < numero4
	print(cond2)
	cond3 = (numero1 > numero2) and (numero3 < numero4)
	print (cond3)
	cond4 = numero3 > numero4
	print(cond4)
	cond5 = (numero1 > numero2) and (numero3 > numero4)
	print (cond5)
	#Operador or con que alguna de las dos condiciones sea cierta, el or lo tomará como verdadero
	cond6 = (numero1 > numero2) or (numero3 > numero4)
	print (cond6)
	
	numero1 = 10
	numero2 = 5
	numero3 = 7
	numero4 = 8
	cond7 = numero3 > numero4
	print(cond7)
	#Operador not
	not(cond7)
	print(not())
#sec5cap15() #Fin

#sec5cap16 Operadores de identidad (is, is not)
def sec5cap16():
	frutas1 = ["Manzana", "Pera"]
	frutas3 = frutas1
	# condicion is
	cond1 = frutas3 is frutas1
	print (cond1)
	# Si le agregamos a frutas 3, una fruta más
	frutas3.append("Naranja")
	print (frutas3)
	# La fruta 1, donde obtiene los datos 
	#tambien se modifica com la nueva información
	print (frutas1)
	#condicion is not
	cond2 = frutas3 is not frutas1
	print (cond2)
#sec5cap16() #Fin

#sec5cap17 Operador de pertenencia (is, not in)
def sec5cap17():
	#Operador is
	frutas1 = ["Manzana", "Pera", "Naranja"]
	frutas2 = "Pera"
	print (frutas2 in frutas1) 
	#Operador not in
	frutas3 = "Melocoton"
	print (frutas3 not in frutas1)
#sec5cap17()

#sec6cap18 Colecciones de datos: Listas
def sec6cap18():
	#Listas
	colores =["rojo","amarillo","verde"]
	print (colores)
	print (colores[0])
	print (colores[1])
	colores[1] = "azul"
	print (colores[1])
	print (colores[2])
	colores.append("naranja")
	print (colores[3])
	colores.remove("rojo")
	print (colores)

	for color in colores:
		print(color)

	colores.clear()
	print(colores)
#sec6cap18() #Fin

#sec6cap19 Tuplas: es una coleccion de elementos ordenada pero que no se puede modificar
def sec6cap19():
	tupla_colores = ("rojo","verde","amarillo")
	print (tupla_colores)
	for color in tupla_colores:
		print (color)
	print(tupla_colores[2])
	print(len(tupla_colores))	
#sec6cap19()

#sec6cap20 conjuntos
def sec6cap20():
	conjunto_colores = {"rojo", "verde", "azul"}
	print(conjunto_colores)
	for color in conjunto_colores:
		print(color)
	#print(conjunto_colores[0]) no se puede hacer esto
	#Para ver longitud del conjunto
	print(len(conjunto_colores))
	#Para agregar al conjunto 
	conjunto_colores.add("negro")
	print(conjunto_colores)
	#Para remover del conjunto
	conjunto_colores.remove("verde")
	print(conjunto_colores)
#sec6cap20()

#sec6cap21 Diccionarios es una coleccion de elementos, que estan indexados, no estan ordenador y se pueden modificar
def sec6cap21():
	diccionario_colores = {"red":"rojo","blue":"azul","yellow":"amarillo"}
	print(diccionario_colores)
	#Para imprimir solo un elemento del diccionario	 
	print(diccionario_colores["red"])
	#Se pueden agregar variables en los elementos del diccionario
	valor = diccionario_colores["yellow"]
	print (valor)
	#Para agregar un elemento al diccionario
	diccionario_colores["black"] = "negro"
	print(diccionario_colores)
	#Para eliminar un elemento del diccionario
	diccionario_colores.pop("yellow")
	print(diccionario_colores)
	#Otra forma de borrar el elemento
	del(diccionario_colores["black"])
	print(diccionario_colores)
	#Desplegar informacion con for
	for color in diccionario_colores:
		print(color)
	#Para mostrar la clave como el valor:
	for clave,valor in diccionario_colores.items():
		print(clave,valor)	
#sec6cap21()

#ec7cap22 Condiciones if... else
def sec7cap22():
	a = 8
	b = 4
	print(a > b)
	print(a < b)
	if (a > b):
		print ("a es mayor que b")
	if (a < b): #No mostrará porque la expresión es falta, solo muestra cuando es true
		print ("a es menor que b")
	a = 8
	b = 4
	c = 2
	d = 6
	if (a > c) and (b < d):
		 print ("la primera expresión es correcta")
	if (a > c) and (b > d): #no se despliega. Si la expresión en algun punto te otorga false (en este caso (true)and(false))
		 print ("la primera expresión es correcta")
	if (a > c) and (b > d):
		 print ("la primera expresión es correcta")
	else:
		print("La segunda expresión es incorrecta, arregle: if (true)and(false)")
	a = 8
	b = 4
	if(a > b):
		print("a es mayor que b")
	elif(a == b):
		print("a es igual a b")
	else:
		print("Ninguna expresión anterior es correcta")
	a = 8
	b = 10	
	if(a > b):
		print("a es mayor que b")
	elif(a == b):
		print("a es igual a b")
	else:
		print("Ninguna expresión anterior es correcta")	
#sec7cap22()

#sec7cap23 bucle for
def sec7cap23():
	espacio = " "
	colores = ["rojo","verde","azul"]
	for color in colores:
		print(color)
	print(espacio)
	cadena = "hola mundo"
	for caracter in cadena:
		print(caracter)
	print(espacio)
	print(range (8))
	print(espacio)
	for numero in range(8):
		print(numero)
	print(espacio)
	for numero in range(3,8):
		print(numero)
	print(espacio)
	for numero in range(3,8,2):
		print(numero)
	print(espacio)	
	#break, para detener el bucle
	for numero in range(10):
		if (numero == 5):
			break
		print(numero)
	print(espacio)
	#Continue - para parar solo la iteracion actual
	for numero in range(10):
		if(numero == 6):
			continue
		print(numero)
	print(espacio)
	#for doble
	for numero1 in range(4):
		for numero2	in range(3):
				print(numero1, numero2)
	print(espacio)
#sec7cap23()

#sec7cap24() while
def sec7cap24():
	#Only while
	valor = 1
	fin = 10
	espacio = " "
	while(valor < fin):
		print(valor)
		valor = valor +1
	#While con if/break
	valor = 1
	print(espacio)
	fin = 10
	while (valor < fin):
		print(valor)
		valor = valor + 1
		if (valor == 5):
			break
	print(espacio)
	#while con if/continue
	valor = 1
	fin = 10
	while (valor < fin):
		valor = valor +1 
		if (valor == 6):
			continue
		print (valor)
	print(espacio)	
#sec7cap24()

#sec8cap25 Clases y objetos POO
def sec8cap25():
	class ClaseSilla:
		color = "blanco"
		precio = 100
	objetoSilla1 = ClaseSilla()
	print (objetoSilla1.color)
	print (objetoSilla1.precio)
	objetoSilla2 = ClaseSilla()
	objetoSilla2.color = "verde"
	objetoSilla2.precio = 120
	print (objetoSilla2.color)
	print (objetoSilla2.precio)

	class Persona: 
		def __init__(self,nombre,edad):
			self.nombre = nombre
			self.edad = edad
		def saludar(self):
			print("Hola, me llamo {} y tengo {} años".format(self.nombre,self.edad))
	persona1 = Persona("Juan",37)
	print (persona1.edad)
	print (persona1.nombre)
	persona1.saludar()
#sec8cap25()

#sec8cap26 Funciones
def sec8cap26():
	def saludar():
		print("Buenos Dias")
		saludar()
	def saludar2(nombre):
		print("Buenos dias " + nombre)
		nombre = "Antonio"
		saludar2(nombre)
	def sumar(numero1,numero2):
		suma = numero1+numero2
		return suma
	numero1 = 5
	numero2 = 3
	resultado = sumar(numero1, numero2)
	print (resultado)

	#Paso de valor por referencia
	colores = ["rojo","verde","azul"]
	def incluir_color(colores,color):
		colores.append(color)
	color = "negro"
	incluir_color(colores,color)
	print (colores)
#sec8cap26()

#sec8cap27 lamda 
def sec8cap27():
	resultado = lambda numero : numero + 30
	print (resultado(10))
	resultado2 = lambda numero1, numero2 : numero1+numero2
	print (resultado2(5,8))	
#sec8cap27()

#sec9cap28 Modulos, El segmento modulos se hará en otra hoja de proyecto
def sec9cap28():

	print("Luigi gay")
sec9cap28()