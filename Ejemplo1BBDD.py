import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN', 15, 'DEPORTES')")
#variosProductos=[

#		("camiseta", 10, "DEPORTES"),
#		("jabón", 1, "DROGUERIA"),
#		("camión", 20, "JUGUETES")

#]

#iCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)

#PARA RECUPERAR LA INFORMACIÓN DE LA BASE DE DATOS:
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()
#print(variosProductos)
for producto in variosProductos:

	#print(producto)
	#print(producto[0])
	print("Nombre Artículo:  ",producto[0], "Sección: ", producto[2])

miConexion.commit() # este método es para confirmar los cambios de los valores introducidos arriba en la base de dato creada.


miConexion.close()

