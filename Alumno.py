# TallerN4

class Alumno:
    def __init__(self):
        print("<<<<<<<PROBLEMA 1: ALUMNO>>>>>>")
        self.nombre = input("Digite el nombre del alumno: \n")
        self.nota = float(input("Digite la nota(0-5) del alumno: \n"))
 
 
    # función para imprimir los datos
    def imprimir(self):
               print(f"Nombre del Alumno: {self.nombre}")
               print(f"Nota del alumno: {self.nota}")
