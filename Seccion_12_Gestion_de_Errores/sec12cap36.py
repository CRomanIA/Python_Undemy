#Gestion de Errores try... except... else... finally

#Division con error
#numero1 = 5
#numero2 = 0
#division = numero1 / numero2

#Division del error camuflado
try:
	numero1 = 5
	numero2 = 0
	division = numero1 / numero2
	print(division)
except:
	print("Ha habido un error")

#excepcion con error declarado: ZeroDivisionError
try:
	numero1 = 5
	numero2 = 0
	division = numero1 / numero2
	print(division)
except ZeroDivisionError:
	print("Error, division entre ceros")
except:
	print("Ha habido un error")

#Excepcion con else
try:
	numero1 = 5
	numero2 = 2
	division = numero1 / numero2
	print(division)
except ZeroDivisionError:
	print("Error, division entre ceros")
except:
	print("Ha habido un error")
else:
	print("La division funcionó correctamente")

#Excepcion con Finally
try:
	numero1 = 5
	numero2 = 2
	division = numero1 / numero2
	print(division)
except ZeroDivisionError:
	print("Error, division entre ceros")
except:
	print("Ha habido un error")
else:
	print("La division funcionó correctamente")
finally:
	print("Esta prueba de try se a acabado")
