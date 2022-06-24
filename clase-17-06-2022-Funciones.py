# Funciones:#
# Son aquellas que dividen el programa en partes, considerando la parte princila y los diferentes metodos (tareas) que deben realizar.
# Las funciones deben ser embocadas.#
# Tipos de funciones:#
# 1) sin argumentos y sin retorno #
# 2) sin argumentos y con retorno #
# 3) con argumentos y sin retorno #
# 4) con argumentos y con retorno #


# 1) sin argumentos y sin retornos:
def saludar(): # cramos la duncion
    print('Hola chuchetumare') # los argumentos van dentro del parentesis.

saludar() # aca estamos ejecutando la funcion


# 2) sin argumentos y con retorno #
def sumar(a,b):
    a=int(input('Ingrese Valor:'))
    b=int(input('Ingrese Valor:'))
    c=a+b
    return c

x=sumar()

# 3) con argumentos y sin retonro #
def sumar(a,b):
    c=a+b
    print(f'la suma de {a} + {b} = {c}')

x=int(input('Ingrese valor:'))
x=int(input('Ingrese valor:'))
sumar(x,y)


# 4) con argumentos y con retorno #
def sumar(a,b):
    c=a+b
    return c

x=int(input('Ingrese valor:'))
x=int(input('Ingrese valor:'))
print(sumar(a,b))


# Len es una funcion para medir el largo de un sting
nombre='juan'
print(len(nombre))

def varios_valores(*args): #arg es una funcion flexible en donde puedo ingresar varios tipos de argumentos.
    for a in args: # aca asignamos las funciones "a" y "args" dentro de un ciclo.
        print(a)

varios_valores(4.5, 'juan', [1,2,3,4,5])

import os
    menu(): # funcion menú
    os.system('cls')
    print('Menú')
    print('1) Agregar')
    print('2) Eliminar')
    print('3) Salir')
    op=input('Ingrese Opción')
    return op #

# Aca definimos las funciones en las cuales del agregamos un print:
def agregar():
    print('eligio agregar')

def elimiar():
    print('eligio agregar')

def error400():
    print('Opción no válida')

#Importamos la funcion desde otro archivo .py:

import funciones as fn # FN es la variable que debo agregar para citar y activar las funciones desde otro archivo (se puede poner cualquier nombre para FN) o un alias

#Inicio de cliclo:
while True:
    op = fn.menu() # debo agregar fn a cada funcion que estamos importando
    if op=='1':
        fn.agregar()
    elif op =='2':
        fn.eliminar()
    elif op =='9':
        break
    else:
        fn.error400()
    input()

# un nuevo ejemplo de funciones por separado
# es mejor ponerle argumento a las funciones para garantizar que hagan lo que tengan que hacer

def mostrar(a):
    print(a)

a=[1,2,3]
mostrar()