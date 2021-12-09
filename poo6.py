import os

total = 0

class Cliente:
    def __init__(self, nombre, cantidad=0):
        self.__nombre = nombre
        self.__cantidad = cantidad

    def darnombre(self):
        return self.__nombre

    def depositar(self):
        self.__cantidad = 0
        deposito = float(input("Ingrese la cantidad a depositar: "))
        self.__cantidad += deposito
        self.__cantidad

    def extraer(self):
        retiro = float(input("Ingrese la cantidad a retirar: "))
        self.__cantidad -= retiro
        self.__cantidad


    def mostrar_total(self):
        return self.__cantidad


class Banco(Cliente):
    def __init__(self, nombre, cantidad=0):
        super().__init__(nombre, cantidad)

    def operar(self):
        
        while True:
            os.system('cls')
            print("\nBienvenido", Cliente.darnombre(self))
            print("\nIngrese una opcion:\n")
            print("1) Depositar")
            print("2) Retirar")
            print("3) Ver saldo")
            print("4) Salir")
            opcion = input("\n--->")
            if opcion == "1":
                Cliente.depositar(self)  
            elif opcion == "2":
                Cliente.extraer(self)  
            elif opcion == "3":
                print("Saldo cliente: ", Cliente.mostrar_total(self))
            elif opcion == "4":
                print("Hasta pronto!")
                break
            else:
                print("Opcion incorrecta, intente nuevamente")

            input("Presione ENTER para continuar")
        
    def deposito_total(self):
        global total
        total += Cliente.mostrar_total(self)
        print("Arca total del banco: ", total)

cliente1 = Banco("Raul Gonzalez")
cliente1.operar()
cliente1.deposito_total()
cliente2 = Banco("Juan Perez")
cliente2.operar()
cliente2.deposito_total()