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
