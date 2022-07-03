import funciones as fn

while True:
    op = fn.menu() # debo agregar fn a cada funcion que estamos importando
    if op=='1':
        fn.agregar()
    elif op =='2':
        fn.buscar()
    elif op =='3':
        fn.imprimir()
    elif op =='4':
        fn.salida()
    else:
        fn.error400()