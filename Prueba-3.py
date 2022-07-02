import os
nif=list();niftipo=list();nombre=list();edad=list();reg=list()
ciudadano=[nif, niftipo, nombre, edad, reg]

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
    if op=='1':
        while True: #Ciclo y validacion de nombre:
            xnombre = input('Ingrese su Nombre:')
            if len(xnombre)>=8:
                input('(OK) Nombre ingresado es correcto')
                break
            else:
                input('(x) Nombre ingresado es incorrecto... pulse una tecla...')
            nombre.append(xnombre)
        while True: #Ciclo y validacion de Edad:
            try:
                xedad = int(input('Ingrese edad:'))
                if xedad>=15 and xedad<=90:
                    input('Edad ingresada es correcta')
                    break
            except Exception as e:
                input('datos ingresados tienen error....',e)
            edad.append(xedad)
        while True:
            xnif = input('Ingrese NIF Ciudadano:')
            if len(xnif)==8 or ((xnif[0:8].isalpha() and xnif[2:2+4].isnumeric()) or (xnif[0:4].isalpha() and xnif[4:4+2].isnumeric())):
                input(f'NIF ingresado {xnif} es correcto')
                break
                nif.append(xnif)
        while True:
            xniftipo = input('Ingrese tipo -RTX, -XXY, -PEU, -03F:')
            xniftipo = xniftipo.upper()
            if xniftipo=='-RTX' or xniftipo=='-XXY' or xniftipo=='-PEU' or xniftipo=='-03F':
                input(f'Tipo de NIF {xniftipo} ingresado es correcto.')
                break
            else:
                input('NIF no válido, Precione tencla para intentar nuevamente....')
            niftipo.append(xniftipo)
            reg.append('reg:')
    elif op=='2':
        xnif=input('Ingrese NIF Ciudadano:')
        if xnif in nif:
            i=nif.index(xnif)
            reg[i]=reg[i]+xfec+"-"+xobs #Al registro le sumo la fecha y las observaciones... es un acumulador
            input('OK...pulse una tecla para continuar...') #cumple la validacion...
        else:
            input('Patente no existente...')
    elif op=='3':
        xnif=input('Ingrese patente:')
        if nif in nif_eu:
            i=nif_eu.index(xnif)
            print(f'{ciudadano[0][i]} - {ciudadano[1][i]} - {ciudadano[2][i]} - {ciudadano[3][i]} - {ciudadano[4][i]}')
            print('....')
        else:
            input('La patente ingresada no existe...')
    elif op=='4':
        break
    else:
        input('opcion no válida, pulse para continuar...')
