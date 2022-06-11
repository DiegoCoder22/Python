import numpy as np
import random as rd #lo asignamos como rd para generar numeros enteros aleatoreos.
m = np.ones((10,3)) #ponemos input
f = len(m)
c = len(m[0])
for i in range(f): # iniciamos el ciclo
    for j in range(c):
        m[i,j] = (rd.randint(10,70)) /10 #aca hacemos que sean decimales
print(m)