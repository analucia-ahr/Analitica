#!/usr/bin/env python
# coding: utf-8

# # Arte de la Analítica
# 
# *1.Escribir una función de Python que encuentre los números primos en los primeros N números naturales.
# N es el argumento de la función
# Llamar la función desde el código principal*
# 
# *2.Escribir una función de Python que encuentre el producto cruz en vectores de 3 componentes.
# La función recibe dos listas (vectores)
# La función regresa un tercer vector (lista) con el resultado
# Llamar a la función desde el código principal*
# 
# *3.Re-escribir el problema 2, pero ahora los vectores son leídos desde un archivo de texto.*

# In[29]:


import math
def num_primo(N):
    nat = [*range(1, N+1)]
    primos = []
    for i in range(2, len(nat)):
        isPrime = True
        for q in range(2, int(math.sqrt(i))+1):
            if nat[i] % q == 0:
                isPrime = False
                break
        if isPrime:
            primos.append(nat[i])
    return primos
p = num_primo(20)
print(p)


# In[30]:


def cross(a, b):
    c = []
    c.append(a[1]*b[2]-a[2]*b[1])
    c.append(a[2]*b[0]-a[0]*b[2])
    c.append(a[0]*b[1]-a[2]*b[1])
    return c

x = [1.2, 3.7, -0.25]
y = [-0.44, -2.8, 7]
cr = cross(x, y)
print("a =", x)
print("b =", y)
print("a x b =", cr)


# In[31]:


import csv 
filas = []
with open("vectores.csv", 'r') as file:
    csvr = csv.reader(file)
    for row in csvr:
        filas.append(row)
    print(filas)
    
x = [float(filas[0][0]), float(filas[0][1]), float(filas[0][2])]
cr = cross(x, y)
print("a =", x)
print("b =", y)
print("a x b =", cr)

