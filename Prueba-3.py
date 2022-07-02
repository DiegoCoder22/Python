import numpy as np
import os

nif=list();niftipo=list();nombre=list();edad=list();reg=list()
ciudadano=[nif, niftipo, nombre, edad, reg]

def salida():
    print("Gracias por utilizar el registro de ciudadanos de la Unión Europea de España, de Andalucía.")

while True:
    def menu():
        print('Bienvenido al registro de ciudadanos de la Unión Europea de España, de Andalucía')
        print('Seleccione una opción:')
        print('1) Ingrese ciudadano')
        print('2) Buscar ciudadano')
        print('3) Imprimir certificado')
        print('4) Salir')
    menu()
    op = input('Ingrese opción:')
    if op=='1': #Opcion 1
        while True: #Ciclo y validacion de nombre:
            xnombre = input('Ingrese su Nombre:')
            if len(xnombre)>=8:
                input('(OK) Nombre ingresado es correcto')
                break
            else:
                input('(X) Nombre ingresado es incorrecto... pulse una tecla...')
            nombre.append(xnombre)
        while True: #Ciclo y validacion de Edad:
            try:
                xedad = int(input('Ingrese edad:'))
                if xedad>=15 and xedad<=90:
                    input('(OK) Edad ingresada es correcta')
                    break
            except Exception as e:
                input('(X) datos ingresados tienen error....',e)
            edad.append(xedad)
        while True: #Ciclo y validacion de NIF:
            xnif = input('Ingrese NIF Ciudadano:')
            if len(xnif)==12 and (ndif[0:8].isnumeric() and ndif[9:12].isalpha()):
                input(f'(OK) NIF ingresado {xnif} es correcto')
                nif.append(xnif)
                break   
        while True: #Ciclo y validacion de Tipo de NIF:
            xniftipo = input('Ingrese tipo -RTX, -XXY, -PEU, -03F:')
            xniftipo = xniftipo.upper()
            if xniftipo=='-RTX' or xniftipo=='-XXY' or xniftipo=='-PEU' or xniftipo=='-03F':
                input(f'(OK) Tipo de NIF {xniftipo} ingresado es correcto.')
                break
            else:
                input('(X) NIF no válido, Precione tencla para intentar nuevamente....')
            niftipo.append(xniftipo)
            reg.append('reg:')
    elif op=='2': #Opcion 2
        cnif=input("Ingrese NIF del ciudadano: ")
        for i in range(len(nif)):
            if cnif in nif:
                print("NIF: ", nif[i])
                print("NOMBRE: ", nombres[i])
                print("EDAD: ", edades[i])
                input("INGRESE ENTER PARA CONTINUAR")
                break
            else:
                print("(X) El NIF ingresado no existe... intente nuevamente...")
    elif op=='3':  #Opcion 3
        xnif=input('Imprimir certificado:')
        nif, niftipo, nombre, edad, reg
        if xnif in nif:
            i=nif.index(xnif)
            print(f'El NIF es: {nif}')
            print(f'El NIF Tipo es: {tiponif}')
            print(f'El NIF completo es: {nif} + {tiponif}')
            print(f'El Nombre del ciudadano es: {nombre}')
            print(f'La edad del ciudadano es: {edad}')
            input('pulse una tecla para continuar....')
        else:
            input('El NIF no existe...')
    elif op=='4': #Opcion 4
        break
    else:
        input('opcion no válida, pulse para continuar...')
