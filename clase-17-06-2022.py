# Funciones:#
# Son aquellas que dividen el programa en partes, considerando la parte princila y los diferentes metodos (tareas) que deben realizar.
# Las funciones deben ser embocadas.#
# Tipos de funciones:#
# 1) sin argumentos y sin retornos #
# 2) sin argumentos y con retorno #
# 3) con argumentos y sin retonro #
# 4) con argumentos y con retonro #

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