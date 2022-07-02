import numpy as np
import os
nif=[]
nombres=[]
edades=[]
fechanac=[]
estadoscon=[]

def menu():
    print("BIENVENIDOS")
    print("1) INGRESAR CIUDADANO")
    print("2) BUSCAR CIUDADANO")
    print("3) IMPRIMIR CERTIFICADO")
    print("4) SALIR")


def salir():
    print("gracias")

continuar = True
while continuar:
    os.system('cls')
    menu()
    validamenu = True
    while validamenu:
            try:
                opcion = int(input("SELECCIONE OPCION: "))
                if opcion < 1 and opcion > 4:
                    print("INGRESE OPCION VALIDA")
                else:
                    validamenu = False
            except ValueError:
                    print("no es valida la opcion")

            if opcion == 1:
                ndif=(input("INGRESAR NIF: "))
                if len(ndif) == 12 and (ndif[0:8].isnumeric() and ndif[9:12].isalpha()):
                    nif.append(ndif)
                else:
                    print("ingrese nif valido")
                    input("ingrese enter para continuar")
                    break
                nombre=(input("INGRESAR NOMBRE COMPLETO: "))
                if len(nombre) == len(nombre) > 8:
                    nombres.append(nombre)
                else:
                    print("ingrese nombre valido")
                    break
                edad=int(input("INGRESAR EDAD: "))
                if edad > 0 :
                    edades.append(edad)
                else:
                    print("ingrese edad valida")
                    break
                fechanacimiento=(input("INGRESAR FECHA DE NACIMIENTO XX/XX/XXXX: "))
                if len(fechanacimiento) == 10:
                    fechanac.append(fechanacimiento)
                else:
                    print("ingrese fecha valida")
                    break
                estadoconyugal=(input("INGRESE ESTADO CONYUGAL: SOLTERO-CASADO-DIVORCIADO-VIUDO: "))
                if (estadoconyugal.isalpha()):
                    estadoscon.append(estadoconyugal)
                else:
                    print("ingrese dato valido")
                    break
            elif opcion == 2:
                ndifconsulta=input("ingrese nif del ciudadano: ")
                for i in range(len(nif)):
                    if ndifconsulta in nif:
                        print(" SE ENCONTRO AL CIUDADANO:")
                        print("NIF: ", nif[i])
                        print("NOMBRE: ", nombres[i])
                        print("EDAD: ", edades[i])
                        input("INGRESE ENTER PARA CONTINUAR")
                        break
                    else:
                        print("el nif ingresado no existe")
            elif opcion == 3:
                print("1)CERTIFICADO DE NACIMIENTO")
                print("2)CERTIFICADO DE ESTADO CONYUGAL")
                opcert=int(input("INGRESE OPCION: "))
                if opcert==1:
                    ndifconsulta=input("ingrese nif del ciudadano: ")
                    for i in range(len(nif)):
                        if ndifconsulta in nif:
                            print("--------CERTIFICADO DE NACIMIENTO---------")
                            print(nombres[i], "NACIDO EN ANDALUCIA EN LA FECHA DEL", fechanacimiento[i])
                            print("NIF: ", nif[i])
                            input("INGRESE ENTER PARA CONTINUAR")
                            break
                if opcert==2:
                    ndifconsulta=input("ingrese nif del ciudadano: ")
                    for i in range(len(nif)):
                        if ndifconsulta in nif:
                            print("--------CERTIFICADO DE ESTADO CONYUGAL---------")
                            print(nombres[i], "NACIDO EN ANDALUCIA EN LA FECHA DEL", fechanacimiento[i])
                            print("NIF: ", nif[i])
                            print("SU ESTADO CONYUGAL ES:", estadoscon[i])
                            input("INGRESE ENTER PARA CONTINUAR")
                            break
                else:
                    print("el nif ingresado no existe")
            elif opcion == 4:
                print("HASTA PRONTO")
                print("BY:NICOLAS CHAVEZ")
                salir()
                continuar = False
