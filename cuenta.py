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

    class plazoFijo(cuenta):
        def __init__(self):
            super().__init__()
            self.plazo = "6 meses"
            self.interes = 0.15
        def importeInteres(self):
            self.importe = (self.cantidad*self.interes)/100
            return self.importe

        def mostrarDatos(self):
            self.intereses = self.importeInteres()
            print("\n<<<<Datos del titular>>>> \n")
            super().imprimir()
            print(f"EL plazo de pago es de {self.plazo}")
            print(f"La cuota de interes es del {self.interes}")
            print(f"El total de intereses es de: {self.intereses} \n")


    def mostrarDatosFinales():
        inter = plazoFijo()
        inter.mostrarDatos()

    def mostrarCaja():
        caja = cajaAhorro()
        caja.mostrarCajaAhorro()

    def imprimirCuenta():
        cuenta1 = cuenta()
        cuenta1.imprimir()
