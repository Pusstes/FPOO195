# Soy un comentario de 1 linea
'''
soy un comentario de 
varias 
lineas 
'''

# Practica 2: sintaxis

#un cometario

# 2. Cadenas

""" print('Esto es una cadena')
print("Soy otra cadena")"""

a = 'mi banda \n favorita es'
b= 'grupo marrano'

print(a+b)
print(a,b)

# contar caracteres
print(len(a))

print(b[2:5])
print(b[:5])
print(b[2:])

# 3 variables
x = 5
y = "john"
x = 4.6
z = 5
n = x+z


print(x)
print(y)
print(n)

print(type(x))
print (type(y))
print(type(n))

import random
numero = random.randrange(1,5)
print(numero)

# 4 solicitud de datos
var1 = input("introduce cualquier dato:")
var2 = str(input("Introduce una cadena: "))
var3 = int(input('ingresa un numero entero: '))
var4 = float(input('Introduce un flotante: '))

print(var1, var2, var3, var4)

# 5 Booleans, operadores de comparacion y logicos
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(10 >= 9)
print(10 != 9)
print(10 <= 9)

x = 1
print(x < 5 and x <10)
print(x < 5 or x < 10)
print(not(x < 5 and x < 10))