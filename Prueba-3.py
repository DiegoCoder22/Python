from prueba-3-fn import agregar
from prueba-3-fn import Buscar
from prueba-3-fn import Imprimir
from prueba-3-fn import salir
import os
#nif=list();niftipo=list();nombre=list();edad=list();reg=list()
#ciudadano=[nif, niftipo, nombre, edad, reg]

nif=[]
niftipo=[]
nombre=[]
edad=[]
reg=[]

while True:
    def menu():
        print('')
        print('Bienvenido al registro de ciudadanos de la Unión Europea de España, de Andalucía')
        print('Seleccione una opción:')
        print('')
        print('1) Ingrese ciudadano')
        print('2) Buscar ciudadano')
        print('3) Imprimir certificado')
        print('4) Salir')
    menu()
    op = input('Ingrese opción:')
    if op=='1': #Opcion 1
        while True: #Ciclo y validacion de nombre:
            xnombre = input(f'Ingrese su Nombre {contador}: ')
            if len(xnombre)>=8:
                input('(OK) Nombre ingresado es correcto')
                nombre.append(xnombre)
                reg.append(reg)
                break
            else:
                input('(X) Nombre ingresado es incorrecto... pulse una tecla...')
        while True: #Ciclo y validacion de Edad:
            try:
                xedad = int(input('Ingrese edad:'))
                if xedad>=15 and xedad<=90:
                    input('(OK) Edad ingresada es correcta')
                    edad.append(xedad)
                    reg.append(reg)
                    break
            except Exception as e:
                input('(X) datos ingresados tienen error....',e)
        while True: #Ciclo y validacion de NIF:
            xnif = input('Ingrese NIF Ciudadano:')
            if len(xnif)==8 or ((xnif[0:8].isalpha() and xnif[2:2+4].isnumeric()) or (xnif[0:4].isalpha() and xnif[4:4+2].isnumeric())):
                input(f'(OK) NIF ingresado {xnif} es correcto')
                nif.append(xnif)
                reg.append(reg)
                break   
        while True: #Ciclo y validacion de Tipo de NIF:
            xniftipo = input('Ingrese tipo -RTX, -XXY, -PEU, -03F:')
            xniftipo = xniftipo.upper()
            if xniftipo=='-RTX' or xniftipo=='-XXY' or xniftipo=='-PEU' or xniftipo=='-03F':
                input(f'(OK) El de NIF: {xnif} y el NIF Tipo: {xniftipo} ingresados son correctos.')
                niftipo.append(xniftipo)
                reg.append(reg)
                break
            else:
                input('(X) NIF no válido, Precione tencla para intentar nuevamente....')
    elif op=='2': #Opcion 2
        cnif=input('Ingrese NIF del ciudadano: ')
        for i in range(len(nif)):
            if cnif in nif:
                print('')
                print('Se ha encontrado al Ciudadano consutado: ')
                print('')
                print('Datos del ciudadano: ')
                print('NIF: ', nif[i])
                print('Tipo NIF: ', niftipo[i])
                print('Nombre: ', nombre[i])
                print('Edad: ', edad[i])
                print('')
                input('Ingrese una tecla para continuar...')
                break
            else:
                print('El NIF ingresado no existe en el sistema... intente nuevamente...')
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
