import os

nif=list();niftipo=list();nombre=list();edad=list();reg=list()
ciudadano=[nif, niftipo, nombre, edad, reg]

while True:
    print('Bienvenido al registro de ciudadanos de la Unión Europea de España, de Andalucía')
    print('Seleccione una opción:')
    print('1) Ingrese ciudadano')
    print('2) Buscar ciudadano')
    print('3) Imprimir certificado')
    print('4) Salir')
    op = input('Ingrese opción:')
    if op=='1':
        while True:
            try:
                xnombre = input('Ingrese su Nombre:')
                if len(xnombre)>=8:
                    input('Nombre ingresado es correcto')
                else:
                    input('Nombre ingresado es incorrecto')
                break
                xedad = int(input('Ingrese edad:'))
                if xedad>=15 and xedd<=90:
                    input('Edad ingresada es correcta')
                else:
                    input('Edad ingresada es incorrecta')
                break
                xnif = input('Ingrese NIF Ciudadano:')

                xniftipo = input('Ingrese tipo -RTX, -XXY, -PEU, -03F:')
                if len(xnif)==8:
                    input(f'NIF ingresado {xnif} es correcto')
                else:
                    input('NIF no válido')
                    input('Precione tencla para intentar nuevamente....')
                    break
                    if ((xnif[0:3].isalpha() and xnif[2:2+4].isnumeric()) or (xnif[0:4].isalpha() and xnif[4:4+2].isnumeric())):
                        if len(xnombre)!=8: #validacion, si el largo de xmar no es igual a 0.
                            if len(xedad)!=0: #validacion si no es igual a 0.
                                xniftipo = xniftipo.upper()
                                if xniftipo=='-RTX' or xniftipo=='-XXY' or xniftipo=='-PEU' or xniftipo=='-03F':
                                    input('datos ingresados correctamente')
                                    break
            except Exception as e:
                input('datos ingresados tienen error....',e)
        nif.append(xnif);nombre.append(xnombre);edad.append(xedad);niftipo.append(xniftipo);reg.append('Reg:')
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
