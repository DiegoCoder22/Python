def agregar():
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