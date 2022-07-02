import os
rut=list()
cp1=list()
cp2=list()
cp3=list()
alumno=[rut,cp1,cp2,cp3]
contador=1
while True:
    os.system('cls')
    #MENU DE OPCIONES
    print('SISTEMA DE NOTAS')
    print('1 INGRESAR NOTAS')
    print('2 MOSTRAR PROMEDIO DE ALUMNOS')
    print('3 MOSTRAR NOTA DE LOS ALUMNOS')
    print('4 MOSTRAR APROBADOS Y REPROBADOS')
    print('9 SALIR')
    op=input('INGRESE OPCION : ')
    if op=='1':
        xrut=input(f'INGRESE RUT DEL ALUMNO {contador}:')
        xcp1=float(input('ingrese nota control 1:'))
        xcp2=float(input('ingrese nota control 2:'))
        xcp3=float(input('ingrese nota control 3:'))
        rut.append(xrut)
        cp1.append(xcp1)
        cp2.append(xcp2)
        cp3.append(xcp3)
        contador=contador+1
    elif op=='2':
        print('CALCULO DE PROMEDIOS')
        acum=0
        n=len(rut)
        for i in range(n):
            prom=cp1[i]*0.3 + cp2[i]*0.35 +cp3[i]*0.35
            print(f'{alumno[0][i]} - promedio {prom}')
            acum=acum+prom
        prom_curso = acum/n
        print(f'el promedio del curso es {prom_curso}')
        input('pulse una tecla para continuar...')
    elif op=='3':
        n=len(rut)
        for i in range(n):
            print(f'{alumno[0][i]} {alumno[1][i]} {alumno[2][i]} {alumno[3][i]}')
        input('pulse una tecla para continuar....')
    elif op=='4':
        print('MOSTRAR APROBADOS Y REPROBADOS')
        n=len(rut)
        con_apro=0
        con_repr=0
        aux_mensaje=''
        for i in range(n):
            prom=cp1[i]*0.3 + cp2[i]*0.35 +cp3[i]*0.35
            prom=(int(prom*10))/10
            if prom>=3.95:
                con_apro=con_apro+1
                aux_mensaje='APROBADO'
            else:
                con_repr=con_repr+1
                aux_mensaje='REAPROBADO'
            print(f'{alumno[0][i]} - promedio {prom} {aux_mensaje}')

        print(f'hay {con_apro} alumnos aprobados')
        print(f'hay {con_repr} alumnos reprobados')
        input('pulse una tecla para continuar...')

    elif op=='9':
        break
    else:
        input('OPCION NO VALIDA...PULSE UNA TECLA PARA CONTINUAR...')
