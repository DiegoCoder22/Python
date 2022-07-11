import numpy as np
asientonom = []
asientovip = []
precionom = 78900
preciovip= 240000
contador = 1
asientonom = np.arange(1,31)
asientovip = np.arange(31,43)

def menu():
    print('Bienvenidos al Sistema DuocUC Aviones:')
    print('Seleccione una opción:')
    print('')
    print(' 1) Ver asientos disponibles')
    print(' 2) Comprar asiento')
    print(' 3) Anular vuelo')
    print(' 4) Modificar datos de pasajero')
    print(' 5) Salir')
    print('')

def salir():
    print('Ha cerrado la sesión')

continuar = True
while continuar:
    menu()
    validamenu = True
    while validamenu:
        try:
            op = int(input('Seleccione Opción: '))
            if op < 1 or op > 5:
                print('Ingrese una opcion válida.')
            else:
                validamenu = False
        except ValueError:
            print('Opcion incorrecta. Intente nuevamente...')

    if op==1:
        print('')
        print(f'Asientos Vuelo {contador}')
        print (asientonom.reshape(5,6))
        print('-----------------------------')
        print('-----------------------------')
        print(asientovip.reshape(2,6))
        print('-----------------------------')
        print('--Asientos disponibles = 0')
        print('--Asientos Comprados = X')
        print('-----------------------------')
        
    elif opcion == 2:
