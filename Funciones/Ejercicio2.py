# Escribir una funcion que calcule el area de un circulo 
# y otra el volumen de un cilindro usando la primera funcion.

import math

def area_circulo(radio):
    return math.pi * radio ** 2

def VolumenCilindro(area, altura):
    return area * altura

print('Calcularemos el area de un circulo:')
radio = float(input('Ingrese el radio del cilindro en metros: '))
altura= float(input('Ingresa la altura del cilindro en metros: '))

area = area_circulo(radio)
volumen = VolumenCilindro(area, altura)

print(f"El volumen del cilindro con radio: '{radio}' y altura: '{altura}' es: '{volumen}'")

    