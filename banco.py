class Cliente:

	def __init__(self,nombre):
		self.nombre=nombre
		self.cantidad=0


	def depositar(self,cantidad):
		self.cantidad+=cantidad


	def extraer(self,cantidad):
		self.cantidad-=cantidad


	def devolver_cantidad(self):
		return self.cantidad

	def imprimir(self):
		print(self.nombre, " tiene depositada una cantidad de ",self.cantidad )
		print("")
