#SQLite - Sistema de gestión de base de datos relacionales 

import sqlite3
datadir = './Seccion 14 Base de Datos'
datafile = 'basededatos1.db'
db = datadir+ ' ' +datafile

conn = sqlite3.connect(db)
cursor = conn.cursor()

#Sec14cap41 Crear Tabla en Base de datos
def sec14cap41():
#Te conectas primero con la sintaxis del capitulo anterior(la de arriba)
	cursor = conn.cursor()
	cursor.execute("CREATE TABLE PERSONAS (nombre TEXT,apellido1 TEXT, apellido2 TEXT, edad INTERGER)")
	conn.commit() #Esa sentencia que hemos creado a funcionado y queremos que funcione siempre
	conn.close()
sec14cap41()

#Sec14cap42 Insertar Fila 
def sec14cap42():
#Te conectas primero con la sintaxis del capitulo1 (la sentencia primera)
	cursor = conn.cursor()
	cursor.execute("INSERT INTO PERSONAS VALUES ('Christian','Roman','Pulento','23')")
	conn.commit()
	conn.close()
#sec14cap42()

#Sec14cap43 Insertar Varias Filas a la vez
def sec14cap43():
	cursor = conn.cursor()
	#Crearemos lista de personas que queramos añadir a la tabla
	lista_persona = [('Luis','Pino','Gay','33'), ('Francisca','Roman','Meona','21')]
	cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_persona)
	conn.commit()
	conn.close()
#sec14cap43()

# sec14cap44() Consultar Datos
def sec14cap44():
	cursor.execute("SELECT * FROM PERSONAS")
	personas = cursor.fetchall() #fetchall: Recoge todo los resultados de la tabla
	for persona in personas:
		print (persona)
	conn.close()
#sec14cap44()

#sec14cap45() Consulta Datos con Where
def sec14cap45():
	cursor.execute("SELECT * FROM PERSONAS WHERE edad > 30")
	personas = cursor.fetchall()
	for persona in personas:
		print (persona)
	conn.close()
#sec14cap45()

#sec14cap46 Ordenar Datos
def sec14cap46():
	cursor.execute("SELECT * FROM PERSONAS ORDER BY edad")
	personas = cursor.fetchall()
	for persona in personas:
		print (persona)
	conn.close()
#sec14cap46()

#sec14cap47 Eliminar Datos
def sec14cap47():
	cursor.execute("DELETE FROM PERSONAS WHERE nombre = 'Francisca'")
	conn.commit()
	conn.close()
#sec14cap47()

#sec14cap48 Actualizar Datos
def sec14cap48():
	cursor.execute("UPDATE PERSONAS SET edad = 40 WHERE nombre = 'Christian'")

	conn.commit()
	conn.close()	
#sec14cap48()



