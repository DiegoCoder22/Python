patente=list();marca=list();modelo=list();ano=list();tipo=list();reg=list();
auto=[patente, marca, modelo, ano, tipo, reg]

while True:
    print('')
    print('1) Registrar Automovil')
    print('2) Registrar Mantenimiento')
    print('3) Consultar Automovil')
    print('4) Salir')
    op = input('Ingrese opción:')
    if op=='1': #Iniciamos el Ciclo 1: Si op es 1, entonces...
        while True: #Se inicia otro ciclo...
            try: #Si...
                xpat = input('Ingrese patente.......:')
                xmar = input('Ingrese marca.........:')
                xmod = input('Ingrese modelo........:')
                xano = int(input('Ingrese Ingrese año de fabricación.:'))
                xtip = input('Ingrese tipo d,b,e,h:')
                xtip = xtip.lower() #cadena de caracteres en minusculas.
                if len(xpat)==6: #Si  xpat (patente) contiene 6 caracteres (validacion).
                    if ((xpat[0:2].isalpha() and xpat[2:2+4].isnumeric()) or (xpat[0:4].isalpha() and xpat[4:4+2].isnumeric())):
                        if len(xmar)!=0: #validacion, si el largo de xmar no es igual a 0.
                            if len(xmod)!=0: #validacion si no es igual a 0.
                                if xano>=1900 and xano<=2022: #validacion si lo ingresado esta dentro de 1900 y 2022
                                    if xtip=='b' or xtip=='d' or xtip=='e' or xtip=='h': #validacion si el caracter ingresado es b,d,e,h.
                                        input:('datos ingresados correctamente')
                                        break
            except Exception as e: #si estos datos no se cumplen...
                input('datos ingresados tienen error....', e) #mostrará este error...
        patente.append(xpat);marca.append(xmar);modelo.append(xmod);ano.append(xano);tipo.append(xtip);reg.append('Reg:')
    elif op=='2':#Iniciamos el Ciclo 1: Si op es 1, entonces...
        xpat=input('Ingrese patente:') #ingresamos patente...
        if xpat in patente: #Si xpat existe dentro de la lista patente...
            i=patente.index(xpat)
            xfec=input('Ingrese fecha:')
            xobs=input('Ingrese observaciones:')
            reg[i]=reg[i]+xfec+"-"+xobs #Al registro le sumo la fecha y las observaciones... es un acumulador
            input('OK...pulse una tecla para continuar...') #cumple la validacion...
        else: #Si no cumple la validacion o no encuentra la patente... aparece el error...
            input('Patente no existente...')
    elif op=='3':
        xpat=input('Ingrese patente:')
        if xpat in patente:
            i=patente.index(xpat)
            print(f'{auto[0][i]} - {auto[1][i]} - {auto[2][i]} - {auto[3][i]} - {auto[4][i]} - {auto[5][i]})
            print('....')
        else: #si no cumple con la condición, imprime un error...
            input('La patente ingresada no existe...')
    elif op=='4':
        break
    else:
        input('opcion no válida, pulse para continuar...')
