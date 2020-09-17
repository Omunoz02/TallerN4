# TallerN4

class Alumno:
    def __init__(self):
        print("<<<<<<<PROBLEMA 1: ALUMNO>>>>>>")
        self.nombre = input("Digite el nombre del alumno: \n")
        self.nota = float(input("Digite la nota(0-5) del alumno: \n"))
 
 

    def imprimir(self):
               print(f"Nombre del Alumno: {self.nombre}")
               print(f"Nota del alumno: {self.nota}")


    def resultado(self):
               if self.nota < 3:
                              print(">>>>>El alumno ha reprobado<<<<<<")
               else:
                              print(">>>>>El alumno ha aprobado<<<<<<")
def main():
    alumno1 = Alumno()
    alumno1.imprimir()
    alumno1.resultado()


if __name__== "__main__":
    main()
