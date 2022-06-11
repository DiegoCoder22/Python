import numpy as np
#array unidimencional
a = np.array([1,2,3,4,5,6,7,8,9])
#print(a)
#a = a**2
#print(a.ndim)

#array bidimencional
m = np.array([[0,2,4],[1,3,5]])
print(m)
print(m.ndim)
print(m.shape) #muestra la cantidad de "filas" y cantidad de elementos que contiene cada fila
print(m[0,1]) # primer numero indice o fila, segundo numero columna
print(m[0]) # muestra los numeros de la primera lista

for i in range(2): #el numero de la lista
    for j in range(3): #cantidad de elementos
        print(m[i,j]) #
        print(f'i:{i}-j:{j}') #aca se ejecuta un ciclo
        break

h = np.ones((30,3)) # Generamos una Matriz
h = h*2
print(h)