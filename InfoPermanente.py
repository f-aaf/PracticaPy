import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona con el nombre: ", self.nombre)

	def __str__(self): # método para convertir en cadena de texto
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:

	personas=[]

	def __init__(self):

		ListaDePersonas=open("ficheroExterno","ab+") # ab+ es que lo podemos abrir para ver información binaria
		ListaDePersonas.seek(0) # con el método seek lo que hacemos que leea toda la lista antes de desplazarse hacia abajo def agregarPersonas

		try:
			self.personas=pickle.load(ListaDePersonas) # con esta instrucción cargamos o almacenamos la lista de personas para poder leerla
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)) ) # método len para saber cuantas personas hay en esa lista

		except:
			print("El fichero está vacío")

		finally:
			ListaDePersonas.close()
			del(ListaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)  # con el método append, las personas creadas en p se agregaran a la lista personas =[]
		self.guardarPersonasEnFicheroExterno() # llamar a este método desde el fichero externo

	def mostrarPersonas(self):
		for p in self.personas: # creamos un bucle for para ir recorriendo esa lista de personas
		   print(p)

	def guardarPersonasEnFicheroExterno(self):
		ListaDePersonas=open("ficheroExterno","wb") # wb para que lo abra de esa forma write bite. 
		pickle.dump(self.personas, ListaDePersonas) # dump es para que vuelque la información de nuestra lista de personas. 
		ListaDePersonas.close()
		del(ListaDePersonas)

	def mostrarInfoFicheroExterno(self):

		print("La información del fichero externo es la siguiente: ")
		for p in self.personas:
			print(p)
 

miLista=ListaPersonas() # Creamos la instancia de tipo ListaPersona
persona=Persona("Sandra", "Femenino", 29) # Nos creamos la persona pertinente. A medida que vamos creando aquí más persona, esta aparecerá y las creadas en el fichero externo anteriormente 
miLista.agregarPersonas(persona) #Esta persona se la pasamos al método agregarPersona que la recibe por parámetro en p
miLista.mostrarInfoFicheroExterno()

# p=Persona("Sandra", "Femenino", 29)
# miLista.agragarPersonas(p)

# miLista=ListaPersonas()
# p=Persona("Pepe", "Masculino", 23)
# miLista.agragarPersonas(p)

# miLista=ListaPersonas()
# p=Persona("Maria", "Femenino", 24)
# miLista.agragarPersonas(p)


# miLista.mostrarPersonas()

