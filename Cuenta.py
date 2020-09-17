# TallerN4

  
import os

def Menu():
    print("<<<<<<<<<PROBLEMA 4: CUENTA>>>>>>>>>>")

    class cuenta:
        def __init__(self):
            self.titular= "Miguel Alfonso Cierra"
            self.cantidad= 25350000

        def imprimir(self):
            print(f"Nombre del titular: {self.titular} ")
            print(f"Cantidad: {self.cantidad} \n")

    class cajaAhorro(cuenta):
        def __init__(self):
            super().__init__()
            
        def mostrarCajaAhorro(self):
            super().imprimir()

   
