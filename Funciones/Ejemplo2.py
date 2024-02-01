import math

def area_cuadrado(lado):
    return lado ** 2

def main():
    lado_cuadrado = float(input('Ingresa valor del lado: '))
    resultado = area_cuadrado(lado_cuadrado)
    print(f"EL area del cuadrado es: {resultado}")