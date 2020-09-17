class Agenda:
	
	def __init__(self):
		print(">>>>>>>PROBLEMA 2: AGENDA<<<<<<<")
		self.contactos=[]
 
	
	def menu(self):
		print()
		menu=[
			['------ Agenda ------'],
			['1. Añadir Contacto',"anadir"],
			['2. Lista de contactos'],
			['3. Buscar contacto'],
			['4. Editar contacto'],
			['5. Cerrar agenda']
		]
 
		for x in range(6):
			print(menu[x][0])

		opcion=int(input("Introduzca la opción deseada:\n"))
		if opcion==1:
			print("\n")
			self.anadir()

		elif opcion==2:
			print("\n")
			self.lista()

		elif opcion==3:
			print("\n")
			self.buscar()

		elif opcion==4:
			print("\n")
			self.editar()

		elif opcion==5:
			print("\n")
			print("Agenda cerrada, vuelve pronto")
			exit()

	
 
		
		self.menu()

		
		def anadir(self):
		print(">>>Añadir nuevo contacto<<<")
		print("\n")
		nombre=input("Introduzca el nombre: ")
		telefono=int(input("Introduzca el teléfono: "))
		email=input("Introduzca el email: ")
		self.contactos.append({'nombre':nombre,'telefono':telefono,'email':email})
		
 

	def lista(self):
		print(">>>>Lista de contactos<<<<")
		print("\n")
		if len(self.contactos) == 0:
			print("No se ha añadido un contacto en la agenda")
		else:
			for x in range(len(self.contactos)):
				print(f"CONTACTOS:: {self.contactos[x]['nombre']}")
		

	def buscar(self):
		print(">>>>Buscador de contactos<<<<")
		print("\n")
		nom=input("Introduzca el nombre del contacto: \n")
		for x in range(len(self.contactos)):
			if nom == self.contactos[x]['nombre']:
				print(">>>>Datos del contacto<<<<")
				print("Nombre: ",self.contactos[x]['nombre'])
				print("Teléfono: ",self.contactos[x]['telefono'])
				print("E-mail: ",self.contactos[x]['email'])
				return x
	def editar(self):
		print(">>>>Editar contacto<<<<")
		print("\n")
		data=self.buscar()
		condition=False
		while condition==False:
			print("Selecciona que quieres editar: \n")
			print("1.Nombre")
			print("2.Teléfono")
			print("3.E-mail")
			print("4.Volver")
			option=int(input("Ingrese la opción deseada: \n"))
			if option==1:
				nom=input("Ingrese el nuevo nombre: \n")
				self.contactos[data]['nombre']=nombre
			elif option==2:
				telf=input("Ingrese el nuevo teléfono:\n ")
				self.contactos[data]['telf']=telefono
			elif option==3:
				email=input("Introduzca el nuevo email: \n")
				self.contactos[data]['email']=email
			elif option==4:
				condition=True
 
 
 
def main():
    agenda=Agenda()
    agenda.menu()

if __name__== "__main__":
    main()
