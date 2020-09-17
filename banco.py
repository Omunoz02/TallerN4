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

		
		class Banco:

	def __init__(self):
		self.cliente1=Cliente(input("Nombre cliente 1: \n"))
		self.cliente2=Cliente(input("Nombre cliente 2: \n"))
		self.cliente3=Cliente(input("Nombre cliente 3: \n"))


	def operacion(self):
		self.cliente2.depositar(1000)
		self.cliente3.depositar(2000)
		self.cliente1.extraer(300)
		self.cliente1.depositar(5000)
		self.cliente3.depositar(5000)
		self.cliente2.extraer(500)
